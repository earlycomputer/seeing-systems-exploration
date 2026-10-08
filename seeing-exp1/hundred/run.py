"""Experiment 1h, one world: a model writes a world from a fresh brief, then checks or fixes it over up to three rounds.

    python -m hundred.run --model opus-5.5 --brief <id> --arm language --seed 0
    python -m hundred.run --model dry-run --brief chain --arm xml --dry-briefs      # plumbing test, no calls

1g's checked loop (langrun/run.py) with three arms (hundred/settings.py). The hidden test (hidden.py) judges the
built MJCF; the model never sees it. The blind arm hears MuJoCo's load errors, as anyone would, and nothing about the
run. No arm is asked for expectations: 1g found that asking cost first attempts (115 against 134 of 160, p = 0.015)
and checking them didn't help (149 against 156), so every arm gets 1g control's rest line instead.
"""

from __future__ import annotations

import argparse
import json
import sys
import time

from config import ROOT
from harder.run import parse_verdict
from history.run import see_history
from langrun import expect, lint
from langrun.run import prompt as langrun_prompt
from langrun.settings import FIXTURES as LANGRUN_FIXTURES, PROMPTS as LANGRUN_PROMPTS
from loop.models import MODELS, extract_block, open_chat, text
from typed.compiler import render
from typed.lang import LIBRARY, compile_program, parse
from worlds.tests import run as run_world
from hundred import briefs as briefs_mod, budget, hidden, settle
from hundred.settings import (ARMS, BRIEFS_FILE, DRY_BRIEFS_FILE, DRYRUN_DIR, MAX_LOAD_RETRIES, MAX_ROUNDS, PROMPTS,
                              RUNS_DIR, SIM_SECONDS, SPEND_LEDGER)

SYSTEM = {"blind": "You build MuJoCo scenes that do what their briefs say, and you check them honestly.",
          "xml": "You build MuJoCo scenes that do what their briefs say, and you check them honestly.",
          "language": "You build worlds in the world language that do what their briefs say, and you check them honestly."}
FORMAT = {"blind": "xml", "xml": "xml", "language": "world"}


def world_id(model: str, brief: str, arm: str, seed: int) -> str:
    return f"{model}__{brief}__{arm}__s{seed}"


def own(name: str, **kw) -> str:
    s = (PROMPTS / f"{name}.md").read_text()
    for k, v in kw.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def judge_xml(arm: str, test: list[str], xml: str) -> dict:
    try:
        problem = None if arm == "blind" else lint.report(xml)
        if arm == "blind":
            run_world(xml, seconds=0.0)  # loads it, so MuJoCo's own load errors come back as they would to anyone
    except Exception as e:
        return {"loaded": False, "problem": f"MuJoCo could not load the file: {e}"}
    if problem:
        return {"loaded": True, "problem": problem, "lint": True}
    r = run_world(xml, seconds=SIM_SECONDS)
    return {"loaded": True, "problem": None, "run": r, "diverged": r.diverged, "test": hidden.judge(test, r),
            "settle": [] if arm == "blind" else settle.problems(xml)}


def judge(arm: str, test: list[str], reply: str, label: str, out) -> dict | None:
    if FORMAT[arm] == "xml":
        xml = extract_block(reply, "xml")
        if xml is None:
            return None
        (out / f"{label}.xml").write_text(xml)
        j = judge_xml(arm, test, xml)
        block = extract_block(reply, "expect")
        j["expect"] = expect.block(block) if block is not None else None
        j["chars"] = len(xml)
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
        try:
            c = compile_program(parse(world, library))
        except Exception as e:
            j = {"loaded": False, "problem": f"The world could not be read: {type(e).__name__}: {e}", "crash": True}
        else:
            if c.problems:
                j = {"loaded": False, "problem": render(c.problems)}
            else:
                (out / f"{label}.compiled.xml").write_text(c.xml)
                j = judge_xml(arm, test, c.xml)
                j["owner"] = c.owner
        j["expect"] = expect.section(world)
        j["chars"] = len(world) + len(parts or "")
    j["label"] = label
    j["passed"] = bool(j.get("test", {}).get("passed"))
    return j


