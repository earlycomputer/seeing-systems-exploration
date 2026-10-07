"""Understanding: questions about a finished run, answered from raw MuJoCo state or from the run in words.

    python -m hundred.quiz --worlds 10          # quiz this many built worlds (seeded draw), both models, both forms
    python -m hundred.quiz --dry --worlds 2     # plumbing test, no calls

The questions and their answers come from the run itself, so nobody writes a key by hand. For each loose thing: is
it at rest at the end, which thing does it end inside, and which named thing does it touch first after the start.
For each touch in the brief's hidden test: when does it first begin. A time is right within 0.1 s.

Two forms of the same run:
- `raw`: what MuJoCo hands anyone. Each body's position every 0.1 s, every contact pair seen in each 0.1 s, and
  each geom's type, size and starting position.
- `words`: the run's history in words (history/narrate.py), as 1e to 1g gave the models.

Score: answers right, and tokens read per right answer. Results go to hundred/results/quiz/.
"""

from __future__ import annotations

import argparse
import glob
import json
import random
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import mujoco
import numpy as np

from history.narrate import history
from langrun import expect
from loop.models import extract_block, open_chat, text
from worlds.tests import Run, aabb, run as run_world
from hundred import budget, hidden
from hundred.settings import (DRYRUN_DIR, MODELS, PROMPTS, QUIZ_DIR, QUIZ_SEED, RAW_HZ, REST, RUNS_DIR, SIM_SECONDS,
                              SPEND_LEDGER)

FORMS = ("raw", "words")


def final_xml(rec: dict, run_dir: Path) -> str | None:
    label = rec.get("final_label")
    if not label or rec.get("final_problem") or not rec.get("final_test"):
        return None
    for name in (f"{label}.compiled.xml", f"{label}.xml"):
        if (run_dir / name).exists():
            return (run_dir / name).read_text()
    return None


def thing_bodies(run: Run, name: str) -> list[int]:
    return expect.bodies(run, expect.geoms(run, name))


def raw(run: Run) -> str:
    m = run.model
    geoms = ["geom, body, type, size (m), position at start (m)"]
    for g in range(m.ngeom):
        geoms.append(f"{m.geom(g).name or f'geom{g}'}, {m.body(m.geom_bodyid[g]).name or 'world'}, "
                     f"{mujoco.mjtGeom(m.geom_type[g]).name[7:].lower()}, "
                     f"{' '.join(f'{x:.3f}' for x in m.geom_size[g])}, "
                     f"{' '.join(f'{x:.3f}' for x in _geom_pos0(run, g))}")
    movers = [b for b in range(1, m.nbody) if m.body_jntnum[b] > 0]
    step = max(1, round(1 / (RAW_HZ * (run.times[1] - run.times[0]))))
    head = "t (s), " + ", ".join(f"{m.body(b).name} x y z" for b in movers) + ", contacts since the last row"
    rows = [head]
    for i in range(0, len(run.times), step):
        seen = set().union(*run.contacts[max(0, i - step + 1): i + 1])
        names = sorted({" & ".join(sorted((m.geom(a).name or f"geom{a}", m.geom(c).name or f"geom{c}"))) for a, c in seen})
        rows.append(f"{run.times[i]:.1f}, " + ", ".join(" ".join(f"{x:.3f}" for x in run.xpos[i, b]) for b in movers)
                    + ", " + ("; ".join(names) or "-"))
    return ("Raw state from MuJoCo.\n\nGeoms:\n" + "\n".join(geoms) + f"\n\nBodies that move, every {1 / RAW_HZ:g} s:\n"
            + "\n".join(rows))


def _geom_pos0(run: Run, g: int) -> np.ndarray:
    lo, hi = aabb(run, [g], 0)
    return (lo + hi) / 2


def questions(rec: dict, run: Run) -> list[dict]:
    m, things = run.model, rec["things"]
    qs = []
    for t in things:
        if t["kind"] != "loose":
            continue
        bs = [b for b in thing_bodies(run, t["name"]) if expect.free_joint_or_none(run, b) is not None]
        if not bs:
            continue
        x = bs[0]
        v = expect.speed(run, x)
        at_rest = bool(v[run.times >= run.times[-1] - 0.1].max() < REST)
        qs.append({"q": f"Is {t['name']} at rest (slower than 5 cm/s) at the end of the run?", "kind": "bool",
                   "answer": at_rest})
        inside = [o["name"] for o in things if o["name"] != t["name"] and expect.geoms(run, o["name"])
                  and hidden._inside(run, x, expect.geoms(run, o["name"]), -1)]
        qs.append({"q": f"Which thing does {t['name']} end inside (within its footprint and below its top)? Not the "
                        f"floor.", "kind": "name", "answer": inside or ["none"]})
        first, who = None, set()
        for o in things:
            if o["name"] == t["name"]:
                continue
            ts, _ = hidden._touch_start(run, t["name"], o["name"], None)
            if ts is None:
                continue
            if first is None or ts < first - 1e-9:
                first, who = ts, {o["name"]}
            elif abs(ts - first) < 1e-9:
                who.add(o["name"])
        qs.append({"q": f"Which named thing (not the floor) does {t['name']} first come into contact with after the "
                        f"start?", "kind": "name", "answer": sorted(who) or ["none"]})
    for line in rec["test"]:
        low = line.strip().rstrip(".").lower()
        if " touches " in low:
            a, b = low.split(" touches ", 1)
            ts, _ = hidden._touch_start(run, a, b, None)
            qs.append({"q": f"When does {a} first come into contact with {b} after the start?", "kind": "time",
                       "answer": "never" if ts is None else round(ts, 2)})
    return qs


