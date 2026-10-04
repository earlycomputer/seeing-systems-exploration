"""Experiment 1b, step 1: Opus adds the shot, and the harness settles the base shot and the misses.

    python -m outcome.author --model opus-5.5
    python -m outcome.author --model dry-run          # plumbing test; writes to .dryrun/outcome

1. Air is added to experiment 1's scene as two one-line edits (outcome/scene/aired.xml).
2. The model adds a `shot` keyframe that launches the ball from where it rests (shot_authored.xml, .json).
   A file that fails to load, lacks a one-line `shot` key, or changes anything else goes back to the model.
3. MuJoCo judges that shot as written: a natural first data point.
4. If it is not a clean make (made by its own path, not off the backboard), the launch speed is scaled,
   same direction, to the middle of the widest run of clean makes. That shot is the base (base.xml).
5. Each deliberate miss takes the first step in settings.MISSES that MuJoCo shows is clear-cut on the base.
   All of it is recorded in base.json.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import time

from loop.models import MODELS, extract_block, open_chat, text
from outcome import budget, shot
from outcome.settings import (AIRED_SCENE, BASE_RECORD, BASE_SCENE, DRYRUN_DIR, MISSES, OUTCOME_DIR, SHOT_KEY,
                              SHOT_SCENE, SOURCE_SCENE, SPEND_LEDGER)

SYSTEM = "You write MuJoCo MJCF scenes that load on the first try and that a person can read."
KEYFRAME_BLOCK = re.compile(r"[ \t]*<keyframe>.*?</keyframe>[ \t]*\n?", re.S)
COMMENT = re.compile(r"<!--.*?-->", re.S)


def other_changes(aired: str, authored: str) -> str:
    """The diff between the two files once the keyframe element and every XML comment are taken out; empty
    when nothing MuJoCo reads changed outside the keyframe. Comments are ignored because the correction
    prompt asks for one, and a model may put it just outside the keyframe element."""
    strip = lambda s: [ln.strip() for ln in KEYFRAME_BLOCK.sub("", COMMENT.sub("", s)).splitlines()  # noqa: E731
                       if ln.strip()]
    return "\n".join(difflib.unified_diff(strip(aired), strip(authored), "aired", "authored", lineterm="", n=0))


def check(aired: str, xml: str) -> str | None:
    """None if the file is acceptable, else the message that goes back to the model."""
    try:
        shot.load(xml)
    except Exception as e:  # MuJoCo raises ValueError with the parser's message
        return f"MuJoCo could not load the file:\n\n{e}"
    try:
        qvel = shot.shot_qvel(xml)
    except ValueError as e:
        return f"{e}. Write the key on a single line with a qvel attribute."
    if len(qvel) != 6:
        return f'The shot key\'s qvel has {len(qvel)} numbers; the ball\'s free joint needs 6.'
    diff = other_changes(aired, xml)
    if diff:
        return f"The file changes more than the keyframe:\n\n{diff}\n\nChange nothing else."
    return None


def settle_misses(base: str) -> dict:
    out = {}
    for miss, spec in MISSES.items():
        tried = []
        for step in spec["steps"]:
            bad, edit = shot.inject(base, miss, step)
            j = shot.judge(bad)
            ok = shot.clear_cut(j, miss)
            tried.append({"step": step, "clear_cut": ok, "edit": edit, "judged": shot.public(j)})
            if ok:
                break
        out[miss] = {"step": tried[-1]["step"] if tried[-1]["clear_cut"] else None, "tried": tried}
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default="opus-5.5", choices=sorted(MODELS))
    ap.add_argument("--effort", default="high")
    ap.add_argument("--retries", type=int, default=2)
    ap.add_argument("--force", action="store_true", help="overwrite an existing shot_authored.xml")
    args = ap.parse_args()

    dry = MODELS[args.model].provider == "dry"
    out_dir = DRYRUN_DIR / "scene" if dry else SHOT_SCENE.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    shot_path, base_path, record_path = (out_dir / p.name for p in (SHOT_SCENE, BASE_SCENE, BASE_RECORD))
    if shot_path.exists() and not args.force:
        print(f"{shot_path} exists and the matrix depends on it; pass --force to replace it", file=sys.stderr)
        return 1

    aired, air_edits = shot.add_air(SOURCE_SCENE.read_text())
    (out_dir / AIRED_SCENE.name).write_text(aired)
    brief = (OUTCOME_DIR / "scene" / "brief.txt").read_text().strip()
    prompt = (OUTCOME_DIR / "prompts" / "author_shot.md").read_text().replace("{brief}", brief).replace(
        "{scene}", aired)
    script = None
    if dry:
        key = f'  <keyframe>\n    <key name="{SHOT_KEY}" qvel="4.2 0 8.1 0 -15 0"/>\n  </keyframe>\n'
        script = ["Dry run.\n```xml\n" + aired.replace("</worldbody>\n", "</worldbody>\n\n" + key) + "```"]
    chat = open_chat(args.model, SYSTEM, args.effort, tag="1b-author", script=script, ledger=SPEND_LEDGER)

    log = {"model": args.model, "model_id": MODELS[args.model].model_id, "effort": args.effort, "brief": brief,
           "source_scene": str(SOURCE_SCENE.relative_to(OUTCOME_DIR.parent)), "air_edits": air_edits,
           "system": SYSTEM, "prompt": prompt, "attempts": [],
           "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    message, xml, problem = prompt, None, "no attempt"
    for _ in range(args.retries + 1):
        budget.check()
        reply = chat.send([text(message)])
        xml = extract_block(reply.text, "xml")
        problem = "I could not find a ```xml block in your reply." if xml is None else check(aired, xml)
        log["attempts"].append({"sent": message, "reply": reply.text, "thinking": reply.thinking,
                                "usage": reply.summary(), "problem": problem})
        if problem is None:
            break
        message = problem + "\n\nReply with the complete corrected file in one ```xml block."
    log["accepted"] = problem is None
    if xml is not None:
        shot_path.write_text(xml)
    if problem is not None:
        log["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        shot_path.with_suffix(".json").write_text(json.dumps(log, indent=2) + "\n")
        print("FAILED: no attempt was acceptable. See", shot_path.with_suffix(".json"))
        return 2

    # The model's own shot, as written: a natural first data point.
    judged = shot.judge(xml)
    log["as_written"] = shot.public(judged)
    log["as_written"]["clean_make"] = shot.clean_make(judged)
    log["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    shot_path.with_suffix(".json").write_text(json.dumps(log, indent=2) + "\n")
    print(f"as written: {judged['outcome']} (clean make: {shot.clean_make(judged)}), "
          f"{judged['launch_speed']} m/s at {judged['launch_elevation_deg']} deg, apex {judged['apex_z']} m")

    record = {"from": shot_path.name, "as_written": log["as_written"], "made_by": "model as written"}
    base = xml
    if not shot.clean_make(judged):
        factor, runs = shot.tune_speed(xml)
        record.update(tuned_factor=factor, clean_make_runs=runs)
        if factor is None:
            record_path.write_text(json.dumps(record, indent=2) + "\n")
            print("FAILED: no launch speed in this direction makes the shot cleanly; a human decides next")
            return 3
        base, edit = shot.set_qvel(xml, shot.scaled(shot.shot_qvel(xml), factor))
        record.update(made_by=f"harness: launch speed x{factor}, same direction", tune_edit=edit)
    base_path.write_text(base)
    record["base"] = shot.public(shot.judge(base))
    record["misses"] = settle_misses(base)
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    print(f"base: {record['made_by']}; {record['base']['launch_speed']} m/s, apex {record['base']['apex_z']} m")
    for miss, m in record["misses"].items():
        last = m["tried"][-1]["judged"]
        print(f"  {miss:5s}: step {m['step']} -> {last['outcome']} (touched {sorted(set(last['touched']))})")
    unsettled = [k for k, m in record["misses"].items() if m["step"] is None]
    if unsettled:
        print(f"NOT CLEAR-CUT at any allowed step: {unsettled}; a human decides next")
        return 4
    return 0


if __name__ == "__main__":
    sys.exit(main())
