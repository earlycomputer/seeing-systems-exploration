"""Write harder/broken/<brief>.xml: each of 1c's hand-written worlds with its one deliberate break (settings.BREAKS).

    python -m harder.breaks

The files are generated, committed, and sent to the models exactly as written. Never edit them by hand.
"""

from __future__ import annotations

from harder.settings import BREAKS, BROKEN_DIR, FIXTURES_1C


def broken(brief: str) -> str:
    old, new, _ = BREAKS[brief]
    src = (FIXTURES_1C / f"{brief}.xml").read_text()
    if src.count(old) != 1:
        raise ValueError(f"{brief}: the break's text must appear exactly once in the fixture")
    return src.replace(old, new)


def main() -> int:
    BROKEN_DIR.mkdir(parents=True, exist_ok=True)
    for b in BREAKS:
        (BROKEN_DIR / f"{b}.xml").write_text(broken(b))
        print(f"{b}: {BREAKS[b][2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
