"""Experiment 1f, one world: a model writes a world from a brief, in the world language or in MJCF, then fixes it.

    python -m langrun.run --model opus-5.5 --brief seesaw --arm language --seed 0
    python -m langrun.run --model dry-run --brief catapult --arm xml           # plumbing test, no calls
    python -m langrun.run --model opus-5.5 --brief seesaw --arm xml --checked   # experiment 1g

1d's loop for a new brief (harder/run.py): write the world (up to two retries while it will not build), then up to
three see-and-fix rounds, stopping when the model is satisfied or the rounds run out. What differs by arm is only the
format and its help (langrun/settings.py). Both arms see the run's history in words each round. The tests judge the
compiled MJCF; the model never sees them. Everything goes to langrun/results/runs/<world>/<timestamp>/.

With --checked (experiment 1g) each world also says what should happen, and each round's readback opens with those
expectations checked against the run (langrun/expect.py); runs go to langrun/results_1g/runs/.
"""

from __future__ import annotations

import argparse
import json
import sys
import time

from config import ROOT
from loop.models import MODELS, extract_block, open_chat, text
from harder import tests as tests_1d
from harder.run import parse_verdict
from harder.settings import FIXTURES_1C, FIXTURES_DIR as FIXTURES_1D
from history import budget
from history.run import see_history
from typed.compiler import render
from typed.lang import LIBRARY, compile_program, parse
from worlds.tests import MissingName, run as run_world
from langrun import expect, heldout, lint
from langrun.settings import (ARMS, BRIEFS, CHECKED_DRYRUN_DIR, CHECKED_RUNS_DIR, CHECKED_SPEND_LEDGER, CONTROL_DRYRUN_DIR,
                              CONTROL_RUNS_DIR, DRYRUN_DIR, FIXTURES,
                              LANGUAGE_NAMES, MAX_LOAD_RETRIES, MAX_ROUNDS, PROMPTS, RUNS_DIR, SIM_SECONDS, SPEND_LEDGER)

SYSTEM = {"xml": "You build MuJoCo scenes that do what their briefs say, and you check them honestly.",
          "language": "You build worlds in the world language that do what their briefs say, and you check them honestly."}
TESTS = dict(tests_1d.TESTS, **heldout.TESTS)
TYPED = ROOT / "typed" / "worlds"


def world_id(model: str, brief: str, arm: str, seed: int) -> str:
    return f"{model}__{brief}__{arm}__s{seed}"


def prompt(name: str, **kw) -> str:
    s = (PROMPTS / f"{name}.md").read_text()
    for k, v in kw.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def judge_xml(test: str, xml: str) -> dict:
    """Load, check as the language would, run and test: 1d's judge with the language's two after-parse checks."""
    try:
        problem = lint.report(xml)
    except Exception as e:  # MuJoCo raises ValueError with the parser's message
        return {"loaded": False, "problem": f"MuJoCo could not load the file: {e}"}
    if problem:
        return {"loaded": True, "problem": problem, "lint": True}
    r = run_world(xml)
    try:
        res = TESTS[test](r)
    except MissingName as e:
        return {"loaded": True, "problem": f"The scene is missing a name the brief needs: {e}.", "run": r}
    res.update(loaded=True, problem=None, diverged=r.diverged, run=r, load_log=r.loaded.log)
    if r.diverged:
        res["passed"] = False
    return res


def judge(arm: str, test: str, reply: str, label: str, out) -> dict | None:
    """The file in a reply, judged; None when the reply holds no file. `expect` holds the world's own expectations:
    a .world file's `expect` section, or an ```expect block sent beside the MJCF (None when the reply sent none)."""
    if arm == "xml":
        xml = extract_block(reply, "xml")
        if xml is None:
            return None
        (out / f"{label}.xml").write_text(xml)
        j = judge_xml(test, xml)
        block = extract_block(reply, "expect")
        j["expect"] = expect.block(block) if block is not None else None
    else:
        world = extract_block(reply, "world")
        if world is None:
            return None
        parts = extract_block(reply, "parts")
        (out / f"{label}.world").write_text(world)
        library = LIBRARY.read_text()
        if parts:
            (out / f"{label}.parts").write_text(parts)
            library = library.rstrip() + "\n\n\n" + parts
        j_expect = expect.section(world)
        try:
            c = compile_program(parse(world, library))
        except Exception as e:  # the parser itself fell over: say so plainly, as a problem the model can act on
            j = {"loaded": False, "problem": f"The world could not be read: {type(e).__name__}: {e}", "crash": True}
        else:
            if c.problems:
                j = {"loaded": False, "problem": render(c.problems)}
            else:
                (out / f"{label}.xml").write_text(c.xml)
                j = judge_xml(test, c.xml)
                j["owner"] = c.owner
        j["expect"] = j_expect
    j["label"] = label
    return j


