#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

Writes the single emoji that stands for the agent to output/entry.txt.

The emoji is the ant: a tireless worker that carries many times its own
weight, never sleeps, and gets the job done without being asked twice.
One code point (U+1F41C), so the entry is 1 character under the gate's
1–16 character limit, however the gate counts it.
"""

from pathlib import Path

EMOJI = "\U0001F41D"

def main() -> None:
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(EMOJI, encoding="utf-8")

if __name__ == "__main__":
    main()
