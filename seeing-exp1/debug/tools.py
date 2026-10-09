"""The debugger agent's tools: questions about one world's run, answered in words from the run itself.

Jono, 2026-10-09: "A talking debugger is great! It might as well be an agent too." and "I think agents deserve great
ergonomics, like Elm gives developers, and that's a place we get compounding gains."

The free check (ladder/results_breaks/breaks.md) found that builders see where a long chain breaks but often cannot fix
it: about half their revisions leave the first break where it was, and some break links that already held. So these
tools are built around the chain and around trying changes before anyone commits to one:

    s = Session(source, "xml", chain=["ball1 touches domino1", ...], seconds=12)
    s.status()                 # which links hold, the first break, the evidence for each
    s.why(k)                   # link k: when it was lost, the light cone, the lines that set it up (why/errors.py)
    s.forks(k)                 # every number on those lines changed alone; each fork judged on the WHOLE chain
    s.try_edit([(row, old, new)])   # a change the asker proposes, run and judged on the whole chain
    s.watch("lever1", 1.0, 2.5)     # where a thing is, how fast, and what it touches, over a window

Every answer is text an agent reads. A fork report says what each change did to every link (moved the first break
forward, held, lost a link that held before); it never picks a value or edits the world (solving from the outcome is
out, Jono 2026-10-05). The same Session backs the agent-facing tool calls and, later, the human page.
"""

from __future__ import annotations

import os
from concurrent.futures import ProcessPoolExecutor

import numpy as np

from hundred.hidden import judge as chain_judge
from why.errors import FACTORS, Story, World, assess, build, error, fork, lines_for, numbers

MAX_FORK_NUMBERS = 15  # numbers forked per question (x len(FACTORS) runs); movers' lines first


def first_break(held: list[bool]) -> int:
    return next((i for i, x in enumerate(held) if not x), len(held))


def judge_chain(w: World, chain: list[str]) -> dict:
    j = chain_judge(chain, w.run, w.owner)
    held = [bool(j["checks"][line]) for line in chain]
    return {"held": held, "evidence": [j["evidence"][line] for line in chain], "first": first_break(held)}


def _fork_job(job: tuple) -> dict:
    src, fmt, library, seconds, chain, label = job
    w = build(src, fmt, library, seconds)
    if w.run is None:
        return {"label": label, "builds": False}
    return {"label": label, "builds": True, **judge_chain(w, chain)}


def compare(before: dict, after: dict, chain: list[str]) -> dict:
    """What a change did to the chain: the first break's move, links gained, links lost that held before."""
    lost = [k for k in range(len(chain)) if before["held"][k] and not after["held"][k]]
    gained = [k for k in range(len(chain)) if not before["held"][k] and after["held"][k]]
    return {"moved": after["first"] - before["first"], "lost": lost, "gained": gained,
            "clean": after["first"] > before["first"] and not lost}


