#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes exactly one letter to entry.txt: A for coffee.
The gate requires 1 to 1 characters, so no newline, no extra text.
"""

import os

LETTER = "A"  # A for coffee: the bolder, more vivid answer of the two


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