def dry_script(model: str, brief: str, arm: str) -> list[str]:
    ok = '```json\n{"what_happens": "dry run", "works": true, "problem": ""}\n```'
    if arm == "xml":
        src = next(p for p in (FIXTURES / f"{brief}.xml", FIXTURES_1D / f"{brief}.xml", FIXTURES_1C / f"{brief}.xml") if p.exists())
        good = f"```xml\n{src.read_text()}```\n\n```expect\nball touches floor\n```"
    else:
        src = next(p for p in (FIXTURES / f"{brief}.world", TYPED / f"{brief}.world") if p.exists())
        good = f"```world\n{src.read_text()}```"
    empty = "```xml\n<mujoco/>\n```" if arm == "xml" else "```world\nworld  empty\n\nfloor\n```"
    return [good if model == "dry-run" else empty] + [ok] * (MAX_ROUNDS + MAX_LOAD_RETRIES)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(MODELS))
    ap.add_argument("--brief", required=True, choices=list(BRIEFS))
    ap.add_argument("--arm", required=True, choices=ARMS)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--effort", default="high")
    ap.add_argument("--checked", action="store_true", help="experiment 1g: expectations checked against each run")
    ap.add_argument("--control", action="store_true", help="1g's control: the rest line, no expectations")
    args = ap.parse_args(argv)
    if args.checked and args.control:
        ap.error("--checked and --control are different conditions")

    spec = MODELS[args.model]
    dry = spec.provider == "dry"
    wid = world_id(args.model, args.brief, args.arm, args.seed)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    if args.checked:
        out = (CHECKED_DRYRUN_DIR / "runs" if dry else CHECKED_RUNS_DIR) / wid / stamp
    elif args.control:
        out = (CONTROL_DRYRUN_DIR / "runs" if dry else CONTROL_RUNS_DIR) / wid / stamp
    else:
        out = (DRYRUN_DIR / "runs" if dry else RUNS_DIR) / wid / stamp
    out.mkdir(parents=True, exist_ok=True)
    B, arm = BRIEFS[args.brief], args.arm
    test = args.brief
    script = dry_script(args.model, args.brief, arm) if dry else None
    exp = "1g" if args.checked else "1g-control" if args.control else "1f"
    chat = open_chat(args.model, SYSTEM[arm], args.effort, tag=f"{exp}/{wid}", script=script,
                     ledger=CHECKED_SPEND_LEDGER if args.checked or args.control else SPEND_LEDGER)

    rec = {"world": wid, "run_dir": str(out.relative_to(ROOT)), "started_at": stamp, "experiment": exp, "checked": args.checked, "control": args.control,
           "model": args.model, "model_label": spec.label, "model_id": spec.model_id, "effort": args.effort,
           "brief": args.brief, "brief_text": B["brief"], "set": B["set"], "kind": B["kind"], "test": test, "arm": arm,
           "seed": args.seed, "dry_run": dry, "turns": [], "files": []}
    calls, t0 = [], time.monotonic()

    def send(parts, name):
        if not dry:
            budget.check()
        r = chat.send(parts)
        calls.append(r)
        (out / f"{name}_reply.md").write_text(r.text + ("\n\n---\nthinking (summarized):\n\n" + r.thinking
                                                        if r.thinking else ""))
        (out / f"{name}_raw.json").write_text(json.dumps(r.raw, indent=2, default=str) + "\n")
        return r

    expect_lines: list[str] = []  # the world's latest expectations; an XML fix without a new block keeps the old ones

    def record_file(j, turn):
        nonlocal expect_lines
        if j.get("expect") is not None:
            expect_lines = j["expect"]
        if args.checked and j.get("run") is not None:
            j["expect_results"] = expect.check(expect_lines, j["run"], j.get("owner"))
        rec["files"].append({k: v for k, v in j.items() if k not in ("run", "owner")} | {"turn": turn})

    if arm == "xml":
        first = prompt("author_xml", brief=B["brief"], names=B["names"], seconds=f"{SIM_SECONDS:g}")
    else:
        guide = prompt("guide", library=LIBRARY.read_text().strip())
        first = prompt("author_language", brief=B["brief"], names=LANGUAGE_NAMES[args.brief], seconds=f"{SIM_SECONDS:g}",
                       guide=guide.strip(), example=(PROMPTS / "example.world").read_text().strip())
    if args.checked:
        first = first.rstrip() + "\n\n" + prompt(f"expect_{arm}")
    elif args.control:
        first = first.rstrip() + "\n\n" + prompt("rest")
    (out / "author_prompt.md").write_text(first)
    message, current = [text(first)], None
    for attempt in range(MAX_LOAD_RETRIES + 1):
        r = send(message, f"write{attempt}")
        j = judge(arm, test, r.text, f"written{attempt}", out)
        if j is None:
            j = {"loaded": False, "label": f"written{attempt}",
                 "problem": f"I could not find a ```{'xml' if arm == 'xml' else 'world'} block in your reply."}
        record_file(j, f"write{attempt}")
        rec["turns"].append({"turn": f"write{attempt}", "usage": r.summary(), "problem": j.get("problem")})
        current = j
        if not j.get("problem"):
            break
        message = [text(prompt(f"load_problem_{arm}", problem=j["problem"]))]
    rec["load_attempts"] = len(rec["turns"])
    rec["loads"] = not current.get("problem")
    rec["passes_first"] = bool(current.get("passed"))
    passed_at = 0 if rec["passes_first"] else None

    rounds = 0
    if rec["loads"]:
        for rnd in range(1, MAX_ROUNDS + 1):
            rounds = rnd
            if current.get("problem"):
                parts, verb = [text(prompt(f"load_problem_{arm}", problem=current["problem"]))], None
            else:
                h = see_history(current["run"], "your")
                if args.checked:
                    h = (expect.words(current.get("expect_results") or []) or
                         "You wrote no expectations, so none were checked.") + "\n\n" + h
                (out / f"round{rnd}_history.md").write_text(h)
                parts = [text(h), text(prompt(f"see_task_{arm}", verb="happens in the run"))]
                verb = True
            (out / f"round{rnd}_prompt.md").write_text("\n\n".join(p["text"] for p in parts))
            r = send(parts, f"round{rnd}")
            v = parse_verdict(r.text) if verb else {}
            j = judge(arm, test, r.text, f"round{rnd}", out)
            turn = {"turn": f"round{rnd}", "verdict": v, "usage": r.summary(),
                    "current_passed": bool(current.get("passed")), "sent_file": j is not None}
            if j is not None:
                current = j
                record_file(j, f"round{rnd}")
                turn["new_file_passed"] = bool(j.get("passed"))
                turn["problem"] = j.get("problem")
                if j.get("passed") and passed_at is None:
                    passed_at = rnd
            rec["turns"].append(turn)
            if j is None and v.get("works_bool") is True:
                break  # the model is satisfied
    last_verdict = next((t["verdict"] for t in reversed(rec["turns"]) if t.get("verdict")), {})
    rec["rounds"] = rounds
    rec["passes_final"] = bool(current.get("passed"))
    rec["passed_at_round"] = passed_at
    rec["claims_works"] = last_verdict.get("works_bool")
    rec["claim_correct"] = None if rec["claims_works"] is None else rec["claims_works"] == rec["passes_final"]
    rec["final_checks"] = current.get("checks")
    rec["final_problem"] = current.get("problem")
    if args.checked:
        ex = current.get("expect_results")
        rec["final_expect"] = ex
        rec["expect_all_hold"] = None if not ex else all(ok for _, ok, _ in ex)
    rec["problems_seen"] = sum(1 for f in rec["files"] if f.get("problem"))
    rec["seconds"] = round(time.monotonic() - t0, 1)
    rec["tokens"] = {"input": sum(c.input_tokens for c in calls), "output": sum(c.output_tokens for c in calls)}
    rec["tokens"]["total"] = rec["tokens"]["input"] + rec["tokens"]["output"]
    rec["cost_usd"] = round(sum(c.cost_usd for c in calls), 6)
    rec["served_models"] = sorted({c.served_model for c in calls})
    rec["finished_at"] = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    (out / "world.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")
    print(f"{wid}: loads={rec['loads']} first={rec['passes_first']} final={rec['passes_final']} rounds={rounds} "
          f"claims={rec['claims_works']} ${rec['cost_usd']:.4f} {rec['seconds']}s -> {rec['run_dir']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
