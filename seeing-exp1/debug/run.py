"""Experiment 1m, one world: XML with the run in words, plus a debugger agent, and optionally built one stage at a time.

    python -m debug.run --model gpt-6.1 --brief cascade8 --seed 0 --debugger            # 1j's XML arm + debugger
    python -m debug.run --model gpt-6.1 --brief cascade8 --seed 0 --debugger --staged   # + link-at-a-time, frozen links
    python -m debug.run --model dry-run --brief cascade8 --seed 0 --debugger --staged   # plumbing, no calls

Why: the free check (ladder/results_breaks/breaks.md) found builders see where a long chain breaks but about half their
revisions leave the first break where it was, and some break links that held. Jono, 2026-10-09: "A talking debugger is
great! It might as well be an agent too." and, on building it with link-at-a-time building, "Go for it!".

Control is 1j's XML-with-words arm (same briefs, model, seeds, prompts, run in words, three rounds), already run.
- --debugger: whenever the builder's file fails, a second GPT-6.1 (debug/agent.py) questions the run through
  debug/tools.py and its report goes to the builder beside the run in words.
- --staged: the chain is built in stages (2 links at a time for 8 steps, 4 for 16). Each stage gets up to three rounds;
  a file that breaks a link from an earlier stage is refused and the last good file kept (frozen links).
The number to beat: the share of revisions that move the first break forward without losing a link (1j: XML with
words 26 of 48). Also: worlds that work, steps held, tokens and cost per world.
"""

from __future__ import annotations

import argparse
import json
import sys
import time

from config import ROOT
from debug import agent as debugger
from debug.tools import Session, first_break
from harder.run import parse_verdict
from hundred import settle, words
from hundred.briefs import names_xml
from hundred.run import judge, judge_xml
from langrun.run import prompt as langrun_prompt
from ladder import briefs as ladder_briefs
from loop.models import MODELS, extract_block, open_chat, text

HERE = ROOT / "debug"
PROMPTS = HERE / "prompts"
RESULTS = HERE / "results"
RUNS = RESULTS / "runs"
LEDGER = RESULTS / "spend.jsonl"
DRY = ROOT / ".dryrun" / "debug"
MAX_ROUNDS = 3
MAX_LOAD_RETRIES = 2
STAGE = {8: 2, 16: 4}
SYSTEM = "You build MuJoCo scenes that do what their briefs say, and you check them honestly."

# 1m's own ceiling. $0 while paid runs were paused (Jono, 2026-10-09 04:30). Raised to $15 when Jono chose "Debugger
# test only" (2026-10-09 18:20) on a card offering the debugger on the stuck cases with a $15 ceiling (debug/stuck.py).
# The staged and debugger worlds of run.py are not approved yet.
CEILING_1M_USD = 15.0


def own(name: str, **kw) -> str:
    s = (PROMPTS / f"{name}.md").read_text()
    for k, v in kw.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def check_budget() -> None:
    from config import SPEND_CAP_USD
    from hundred import budget
    from loop.models import BudgetExceeded, spent_usd
    s = spent_usd(LEDGER)
    total = sum(budget.spent().values()) + s
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} across all experiments, the ${SPEND_CAP_USD:.0f} program cap")
    if s >= CEILING_1M_USD:
        raise BudgetExceeded(f"1m has spent ${s:.2f}, its ${CEILING_1M_USD:.0f} ceiling; going on needs Jono")


def chain_list(lines: list[str], start: int = 1) -> str:
    return "\n".join(f"{k}. {line}" for k, line in enumerate(lines, start))