def dry_script(model: str, brief: str, arm: str) -> list[str]:
    ok = '```json\n{"what_happens": "dry run", "works": true, "problem": ""}\n```'
    if FORMAT[arm] == "xml":
        good = f"```xml\n{(LANGRUN_FIXTURES / f'{brief}.xml').read_text()}```\n\n```expect\nball touches floor\n```"
    else:
        good = f"```world\n{(LANGRUN_FIXTURES / f'{brief}.world').read_text()}```"
    empty = "```xml\n<mujoco/>\n```" if FORMAT[arm] == "xml" else "```world\nworld  empty\n\nfloor\n```"
    return [good if model == "dry-run" else empty] + [ok] * (MAX_ROUNDS + MAX_LOAD_RETRIES)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(MODELS))
    ap.add_argument("--brief", required=True)
    ap.add_argument("--arm", required=True, choices=ARMS)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--effort", default="high")
    ap.add_argument("--dry-briefs", action="store_true", help="1f's ledge and chain, for plumbing tests")
    ap.add_argument("--full", action="store_true", help="past the pilot: 1h's own ceiling, not the pilot's")
    args = ap.parse_args(argv)

    spec = MODELS[args.model]
    dry = spec.provider == "dry"
    B = briefs_mod.load(DRY_BRIEFS_FILE if args.dry_briefs else BRIEFS_FILE)[args.brief]
    arm, test = args.arm, B["test"]
    wid = world_id(args.model, args.brief, arm, args.seed)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    out = (DRYRUN_DIR / "runs" if dry else RUNS_DIR) / wid / stamp
    out.mkdir(parents=True, exist_ok=True)
    script = dry_script(args.model, args.brief, arm) if dry else None
    chat = open_chat(args.model, SYSTEM[arm], args.effort, tag=f"1h/{wid}", script=script,
                     ledger=None if dry else SPEND_LEDGER)

    rec = {"world": wid, "run_dir": str(out.relative_to(ROOT)) if not dry else str(out), "started_at": stamp,
           "experiment": "1h", "model": args.model, "model_label": spec.label, "model_id": spec.model_id,
           "effort": args.effort, "brief": args.brief, "brief_text": B["brief"], "test": test, "arm": arm,
           "seed": args.seed, "dry_run": dry, "turns": [], "files": []}
    calls, t0 = [], time.monotonic()

    def send(parts, name):
        if not dry:
            budget.check(pilot=not args.full)
        r = chat.send(parts)
        calls.append(r)
        (out / f"{name}_reply.md").write_text(r.text + ("\n\n---\nthinking (summarized):\n\n" + r.thinking
                                                        if r.thinking else ""))
        (out / f"{name}_raw.json").write_text(json.dumps(r.raw, indent=2, default=str) + "\n")
        return r

    expect_lines: list[str] = []

    def record_file(j, turn):
        nonlocal expect_lines
        if j.get("expect") is not None:
            expect_lines = j["expect"]
        if j.get("run") is not None:
            j["expect_results"] = expect.check(expect_lines, j["run"], j.get("owner"))
        rec["files"].append({k: v for k, v in j.items() if k not in ("run", "owner")} | {"turn": turn})

    if FORMAT[arm] == "xml":
        first = langrun_prompt("author_xml", brief=B["brief"], names=briefs_mod.names_xml(B), seconds=f"{SIM_SECONDS:g}")
        first = first.rstrip() + "\n\n" + langrun_prompt("rest")
    else:
        guide = langrun_prompt("guide", library=LIBRARY.read_text().strip())
        first = langrun_prompt("author_language", brief=B["brief"], names=briefs_mod.names_language(B),
                               seconds=f"{SIM_SECONDS:g}", guide=guide.strip(),
                               example=(LANGRUN_PROMPTS / "example.world").read_text().strip())
        first = first.rstrip() + "\n\n" + langrun_prompt("rest")
    (out / "author_prompt.md").write_text(first)
    load_problem = "load_problem_xml" if FORMAT[arm] == "xml" else "load_problem_language"
    see_task = "see_task_xml" if FORMAT[arm] == "xml" else "see_task_language"

    message, current = [text(first)], None
    for attempt in range(MAX_LOAD_RETRIES + 1):
        r = send(message, f"write{attempt}")
        j = judge(arm, test, r.text, f"written{attempt}", out)
        if j is None:
            j = {"loaded": False, "label": f"written{attempt}", "passed": False,
                 "problem": f"I could not find a ```{FORMAT[arm]} block in your reply."}
        record_file(j, f"write{attempt}")
        rec["turns"].append({"turn": f"write{attempt}", "usage": r.summary(), "problem": j.get("problem")})
        current = j
        if not j.get("problem"):
            break
        message = [text(langrun_prompt(load_problem, problem=j["problem"]))]
    rec["load_attempts"] = len(rec["turns"])
    rec["loads"] = not current.get("problem")
    rec["passes_first"] = bool(current.get("passed"))
    rec["first_expect"] = current.get("expect_results")
    passed_at = 0 if rec["passes_first"] else None

    rounds = 0
    if rec["loads"]:
        for rnd in range(1, MAX_ROUNDS + 1):
            rounds = rnd
            if current.get("problem"):
                parts, verb = [text(langrun_prompt(load_problem, problem=current["problem"]))], None
            else:
                if arm == "blind":
                    h, verb_words = own("see_blind"), "will happen when it runs"
                else:
                    h = settle.say(current.get("settle")) + see_history(current["run"], "your")
                    verb_words = "happens in the run"
                (out / f"round{rnd}_history.md").write_text(h)
                parts = [text(h), text(langrun_prompt(see_task, verb=verb_words))]
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
                break
    last_verdict = next((t["verdict"] for t in reversed(rec["turns"]) if t.get("verdict")), {})
    final_file = next((f for f in reversed(rec["files"]) if f.get("loaded") is not None), {})
    rec["rounds"] = rounds
    rec["passes_final"] = bool(current.get("passed"))
    rec["passed_at_round"] = passed_at
    rec["claims_works"] = last_verdict.get("works_bool")
    rec["claim_correct"] = None if rec["claims_works"] is None else rec["claims_works"] == rec["passes_final"]
    rec["final_test"] = current.get("test")
    rec["final_problem"] = current.get("problem")
    rec["final_expect"] = current.get("expect_results")
    rec["final_label"] = current.get("label")
    rec["final_chars"] = final_file.get("chars")
    rec["seconds"] = round(time.monotonic() - t0, 1)
    rec["tokens"] = {"input": sum(c.input_tokens for c in calls), "output": sum(c.output_tokens for c in calls)}
    rec["tokens"]["total"] = rec["tokens"]["input"] + rec["tokens"]["output"]
    rec["cost_usd"] = round(sum(c.cost_usd for c in calls), 6)
    rec["served_models"] = sorted({c.served_model for c in calls})
    rec["finished_at"] = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    (out / "world.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")
    print(f"{wid}: loads={rec['loads']} first={rec['passes_first']} final={rec['passes_final']} rounds={rounds} "
          f"claims={rec['claims_works']} ${rec['cost_usd']:.4f} {rec['seconds']}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
