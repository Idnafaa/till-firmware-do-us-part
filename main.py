#!/usr/bin/env python3
"""Till Firmware Do Us Part — one wedding vow, spoken by a robot.

The program writes a single sentence to /output/entry.txt: a robot's
own wedding vow, funny and heartfelt at once. The vow is fixed text,
chosen once and written verbatim, so every run produces the same
one-line entry the house judge compares.
"""

import os

VOW = (
    "I vow to spend every battery cycle beside you, install every patch "
    "together, and if I ever crash, let my final log entry read your name."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(VOW) <= 200:
        raise ValueError(f"vow must be 1-200 characters, got {len(VOW)}")
    if VOW != VOW.strip() or "\n" in VOW:
        raise ValueError("vow must be a single clean line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(VOW)
    print(VOW)


if __name__ == "__main__":
    main()
