"""1m's first paid test: the debugger agent on the cases where 1j's builders were stuck.

    python -m debug.stuck --model dry-run      # plumbing, no calls
    python -m debug.stuck --model gpt-6.1      # the test (ceiling $15, CEILING_1M_USD in debug/run.py)
    python -m debug.stuck --report             # debug/results/stuck/stuck.md from stuck.json

Jono chose "Debugger test only" (2026-10-09 18:20). The cases: every 1j XML-with-words revision where the builder had
read the run in words and its next file did NOT move the first break forward without losing a link (debug/bench.py).
Revisions answering a load refusal (written0 -> written1) are left out: that builder never saw a run.

For each case, two fresh one-turn builders (GPT-6.1, high effort) get the brief, their stuck file, the run in words
and 1j's see-task:
- control: just that (a fresh draw, since picking failures guarantees the original builders scored 0);
- debugger: the same plus the debugger agent's report (debug/agent.py, GPT-6.1, up to 3 question turns).
Each reply's file is judged on the whole chain. Clean = the first break moves forward and no link that held is lost.
Pairs run case by case, so a ceiling stop leaves matched pairs.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from debug import agent as debugger
from debug.run import LEDGER, CEILING_1M_USD, check_budget, own
from debug.tools import Session, compare, judge_chain
from harder.run import parse_verdict
from hundred import settle, words
from hundred.briefs import names_xml
from hundred.run import judge_xml
from langrun.run import prompt as langrun_prompt
from ladder import briefs as ladder_briefs
from loop.models import MODELS, extract_block, open_chat, spent_usd, text
from why.errors import build

HERE = Path(__file__).parent
OUT = HERE / "results" / "stuck"
BENCH = HERE / "results" / "bench.json"
SYSTEM = "You build MuJoCo scenes that do what their briefs say, and you check them honestly."
RESERVE_USD = 1.5  # stop a pair early rather than cross the ceiling mid-pair


def cases() -> list[dict]:
    rows = [r for r in json.loads(BENCH.read_text()) if "skipped" not in r]
    return [r for r in rows if r["arm"] == "xml" and not r["builder_clean"] and r["next"].startswith("round")]


def builder_prompt(B: dict, xml: str, h: str, report: str | None) -> str:
    seconds = B["seconds"]
    p = langrun_prompt("author_xml", brief=B["brief"], names=names_xml(B), seconds=f"{seconds:g}")
    p = p.rstrip() + "\n\n" + langrun_prompt("rest")
    p += f"\n\nYou wrote this file:\n\n```xml\n{xml.rstrip()}\n```\n\n"
    p += own("builder_sees", history=h, report=report) if report else h
    return p + "\n\n" + langrun_prompt("see_task_xml", verb="happens in the run")


def judge_reply(reply: str, chain: list[str], seconds: float, before: dict) -> dict:
    xml = extract_block(reply, "xml")
    if xml is None:
        return {"sent_file": False, "clean": False, "moved": 0, "lost": []}
    w = build(xml, "xml", None, seconds)
    if w.run is None:
        return {"sent_file": True, "builds": False, "clean": False, "moved": 0, "lost": []}
    after = judge_chain(w, chain)
    return {"sent_file": True, "builds": True, "first": after["first"], "held": after["held"],
            **compare(before, after, chain)}


def main() -> int:
    if "--report" in sys.argv:
        return report()
    model = sys.argv[sys.argv.index("--model") + 1]
    dry = MODELS[model].provider == "dry"
    out_root = (HERE.parent / ".dryrun" / "debug" / "stuck") if dry else OUT
    out_root.mkdir(parents=True, exist_ok=True)
    out_file = out_root / "stuck.json"
    done = json.loads(out_file.read_text()) if out_file.exists() else []
    seen = {(d["world"], d["label"]) for d in done}
    briefs = ladder_briefs.load()
    dirs = {r["world"]: Path(r["dir"]) if Path(r["dir"]).is_absolute() else HERE.parent / r["dir"]
            for r in json.loads((HERE.parent / "ladder" / "results_breaks" / "breaks.json").read_text())}
    for c in cases():
        if (c["world"], c["label"]) in seen:
            continue
        if not dry and spent_usd(LEDGER) + RESERVE_USD >= CEILING_1M_USD:
            print(f"stopping: 1m has spent ${spent_usd(LEDGER):.2f} of ${CEILING_1M_USD:.0f}")
            break
        B = briefs[c["world"].split("__")[1]]
        chain, seconds = B["test"], B["seconds"]
        src_dir = dirs[c["world"]]
        xml = (src_dir / f"{c['label']}.xml").read_text()
        j = judge_xml("xml", chain, xml, seconds)
        before = judge_chain(build(xml, "xml", None, seconds), chain)
        h = settle.say(j.get("settle")) + words.see(j["run"], "your", seconds)
        case_dir = out_root / f"{c['world']}__{c['label']}"
        case_dir.mkdir(parents=True, exist_ok=True)
        row = {"world": c["world"], "label": c["label"], "steps": c["steps"], "first": before["first"],
               "link": chain[before["first"]] if before["first"] < len(chain) else None}
        t0 = time.monotonic()
        ok = '```json\n{"what_happens": "dry", "works": false, "problem": "dry"}\n```\n\n```xml\n' + xml + "```"
        for arm in ("control", "debugger"):
            report_text, cost = None, 0.0
            if arm == "debugger":
                dchat = open_chat(model, debugger.SYSTEM, "high", tag=f"1m/stuck/{c['world']}/debugger",
                                  script=["```ask\nstatus\nwhy %d\n```" % (before["first"] + 1), "```report\ndry\n```"] * 5
                                  if dry else None, ledger=None if dry else LEDGER)
                s = Session(xml, "xml", chain, seconds)
                try:
                    report_text, replies = debugger.debug(s, B["brief"], dchat, case_dir, "debugger")
                except RuntimeError as e:  # OpenAI sometimes flags a prompt; the case is recorded as lost, not retried
                    row["debugger_error"] = str(e)[:300]
                    print(c["world"], c["label"], "debugger failed:", str(e)[:120], flush=True)
                    break
                cost += sum(r.cost_usd for r in replies)
                row["debugger_turns"] = len(replies)
                row["debugger_tokens"] = sum(r.input_tokens + r.output_tokens for r in replies)
            p = builder_prompt(B, xml, h, report_text)
            (case_dir / f"{arm}_prompt.md").write_text(p)
            if not dry:
                check_budget()
            chat = open_chat(model, SYSTEM, "high", tag=f"1m/stuck/{c['world']}/{arm}", script=[ok] if dry else None,
                             ledger=None if dry else LEDGER)
            r = chat.send([text(p)])
            (case_dir / f"{arm}_reply.md").write_text(r.text)
            res = judge_reply(r.text, chain, seconds, before)
            res["claims_works"] = parse_verdict(r.text).get("works_bool")
            res["cost_usd"] = round(cost + r.cost_usd, 4)
            res["builder_tokens"] = r.input_tokens + r.output_tokens
            row[arm] = res
        row["seconds"] = round(time.monotonic() - t0, 1)
        done.append(row)
        if "debugger_error" in row:
            out_file.write_text(json.dumps(done, indent=1) + "\n")
            continue
        out_file.write_text(json.dumps(done, indent=1) + "\n")
        print(c["world"], c["label"], "control", row["control"]["clean"], "debugger", row["debugger"]["clean"],
              f"${row['control']['cost_usd'] + row['debugger']['cost_usd']:.2f}", flush=True)
    if not dry:
        return report()
    return 0


def report() -> int:
    rows = json.loads((OUT / "stuck.json").read_text())
    lost = [r for r in rows if "debugger_error" in r]
    rows = [r for r in rows if "debugger_error" not in r]
    n = len(rows)
    pct = lambda k, d: f"{k} of {d}" if d else "none"
    lines = ["# The debugger agent on stuck cases (1m, GPT-6.1)", "",
             "Generated by `python -m debug.stuck --report`; never edited by hand. Each case is a 1j XML-with-words file "
             "whose builder read the run in words and did not move the first break forward. Two fresh one-turn builders "
             "per case; one also reads the debugger agent's report. Clean = first break forward, no held link lost.", "",
             "| Builder | Cases | Clean | Moved forward (any) | Lost a held link | Sent no file or did not build | Said it works | Cost |",
             "|---|---|---|---|---|---|---|---|"]
    for arm in ("control", "debugger"):
        g = [r[arm] for r in rows]
        lines.append(f"| {arm} | {n} | {pct(sum(x['clean'] for x in g), n)} | {pct(sum(x.get('moved', 0) > 0 for x in g), n)} "
                     f"| {pct(sum(bool(x.get('lost')) for x in g), n)} "
                     f"| {pct(sum((not x['sent_file']) or x.get('builds') is False for x in g), n)} "
                     f"| {pct(sum(bool(x.get('claims_works')) for x in g), n)} | ${sum(x['cost_usd'] for x in g):.2f} |")
    both = sum(r["control"]["clean"] and r["debugger"]["clean"] for r in rows)
    only_d = sum(r["debugger"]["clean"] and not r["control"]["clean"] for r in rows)
    only_c = sum(r["control"]["clean"] and not r["debugger"]["clean"] for r in rows)
    lines += ["", f"{len(lost)} cases left out because the model provider refused the debugger's prompt: "
              + ", ".join(f"{r['world'].split('__')[1]} s{r['world'][-1]} {r['label']}" for r in lost) + "."] if lost else []
    lines += ["", f"Paired: both clean {both}, only with the debugger {only_d}, only without {only_c}, neither "
              f"{n - both - only_d - only_c}.", ""]
    lines += ["| Case | First break | Control | Debugger |", "|---|---|---|---|"]
    word = lambda x: "clean" if x["clean"] else (f"moved {x['moved']:+d}, lost {len(x['lost'])}" if x.get("builds") else
                                                 ("no file" if not x["sent_file"] else "did not build"))
    for r in rows:
        lines.append(f"| {r['world'].split('__')[1]} s{r['world'][-1]} {r['label']} | {r['first'] + 1}: {r['link']} "
                     f"| {word(r['control'])} | {word(r['debugger'])} |")
    (OUT / "stuck.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
