"""Step 1, authoring: the primary model writes MJCF from the brief; MuJoCo loads it and runs it for 2 s.

    python -m scene.author --model opus-5.5

Acceptance (handoff): the file loads without edits by hand, and the hoop geom's z equals 3.05 m when read
back from the model. Writes scene/authored.xml exactly as the model wrote it, and scene/authored.json with
the prompt, every reply, the measurements and the trajectory. If MuJoCo cannot load the file, the error
goes back to the model (up to --retries times) and every attempt is logged.
"""

from __future__ import annotations

import argparse
import json
import sys
import time

from config import AUTHORED_SCENE, BRIEF_FILE, DRYRUN_DIR, FIXTURE_SCENE, SCENE_DIR, TARGETS
from loop.models import MODELS, extract_block, open_chat, text
from scene import sim

SYSTEM = "You write MuJoCo MJCF scenes that load on the first try and that a person can read."


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default="opus-5.5", choices=sorted(MODELS))
    ap.add_argument("--effort", default="high")
    ap.add_argument("--retries", type=int, default=2, help="times a MuJoCo load error is sent back to the model")
    ap.add_argument("--force", action="store_true", help="overwrite an existing scene/authored.xml")
    args = ap.parse_args()

    dry = MODELS[args.model].provider == "dry"
    out_xml = (DRYRUN_DIR / "authored.xml") if dry else AUTHORED_SCENE
    if out_xml.exists() and not args.force:
        print(f"{out_xml} exists and the matrix depends on it; pass --force to replace it", file=sys.stderr)
        return 1

    brief = BRIEF_FILE.read_text().strip()
    prompt = (SCENE_DIR / "author_prompt.md").read_text().replace("{brief}", brief)
    script = [f"Dry run: the hand-written fixture.\n```xml\n{FIXTURE_SCENE.read_text()}```"] if dry else None
    chat = open_chat(args.model, SYSTEM, args.effort, tag="author", script=script)

    log = {"model": args.model, "model_id": MODELS[args.model].model_id, "effort": args.effort, "brief": brief,
           "system": SYSTEM, "prompt": prompt, "attempts": [],
           "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    message, xml, loaded = prompt, None, None
    for attempt in range(args.retries + 1):
        reply = chat.send([text(message)])
        xml = extract_block(reply.text, "xml")
        entry = {"sent": message, "reply": reply.text, "thinking": reply.thinking, "usage": reply.summary()}
        log["attempts"].append(entry)
        if xml is None:
            entry["load_error"] = "no ```xml block in the reply"
            message = "I could not find a ```xml block in your reply. Reply with the complete file in one."
            continue
        try:
            loaded = sim.load(xml)
            break
        except Exception as e:  # MuJoCo raises ValueError with the parser's message
            entry["load_error"] = str(e)
            message = (f"MuJoCo could not load the file:\n\n{e}\n\n"
                       "Reply with the complete corrected file in one ```xml block.")

    if loaded is None:
        log["accepted"] = False
        _write(out_xml, xml, log)
        print("FAILED: no attempt loaded. See", out_xml.with_suffix(".json"))
        return 2

    log["load_log"] = loaded.log
    log["measurements"] = sim.measure(loaded)
    log["trajectory"] = sim.trajectory(loaded)
    hoop = log["measurements"]["hoop_height"]
    log["acceptance"] = {
        "loaded_without_hand_edits": True,
        "attempts": len(log["attempts"]),
        "hoop_height": hoop,
        "hoop_height_is_3.05": abs(hoop - TARGETS["hoop_height"]) < 1e-3,
        "all_targets_within_tolerance": {k: sim.within(log["measurements"], k) for k in TARGETS},
    }
    log["accepted"] = log["acceptance"]["hoop_height_is_3.05"]
    _write(out_xml, xml, log)
    print(json.dumps(log["acceptance"], indent=2))
    print("PASS" if log["accepted"] else "FAIL", "->", out_xml)
    return 0 if log["accepted"] else 3


def _write(out_xml, xml, log):
    out_xml.parent.mkdir(parents=True, exist_ok=True)
    if xml is not None:
        out_xml.write_text(xml)
    log["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    out_xml.with_suffix(".json").write_text(json.dumps(log, indent=2) + "\n")


if __name__ == "__main__":
    sys.exit(main())