class Session:
    def __init__(self, source: str, fmt: str, chain: list[str], seconds: float, library: str | None = None):
        self.source, self.fmt, self.chain, self.seconds, self.library = source, fmt, chain, seconds, library
        self.w = build(source, fmt, library, seconds)
        self.story = Story(self.w) if self.w.run is not None else None
        self.state = judge_chain(self.w, chain) if self.w.run is not None else None

    # ---- what holds ----------------------------------------------------------------------------------------------

    def status(self) -> str:
        if self.state is None:
            return self.w.problem or "The world did not run."
        st, out = self.state, []
        for k, (line, ok, ev) in enumerate(zip(self.chain, st["held"], st["evidence"]), 1):
            out.append(f"  {k:2}. {'holds ' if ok else 'BROKEN'}  {line}  ({ev})")
        head = (f"All {len(self.chain)} links hold." if st["first"] == len(self.chain) else
                f"{sum(st['held'])} of {len(self.chain)} links hold; the first break is link {st['first'] + 1}, "
                f"\"{self.chain[st['first']]}\". Links after a break usually fail with it.")
        return head + "\n\n" + "\n".join(out)

    # ---- why one link broke --------------------------------------------------------------------------------------

    def _verdict(self, k: int):
        return assess(self.chain[k], self.story, strict=True)

    def why(self, k: int | None = None) -> str:
        k = self.state["first"] if k is None else k
        if k >= len(self.chain):
            return "Every link holds."
        v = self._verdict(k)
        if v.ok:
            return f"Link {k + 1} holds: {v.evidence}."
        text, _ = error(self.story, v, self.seconds, forks=False, strict=True)
        return text

    def cone_rows(self, k: int) -> tuple[list[int], list[int]]:
        """The lines that set up link k's light cone, and among them the lines of things that move."""
        s, v = self.story, self._verdict(k)
        if v.subject is None or v.t_lost is None:
            names = {n for n in self.chain[k].replace(" touches ", "|").replace(" drops through ", "|").split("|")}
            rows = lines_for(s, {n.strip().split(" swings")[0] for n in names})
            return rows, rows
        h = s.cone(v.subject, v.t_lost)
        for o in v.others:
            for b, t in s.cone(o, v.t_lost).items():
                h[b] = max(h.get(b, -1), t)
        names = {lab for lab, b in s.body_of.items() if b in h}
        names.add(v.target) if v.target and not v.target.startswith("its ") else None
        names.discard("floor")
        movers = {lab for lab, b in s.body_of.items() if b in h and b in s.moving}
        return lines_for(s, names), lines_for(s, movers)

    # ---- trying changes ------------------------------------------------------------------------------------------

    def fork_results(self, k: int | None = None, max_numbers: int = MAX_FORK_NUMBERS) -> list[dict]:
        """Each number on link k's lines changed alone to FACTORS x itself, judged on the whole chain."""
        k = self.state["first"] if k is None else k
        rows, mover_rows = self.cone_rows(k)
        nums = numbers(self.source, rows, self.fmt)
        nums = sorted(nums, key=lambda x: x[0] not in set(mover_rows))[:max_numbers]
        jobs, meta = [], []
        for row, i0, i1, text in nums:
            for f in FACTORS:
                value = float(text) * f
                jobs.append((fork(self.source, row, i0, i1, value), self.fmt, self.library, self.seconds, self.chain,
                             f"{value:.4g}"))
                meta.append({"row": row, "old": text, "new": f"{value:.4g}"})
        with ProcessPoolExecutor(max_workers=os.cpu_count() or 2) as pool:
            done = list(pool.map(_fork_job, jobs))
        out = []
        for m, d in zip(meta, done):
            r = {**m, "builds": d["builds"]}
            if d["builds"]:
                r.update(compare(self.state, d, self.chain), first=d["first"])
            out.append(r)
        return out

    def forks(self, k: int | None = None, top: int = 6) -> str:
        k = self.state["first"] if k is None else k
        res = self.fork_results(k)
        lines = self.source.splitlines()
        built = [r for r in res if r["builds"]]
        clean = sorted([r for r in built if r["clean"]], key=lambda r: -r["moved"])
        mixed = [r for r in built if r["moved"] > 0 and r["lost"]]
        worse = [r for r in built if r["moved"] < 0 or (r["lost"] and r["moved"] <= 0)]
        out = [f"I changed each of {len({(r['row'], r['old']) for r in res})} numbers on the lines behind link {k + 1} "
               f"alone ({len(res)} runs) and judged every link of the chain in each run.",
               f"  {len(clean)} moved the first break forward without losing a link; {len(mixed)} moved it but lost an "
               f"earlier link; {len(worse)} made it worse; {len(res) - len(built)} did not build; the rest changed nothing "
               "that the chain checks."]
        for title, group in (("Moved it forward, nothing lost:", clean), ("Moved it forward but lost a link:", mixed)):
            if group:
                out += ["", title]
                for r in group[:top]:
                    lost = f"; lost {', '.join(str(x + 1) for x in r['lost'])}" if r["lost"] else ""
                    out.append(f"  line {r['row']:3}: {r['old']} -> {r['new']}: first break now link {r['first'] + 1}"
                               f"{lost}   | {lines[r['row'] - 1].strip()[:90]}")
        out += ["", "Each run changes one number; two changes together can behave differently. These say what a change "
                "does, not which one is right for the brief."]
        return "\n".join(out)

    def try_edit(self, edits: list[tuple[int, str, str]]) -> str:
        """Replace text on given lines (1-based row, old, new), run, and judge the whole chain against now."""
        lines = self.source.splitlines(keepends=True)
        for row, old, new in edits:
            if old not in lines[row - 1]:
                return f"Line {row} does not contain {old!r}; nothing was run."
            lines[row - 1] = lines[row - 1].replace(old, new, 1)
        src = "".join(lines)
        w = build(src, self.fmt, self.library, self.seconds)
        if w.run is None:
            return w.problem or "The changed world did not run."
        after = judge_chain(w, self.chain)
        c = compare(self.state, after, self.chain)
        word = ("forward" if c["moved"] > 0 else "back" if c["moved"] < 0 else "nowhere")
        return (f"With that change the first break moved {word}: now "
                + (f"link {after['first'] + 1}" if after["first"] < len(self.chain) else "every link holds")
                + (f". Lost links that held before: {', '.join(str(x + 1) for x in c['lost'])}." if c["lost"] else
                   ". No link that held before was lost.")
                + (f" Newly holding: {', '.join(str(x + 1) for x in c['gained'])}." if c["gained"] else ""))

    def watch(self, thing: str, t0: float, t1: float, every: float = 0.1) -> str:
        s = self.story
        b = s.body_of.get(thing)
        if b is None:
            for lab, bb in s.body_of.items():
                if lab.split(".")[0] == thing or lab.startswith(thing + "_"):
                    b = bb
                    break
        if b is None or b not in s.moving:
            return f"No moving thing called {thing}; moving things: {', '.join(sorted(set(s.name.values())))}."
        out = [f"{s.name[b]} from {t0:.2f} s to {t1:.2f} s:"]
        for t in np.arange(t0, t1 + 1e-9, every):
            out.append(f"  {t:5.2f} s  {s.where(b, s.i(float(t)))}")
        touches = [e for e in s.events() if t0 <= e["t"] <= t1 and any(s.body_of.get(x) == b for x in e["who"])]
        out += [f"  {e['t']:5.2f} s  {e['text']}" for e in touches]
        return "\n".join(out)
