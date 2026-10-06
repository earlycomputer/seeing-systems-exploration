"""Experiment 1e, one world: one of 1d's broken worlds, checked and fixed with the run's history in words.

    python -m history.run --model opus-5.5 --brief catapult --seed 0
    python -m history.run --model dry-run --brief door            # plumbing test, no calls

1d's loop for a broken world (harder/run.py), with only the readback changed. The model gets the brief, the naming
conventions and the broken file, presented as a scene to check, with the first round's readback. Then up to three
see-and-fix rounds; the loop stops when the model is satisfied or the rounds run out. The readback is the history
of the run in words (history/narrate.py) where 1d sent a picture or nothing. 1d's tests judge every file; the
model never sees them. Everything goes to history/results/runs/<world>/<timestamp>/ in 1d's layout.
"""

from __future__ import annotations

import argparse
import json
import sys
import time

from config import ROOT
from loop.models import MODELS, extract_block, open_chat, text
from harder import tests
from harder.breaks import broken
from harder.run import SYSTEM, judge_file, parse_verdict, prompt
from harder.settings import BRIEFS as BRIEFS_1D, FIXTURES_1C, MAX_LOAD_RETRIES, MAX_ROUNDS, SIM_SECONDS
from history import budget
from history.narrate import history
from history.settings import ARM, BRIEFS, DRYRUN_DIR, PROMPTS, RUNS_DIR, SPEND_LEDGER


def world_id(model: str, brief: str, seed: int) -> str:
    return f"{model}__{brief}__{ARM}__s{seed}"


def see_history(run, whose: str) -> str:
    s = (PROMPTS / "see_history.md").read_text()
    return s.replace("{whose}", whose).replace("{seconds}", f"{SIM_SECONDS:g}").replace("{history}", history(run))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(MODELS))
    ap.add_argument("--brief", required=True, choices=BRIEFS)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--effort", default="high")
    args = ap.parse_args(argv)

    spec = MODELS[args.model]
    dry = spec.provider == "dry"
    wid = world_id(args.model, args.brief, args.seed)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    out = (DRYRUN_DIR / "runs" if dry else RUNS_DIR) / wid / stamp
    out.mkdir(parents=True, exist_ok=True)
    B = BRIEFS_1D[args.brief]
    test = B["test"]

    script = None
    if dry:  # "dry-run" sends the hand-written world; "dry-run-echo" changes nothing; both then say it works
        fixture = (FIXTURES_1C / f"{args.brief}.xml").read_text()
        ok = '```json\n{"what_happens": "dry run", "works": true, "problem": ""}\n```'
        fix = f'```json\n{{"what_happens": "dry run", "works": false, "problem": "dry run"}}\n```\n```xml\n{fixture}```'
        script = ([fix] if args.model == "dry-run" else []) + [ok] * (MAX_ROUNDS + MAX_LOAD_RETRIES)
    chat = open_chat(args.model, SYSTEM, args.effort, tag=f"1e/{wid}", script=script, ledger=SPEND_LEDGER)

    rec = {"world": wid, "run_dir": str(out.relative_to(ROOT)), "started_at": stamp, "experiment": "1e",
           "model": args.model, "model_label": spec.label, "model_id": spec.model_id, "effort": args.effort,
           "brief": args.brief, "brief_text": B["brief"], "kind": "broken", "test": test, "arm": ARM,
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

    given = broken(args.brief)
    current = judge_file(test, given, "given", out)
    rec["files"].append(tests.public({**current, "turn": "given"}) | {"run": None})
    lead = [text(prompt("given", brief=B["brief"], names=B["names"], seconds=f"{SIM_SECONDS:g}", scene=given.strip()))]
    rec["load_attempts"] = 0
    rec["loads"] = not current.get("problem")
    rec["passes_first"] = bool(current.get("passed"))
    passed_at = 0 if rec["passes_first"] else None

    rounds, edited = 0, False
    if rec["loads"]:
        for rnd in range(1, MAX_ROUNDS + 1):
            rounds = rnd
            whose = "your" if edited else "the"
            if current.get("problem"):
                parts, verb = [text(prompt("load_problem", problem=current["problem"]))], None
            else:
                h = see_history(current["run"], whose)
                (out / f"round{rnd}_history.md").write_text(h)
                parts, verb = [text(h)], "happens in the run"
            if verb:
                parts = parts + [text(prompt("see_task", verb=verb))]
            parts = lead + parts
            lead = []
            (out / f"round{rnd}_prompt.md").write_text("\n\n".join(p["text"] for p in parts))
            r = send(parts, f"round{rnd}")
            v = parse_verdict(r.text) if verb else {}
            xml = extract_block(r.text, "xml")
            turn = {"turn": f"round{rnd}", "verdict": v, "usage": r.summary(),
                    "current_passed": bool(current.get("passed")), "sent_file": xml is not None}
            if xml is not None:
                edited = True
                current = judge_file(test, xml, f"round{rnd}", out)
                rec["files"].append(tests.public({**current, "turn": f"round{rnd}"}) | {"run": None})
                turn["new_file_passed"] = bool(current.get("passed"))
                if current.get("passed") and passed_at is None:
                    passed_at = rnd
            rec["turns"].append(turn)
            if xml is None and v.get("works_bool") is True:
                break  # the model is satisfied
    last_verdict = next((t["verdict"] for t in reversed(rec["turns"]) if t.get("verdict")), {})
    rec["rounds"] = rounds
    rec["passes_final"] = bool(current.get("passed"))
    rec["passed_at_round"] = passed_at
    rec["tried_fix"] = any(t.get("sent_file") for t in rec["turns"])
    rec["claims_works"] = last_verdict.get("works_bool")
    rec["claim_correct"] = None if rec["claims_works"] is None else rec["claims_works"] == rec["passes_final"]
    rec["final_checks"] = current.get("checks")
    rec["seconds"] = round(time.monotonic() - t0, 1)
    rec["tokens"] = {"input": sum(c.input_tokens for c in calls), "output": sum(c.output_tokens for c in calls)}
    rec["tokens"]["total"] = rec["tokens"]["input"] + rec["tokens"]["output"]
    rec["cost_usd"] = round(sum(c.cost_usd for c in calls), 6)
    rec["served_models"] = sorted({c.served_model for c in calls})
    rec["finished_at"] = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    (out / "world.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")
    print(f"{wid}: first={rec['passes_first']} final={rec['passes_final']} rounds={rounds} "
          f"claims={rec['claims_works']} ${rec['cost_usd']:.4f} {rec['seconds']}s -> {rec['run_dir']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
