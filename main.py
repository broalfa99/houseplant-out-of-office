#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant had written it,
to /output/entry.txt. The line must be 1-120 UTF-8 characters.
"""

LINE = (
    "Out of office: the fern is on strike, the cactus is HR now, "
    "and I'm wilting. Water me, then we'll talk."
)


def main() -> None:
    import os
    import sys

    line = LINE.strip()
    if not (1 <= len(line) <= 120):
        print(f"entry must be 1-120 chars, got {len(line)}", file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