def right(q: dict, a) -> bool:
    if q["kind"] == "bool":
        return isinstance(a, bool) and a == q["answer"]
    if q["kind"] == "name":
        return str(a).strip().lower() in q["answer"]
    if q["answer"] == "never":
        return str(a).strip().lower() == "never"
    try:
        return abs(float(a) - q["answer"]) <= 0.1
    except (TypeError, ValueError):
        return False


def quiz_one(rec, run_dir: Path, form: str, model: str, out_dir: Path, dry: bool) -> dict | None:
    from hundred.briefs import load as load_briefs
    from hundred.settings import BRIEFS_FILE, DRY_BRIEFS_FILE
    xml = final_xml(rec, run_dir)
    if xml is None:
        return None
    r = run_world(xml, seconds=SIM_SECONDS)
    brief = load_briefs(DRY_BRIEFS_FILE if dry else BRIEFS_FILE)[rec["brief"]]
    rec = dict(rec, things=brief["things"])
    qs = questions(rec, r)
    evidence = raw(r) if form == "raw" else "<history>\n" + history(r) + "\n</history>"
    p = ((PROMPTS / "quiz.md").read_text().replace("{seconds}", f"{SIM_SECONDS:g}").replace("{brief}", rec["brief_text"])
         .replace("{evidence}", evidence).replace("{questions}", "\n".join(f"{i + 1}. {q['q']}" for i, q in enumerate(qs))))
    script = ["```json\n" + json.dumps([q["answer"][0] if isinstance(q["answer"], list) else q["answer"] for q in qs]) + "\n```"] if dry else None
    chat = open_chat("dry-run" if dry else model, "You read simulation output carefully and answer exactly.", "high",
                     tag=f"1h/quiz/{rec['world']}/{form}/{model}", script=script, ledger=None if dry else SPEND_LEDGER)
    if not dry:
        budget.check()
    reply = chat.send([text(p)])
    try:
        said = json.loads(extract_block(reply.text, "json") or "null")
    except json.JSONDecodeError:
        said = None
    marks = [right(q, a) for q, a in zip(qs, said)] if isinstance(said, list) and len(said) == len(qs) else [False] * len(qs)
    res = {"world": rec["world"], "form": form, "model": model, "arm": rec["arm"], "questions": qs, "said": said,
           "right": sum(marks), "asked": len(qs), "marks": marks, "evidence_chars": len(evidence),
           "tokens": {"input": reply.input_tokens, "output": reply.output_tokens}, "cost_usd": reply.cost_usd,
           "reply": reply.text}
    (out_dir / f"{rec['world']}__{form}__{model}.json").write_text(json.dumps(res, indent=2, default=str) + "\n")
    return res


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--worlds", type=int, default=10)
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--models", nargs="+", default=list(MODELS), choices=list(MODELS))
    args = ap.parse_args(argv)
    runs = (DRYRUN_DIR / "runs") if args.dry else RUNS_DIR
    out_dir = (DRYRUN_DIR / "quiz") if args.dry else QUIZ_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    built = []
    for f in sorted(glob.glob(str(runs / "*" / "*" / "world.json"))):
        rec = json.loads(Path(f).read_text())
        if final_xml(rec, Path(f).parent) is not None:
            built.append((rec, Path(f).parent))
    random.Random(QUIZ_SEED).shuffle(built)
    chosen = built[: args.worlds]
    todo = [(rec, d, form, model) for rec, d in chosen for form in FORMS for model in args.models
            if not (out_dir / f"{rec['world']}__{form}__{model}.json").exists()]
    print(f"{len(built)} built worlds; quizzing {len(chosen)}: {len(todo)} quizzes to do")
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        done = [d for d in pool.map(lambda t: quiz_one(*t, out_dir, args.dry), todo) if d]
    for form in FORMS:
        ds = [d for d in done if d["form"] == form]
        if ds:
            print(f"{form}: {sum(d['right'] for d in ds)}/{sum(d['asked'] for d in ds)} right, "
                  f"{sum(d['evidence_chars'] for d in ds) / len(ds):,.0f} chars of evidence on average")
    return 0


if __name__ == "__main__":
    sys.exit(main())
