"""Check the errors at $0: 1d's five breaks in both formats, and every world that failed its hidden test in 1h.

    python -m why.bench            # writes why/results/bench.md, bench.json and every error in why/results/errors/

For 1d's breaks the cause is known (the one line the break changed), so the bench asks of each error:
- is the broken line among the lines it points at, and out of how many lines in the file;
- where the broken line ranks among the numbers that move the miss most, and whether forking it alone makes the
  expectation hold;
- how long the error is against the run in words that 1e to 1h sent (history/narrate.py), in characters.

For 1h's failures the cause isn't known; the bench records what each error says, so a person can read them. No model
reads any of this here; that is the debugging run, which costs money and waits on Jono.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from history.narrate import history
from hundred.hidden import judge as hidden_judge
from why.errors import Story, assess, build, explain

HERE = Path(__file__).parent
OUT = HERE / "results"
WORLDS = HERE.parent / "typed" / "worlds"
BROKEN = HERE.parent / "harder" / "broken"
FIXTURES_1C = HERE.parent / "worlds" / "fixtures"
RUNS_1H = HERE.parent / "hundred" / "results" / "runs"

# 1d's breaks (harder/settings.py BREAKS), each written once in the world language: (old, new) in typed/worlds.
BREAKS = {
    "catapult": ("spring        3 N·m/rad", "spring        2 N·m/rad", "ball comes to rest in bucket"),
    "cup": ("stands  on floor, 2.05 m along", "stands  on floor, 2.65 m along", "ball comes to rest in cup"),
    "stack": ("launched  3 m/s along", "launched  1.5 m/s along", "block5 touches floor"),
    "shot": ("launched  3.21 m/s along, 9.3 m/s up", "launched  3.21 m/s along, 9.3 m/s up\n  spins     -30 rad/s about y",
             ("ball drops through hoop.rim", "ball drops through rim")),
    "door": ("swings       from 0° to 120°", "swings       from 0° to 2.1°", "door reaches its lower stop"),
}
XML_BREAKS = {  # the text each 1d break wrote into the XML, to find its line
    "catapult": 'stiffness="2.0"', "cup": 'pos="2.6500 0 0"', "stack": "  1.5 0 0 0 0 0\"",
    "shot": 'qvel="3.21 0 9.3 0 -30 0"', "door": 'range="0 2.1"',
}


def row_of(text: str, needle: str) -> int:
    first = needle.split("\n")[-1].strip()
    return next(n for n, line in enumerate(text.splitlines(), 1) if first in line)


def one(name: str, fmt: str, source: str, line: str, broken_row: int | None, strict: bool = False,
        lines: list[str] | None = None) -> dict:
    t0 = time.monotonic()
    text, infos = explain(source, fmt, lines or [line], strict=strict)
    secs = round(time.monotonic() - t0, 1)
    w = build(source, fmt)
    words = history(w.run) if w.run is not None else ""
    rec = {"world": name, "format": fmt, "line": line, "file_lines": len(source.splitlines()), "seconds": secs,
           "error_chars": len(text), "history_chars": len(words), "fails": bool(infos), "broken_row": broken_row,
           "builds": w.run is not None}
    if infos:
        i = infos[0]
        rec.update(t_lost=i.get("t_lost"), rows=len(i.get("rows", [])), cone=i.get("cone"), events=i.get("events"))
        if broken_row is not None:
            rec["points_at_break"] = broken_row in i.get("rows", [])
            ranked = [r["row"] for r in i.get("forks", {}).get("rows", [])]
            moving = [r["row"] for r in i.get("forks", {}).get("rows", []) if r["moves"] > 0.005 or r["fixes"]]
            rec["break_rank"] = (moving.index(broken_row) + 1) if broken_row in moving else None
            rec["numbers_forked"] = len(ranked)
            rec["break_fork_holds"] = any(r["fixes"] for r in i["forks"]["rows"] if r["row"] == broken_row) \
                if "forks" in i else None
        if "forks" in i:
            rec["any_fork_holds"] = any(r["fixes"] for r in i["forks"]["rows"])
            rec["forks"], rec["fork_seconds"] = i["forks"]["forks"], i["forks"]["seconds"]
    return rec, text


def breaks() -> list[tuple[dict, str]]:
    out = []
    for name, (old, new, lines) in BREAKS.items():
        line, xml_line = (lines, lines) if isinstance(lines, str) else lines
        good = (WORLDS / f"{name}.world").read_text()
        assert good.count(old) == 1, (name, old)
        src = good.replace(old, new)
        if "expect" in src:
            src = src[: src.index("\nexpect")] + f"\nexpect\n  {line}\n"
        out.append(one(name, "world", src, line, row_of(src, new)))
        xml = (BROKEN / f"{name}.xml").read_text()
        out.append(one(name, "xml", xml, xml_line, row_of(xml, XML_BREAKS[name])))
    return out


def failures_1h() -> list[tuple[dict, str]]:
    out = []
    for d in sorted(RUNS_1H.iterdir()):
        stamps = sorted(d.iterdir())
        rec = json.loads((stamps[-1] / "world.json").read_text())
        if rec.get("passes_final") or not rec.get("final_label"):
            continue
        label, run_dir = rec["final_label"], stamps[-1]
        if rec["arm"] == "language":
            fmt, src = "world", (run_dir / f"{label}.world").read_text()
            parts = run_dir / f"{label}.parts"
            if parts.exists():
                continue  # its own parts library; rare, left out of the bench
        else:
            fmt, src = "xml", (run_dir / f"{label}.xml").read_text()
        lines = rec["test"]
        w = build(src, fmt)
        failing = []
        if w.run is not None:
            verdict = hidden_judge(lines, w.run, w.owner)
            failing = [x for x in lines if not verdict["checks"].get(x, True)]
            s = Story(w)
            plain = {x: assess(x, s).ok for x in failing}
        r, text = one(rec["world"], fmt, src, failing[0], None, strict=True, lines=lines) if failing else ({"world": rec["world"], "format": fmt,
                                                                                 "builds": w.run is not None}, "")
        r.update(arm=rec["arm"], failing=failing, claimed_works=rec.get("claims_works"),
                 hidden_only=[x for x in failing if plain.get(x)] if failing else [])
        out.append((r, text))
    return out


def table(rows: list[dict]) -> list[str]:
    out = ["| world | format | lost at | lines pointed at / file | points at the break | break's rank among numbers that "
           "move it | forking the break alone fixes it | error chars | run-in-words chars | seconds |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if not r.get("fails"):
            out.append(f"| {r['world']} | {r['format']} | holds: {r['line']} | | | | | | {r['history_chars']:,} | |")
            continue
        out.append(f"| {r['world']} | {r['format']} | {r['t_lost']:.2f} s | {r['rows']} / {r['file_lines']} | "
                   f"{'yes' if r.get('points_at_break') else 'no'} | "
                   f"{r['break_rank'] if r.get('break_rank') else '-'} of {r.get('numbers_forked', 0)} | "
                   f"{'yes' if r.get('break_fork_holds') else 'no'} | {r['error_chars']:,} | {r['history_chars']:,} | "
                   f"{r['seconds']} |")
    return out


def main() -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / "errors").mkdir(exist_ok=True)
    b = breaks()
    f = failures_1h()
    for r, text in b:
        (OUT / "errors" / f"break_{r['world']}.{r['format']}.txt").write_text(text)
    for r, text in f:
        if text:
            (OUT / "errors" / f"1h_{r['world']}.txt").write_text(text)
    rows_b = [r for r, _ in b]
    rows_f = [r for r, _ in f]
    (OUT / "bench.json").write_text(json.dumps({"breaks": rows_b, "failures_1h": rows_f}, indent=2, default=str) + "\n")
    failed = [r for r in rows_b if r.get("fails")]
    md = ["# Errors with the why: the $0 bench", "",
          "Generated by `python -m why.bench`; never edited by hand. No model calls. Every error is in `errors/`.", "",
          "## 1d's five breaks, in both formats", "",
          "The cause is known: the one line each break changed. Characters are a stand-in for tokens (about four "
          "characters a token).", ""] + table(rows_b) + [""]
    if failed:
        pts = sum(bool(r.get("points_at_break")) for r in failed)
        top = sum(r.get("break_rank") == 1 for r in failed)
        top3 = sum(bool(r.get("break_rank")) and r["break_rank"] <= 3 for r in failed)
        md += [f"Of the {len(failed)} broken worlds whose expectation fails, the error points at the broken line in "
               f"{pts}, ranks it first among the numbers that move the miss in {top}, and in the top three in {top3}.", ""]
    md += ["## 1h's failures (real model-written worlds, hidden tests)", "",
           "| world | arm | said it worked | failing hidden line | fails by the plain form too | lost at | lines pointed at / file "
           "| one forked number makes it hold | error chars | run-in-words chars |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows_f:
        if not r.get("failing"):
            md.append(f"| {r['world']} | {r['arm']} | {r.get('claimed_works')} | (builds: {r['builds']}) | | | | | | |")
            continue
        md.append(f"| {r['world']} | {r['arm']} | {r.get('claimed_works')} | {r['failing'][0]} | "
                  f"{'no' if r['failing'][0] in r['hidden_only'] else 'yes'} | "
                  f"{(str(round(r['t_lost'], 2)) + ' s') if r.get('t_lost') is not None else '-'} | "
                  f"{r.get('rows', '-')} / {r['file_lines']} | {'yes' if r.get('any_fork_holds') else 'no'} | "
                  f"{r.get('error_chars', 0):,} | {r.get('history_chars', 0):,} |")
    (OUT / "bench.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
