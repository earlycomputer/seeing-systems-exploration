"""The debugger agent: a second model that questions the run through debug/tools.py and reports to the builder.

It never edits the builder's file. It reads the brief, the chain, what holds and the file; asks questions in ```ask
blocks (why, forks, try, watch, status) that the harness answers from the run; and ends with a ```report block.
"""

from __future__ import annotations

import re

from debug.tools import Session
from loop.models import extract_block, text

PROMPTS = __import__("pathlib").Path(__file__).parent / "prompts"
SYSTEM = ("You are a debugger for physics scenes. You find out from the run itself why a scene fails, check what a "
          "change would do before you recommend it, and report plainly to the agent who will fix it.")
MAX_ASK_TURNS = 3
MAX_ASKS = 4


def numbered(source: str) -> str:
    return "\n".join(f"{n:4}| {line}" for n, line in enumerate(source.splitlines(), 1))


def answer(s: Session, ask: str) -> str:
    ask = ask.strip()
    try:
        if m := re.fullmatch(r"why\s+(\d+)", ask):
            return s.why(int(m[1]) - 1)
        if m := re.fullmatch(r"forks\s+(\d+)", ask):
            return s.forks(int(m[1]) - 1)
        if m := re.fullmatch(r"watch\s+(\S+)\s+([\d.]+)\s+([\d.]+)", ask):
            return s.watch(m[1], float(m[2]), float(m[3]))
        if ask == "status":
            return s.status()
        if m := re.fullmatch(r"try\s+(.+)", ask, flags=re.S):
            edits = []
            for part in m[1].split(";;"):
                e = re.fullmatch(r"\s*(\d+)\s+(.+?)\s+=>\s+(.+?)\s*", part, flags=re.S)
                if not e:
                    return f"I could not read `{part.strip()}`; write `try <line> <old text> => <new text>`."
                edits.append((int(e[1]), e[2], e[3]))
            return s.try_edit(edits)
    except Exception as e:  # noqa: BLE001 - a tool error goes back to the asker as text
        return f"That question failed: {type(e).__name__}: {e}"
    return f"I don't know `{ask}`. Ask why, forks, try, watch or status."


def debug(s: Session, brief: str, chat, out, label: str) -> tuple[str, list]:
    """Run the debugger on one failing file. Returns its report and the replies (for cost)."""
    chain = "\n".join(f"{k}. {line}" for k, line in enumerate(s.chain, 1))
    task = (PROMPTS / "debugger_task.md").read_text()
    for k, v in {"brief": brief, "chain": chain, "seconds": f"{s.seconds:g}", "status": s.status(),
                 "file": numbered(s.source), "turns": MAX_ASK_TURNS}.items():
        task = task.replace("{" + k + "}", str(v))
    message, replies, log = [text(task)], [], [task]
    for turn in range(MAX_ASK_TURNS + 1):
        r = chat.send(message)
        replies.append(r)
        log.append(r.text)
        report = extract_block(r.text, "report")
        if report is not None:
            break
        asks = extract_block(r.text, "ask")
        if asks is None or turn == MAX_ASK_TURNS:
            message = [text("End now with one ```report block for the builder.")]
            continue
        answers = [f"> {a}\n\n{answer(s, a)}" for a in asks.strip().splitlines()[:MAX_ASKS] if a.strip()]
        reply = "\n\n".join(answers) + (f"\n\nYou have {MAX_ASK_TURNS - turn - 1} more replies with questions."
                                         if turn < MAX_ASK_TURNS - 1 else "\n\nNow end with one ```report block.")
        log.append(reply)
        message = [text(reply)]
    else:
        report = None
    if report is None:
        report = extract_block(replies[-1].text, "report") or "The debugger gave no report."
    (out / f"{label}_debugger.md").write_text("\n\n---\n\n".join(log))
    return report.strip(), replies
