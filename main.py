#!/usr/bin/env python3
"""Houseplant out-of-office auto-reply — make.fun bounty entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt.
"""

import os

LINE = (
    "Out of office: the plant in the corner has unionised "
    "and is demanding sunlight, water, and fewer meetings."
)

OUTPUT_PATH = "/output/entry.txt"


MAX_CHARS = 120


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
