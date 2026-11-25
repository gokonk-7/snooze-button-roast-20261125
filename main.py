#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes one roast line to /output/entry.txt: an alarm clock that rings
at 6 AM on a Saturday morning, roasted in a single line.
"""

import os

ENTRY = "My alarm clock rang at 6 AM on a Saturday like an ex texting 'u up?' from a number I blocked in 2019."


def main() -> None:
    # Enforce the house gate locally: 1-200 UTF-8 characters, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