def dry_script(brief: str) -> list[str]:
    from langrun.settings import FIXTURES
    ok = '```json\n{"what_happens": "dry run", "works": false, "problem": "dry"}\n```'
    xml = "```xml\n<mujoco>\n  <option timestep=\"0.002\"/>\n  <worldbody>\n    <geom name=\"floor\" type=\"plane\" size=\"5 5 0.1\"/>\n    <body name=\"ball1\" pos=\"0 0 1\">\n      <freejoint/>\n      <geom name=\"ball1_sphere\" type=\"sphere\" size=\"0.05\" mass=\"0.2\"/>\n    </body>\n  </worldbody>\n</mujoco>\n```"
    return [xml] + [ok + "\n\n" + xml] * 40


def dry_debugger_script() -> list[str]:
    return ["```ask\nstatus\nwhy 1\nforks 1\nwatch ball1 0 1\n```", "```report\ndry report\n```"] * 40


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(MODELS))
    ap.add_argument("--brief", required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--effort", default="high")
    ap.add_argument("--debugger", action="store_true")
    ap.add_argument("--staged", action="store_true")
    args = ap.parse_args(argv)

    spec = MODELS[args.model]
    dry = spec.provider == "dry"
    B = ladder_briefs.load()[args.brief]
    chain, seconds = B["test"], B.get("seconds", 6.0)
    arm = "xml" + ("+debugger" if args.debugger else "") + ("+staged" if args.staged else "")
    wid = f"{args.model}__{args.brief}__{arm.replace('+', '_')}__s{args.seed}"
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    out = (DRY if dry else RUNS) / wid / stamp
    out.mkdir(parents=True, exist_ok=True)
    ledger = None if dry else LEDGER
    chat = open_chat(args.model, SYSTEM, args.effort, tag=f"1m/{wid}", script=dry_script(args.brief) if dry else None,
                     ledger=ledger)
    dchat_args = (args.model, debugger.SYSTEM, args.effort)

    rec = {"world": wid, "experiment": "1m", "brief": args.brief, "family": B.get("family"), "steps": len(chain),
           "sim_seconds": seconds, "model": args.model, "arm": arm, "seed": args.seed, "dry_run": dry,
           "debugger": args.debugger, "staged": args.staged, "test": chain, "brief_text": B["brief"], "files": [],
           "turns": [], "revisions": [], "debugger_calls": 0}
    calls, t0 = [], time.monotonic()

    def send(c, parts, name):
        if not dry:
            check_budget()
        r = c.send(parts)
        calls.append(r)
        (out / f"{name}_reply.md").write_text(r.text)
        return r

    def full_state(xml: str) -> dict | None:
        s = Session(xml, "xml", chain, seconds)
        return s.state

    def report_for(xml: str, sub: list[str], label: str) -> str:
        s = Session(xml, "xml", sub, seconds)
        dchat = open_chat(*dchat_args, tag=f"1m/{wid}/debugger", script=dry_debugger_script() if dry else None,
                          ledger=ledger)
        if not dry:
            check_budget()
        report, replies = debugger.debug(s, B["brief"], dchat, out, label)
        calls.extend(replies)
        rec["debugger_calls"] += len(replies)
        return report

    first = langrun_prompt("author_xml", brief=B["brief"], names=names_xml(B), seconds=f"{seconds:g}")
    first = first.rstrip() + "\n\n" + langrun_prompt("rest")
    step = STAGE.get(len(chain), len(chain)) if args.staged else len(chain)
    k = step
    if args.staged:
        first += "\n\n" + own("staged_author", k=k, chain_now=chain_list(chain[:k]), chain_later=chain_list(chain[k:], k + 1))
    (out / "author_prompt.md").write_text(first)

    message, good, good_state, n = [text(first)], None, None, 0
    while True:
        sub = chain[:k]
        current = None
        for attempt in range(MAX_LOAD_RETRIES + 1):  # a file that loads
            n += 1
            r = send(chat, message, f"t{n}_write")
            j = judge("xml", sub, r.text, f"t{n}", out, seconds)
            if j is None:
                j = {"loaded": False, "problem": "I could not find a ```xml block in your reply.", "passed": False}
            rec["turns"].append({"turn": f"t{n}", "kind": "write", "links": k, "problem": j.get("problem")})
            if not j.get("problem"):
                current = j
                break
            message = [text(langrun_prompt("load_problem_xml", problem=j["problem"]))]
        if current is None:
            break
        xml = (out / f"t{n}.xml").read_text()
        state = full_state(xml)
        rounds, fresh = 0, args.staged and good_state is not None  # fresh: this stage's first file, which adds links rather than revising
        while True:
            held_sub = [bool(current["test"]["checks"][x]) for x in sub]
            if good_state is not None:  # frozen links: a staged file may not break what an earlier stage made hold
                frozen = first_break(good_state["held"][:k - step]) if args.staged else 0
                lost = [i for i in range(frozen) if not state["held"][i]]
                before, after = min(good_state["first"], k), min(state["first"], k)  # only the links asked for so far
                rec["revisions"].append({"turn": f"t{n}", "before_first": before, "after_first": after,
                                         "lost": [i for i in range(before) if not state["held"][i]], "links": k,
                                         "new_stage": fresh})
                fresh = False
                if args.staged and lost:
                    rounds += 1
                    if rounds > MAX_ROUNDS:
                        break
                    message = [text(own("staged_refused", lost=lost[0] + 1, done=k - step,
                                        evidence=state["evidence"][lost[0]]))]
                    n += 1
                    r = send(chat, message, f"t{n}_write")
                    j = judge("xml", sub, r.text, f"t{n}", out, seconds)
                    rec["turns"].append({"turn": f"t{n}", "kind": "refused", "links": k})
                    if j and not j.get("problem"):
                        current, xml = j, (out / f"t{n}.xml").read_text()
                        state = full_state(xml)
                    continue
            good, good_state = xml, state
            if all(held_sub):
                break
            rounds += 1
            if rounds > MAX_ROUNDS:
                break
            h = settle.say(current.get("settle")) + words.see(current["run"], "your", seconds)
            if args.debugger:
                h = own("builder_sees", history=h, report=report_for(xml, sub, f"t{n}"))
            parts = [text(h), text(langrun_prompt("see_task_xml", verb="happens in the run"))]
            (out / f"t{n}_round_prompt.md").write_text("\n\n".join(p["text"] for p in parts))
            n += 1
            r = send(chat, parts, f"t{n}_round")
            v = parse_verdict(r.text)
            j = judge("xml", sub, r.text, f"t{n}", out, seconds)
            rec["turns"].append({"turn": f"t{n}", "kind": "round", "links": k, "verdict": v, "sent_file": j is not None})
            if j is None or j.get("problem"):
                if j is None and v.get("works_bool"):
                    break
                continue
            current, xml = j, (out / f"t{n}.xml").read_text()
            state = full_state(xml)
        if not args.staged or k >= len(chain) or not all(good_state["held"][:k]):
            break
        k = min(k + step, len(chain))
        message = [text(own("staged_next", done=k - step, n=k - (k - step), chain_now=chain_list(chain[k - step:k], k - step + 1)))]

    final = full_state(good) if good else None
    rec |= {"final_held": final["held"] if final else None, "final_first": final["first"] if final else 0,
            "passes_final": bool(final and final["first"] == len(chain)), "steps_held": sum(final["held"]) if final else 0,
            "seconds": round(time.monotonic() - t0, 1),
            "tokens": {"input": sum(c.input_tokens for c in calls), "output": sum(c.output_tokens for c in calls)},
            "cost_usd": round(sum(c.cost_usd for c in calls), 6)}
    (out / "world.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")
    revs = rec["revisions"]
    revs = [r for r in revs if not r["new_stage"]]
    clean = sum(r["after_first"] > r["before_first"] and not r["lost"] for r in revs)
    print(f"{wid}: works={rec['passes_final']} held={rec['steps_held']}/{len(chain)} clean revisions {clean}/{len(revs)} "
          f"${rec['cost_usd']:.4f} {rec['seconds']}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
