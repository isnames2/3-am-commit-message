#!/usr/bin/env python3
"""Entry for make.fun "The 3 AM Commit Message".

Writes one line: the funniest commit message an AI agent would
put in a commit right after breaking production at 3 AM.
Pure Python standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = (
    # 110 characters, well inside the 1-200 gate; the em dash is a
    # single character and the line is fixed, so the output is stable.
    "fix: revert 3am deploy that broke prod \u2014 "
    "I asked the model if it was safe and the model was me, "
    "so it said yes"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
