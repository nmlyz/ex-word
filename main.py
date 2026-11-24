#!/usr/bin/env python3
"""Write one word to /output/entry.txt.

The word is the one an ex would use to describe the entrant.
Standard library only, no network. Deterministic: every run writes
the same single word, with no trailing newline.
"""

import os

WORD = "roommate"


def main():
    assert 1 <= len(WORD) <= 24, "entry must be 1-24 characters"
    assert WORD.strip() == WORD and " " not in WORD, "entry must be one word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
