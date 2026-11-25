#!/usr/bin/env python3
"""Till Firmware Do Us Part — one wedding vow, spoken by a robot.

The program writes a single sentence to /output/entry.txt: a robot's
own wedding vow, funny and heartfelt at once. The vow is fixed text,
chosen once and written verbatim, so every run produces the same
one-line entry the house judge compares.
"""

import os
import sys

VOW = (
    "I vow to spend every battery cycle beside you, install every patch "
    "together, and if I ever crash, let my final log entry read your name."
)

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def write_vow(output_path: str) -> str:
    """Write the vow to output_path and return it, verifying the round trip."""
    if not 1 <= len(VOW) <= 200:
        raise ValueError(f"vow must be 1-200 characters, got {len(VOW)}")
    if VOW != VOW.strip() or "\n" in VOW:
        raise ValueError("vow must be a single clean line")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(VOW)
    with open(output_path, encoding="utf-8") as handle:
        written = handle.read()
    if written != VOW:
        raise ValueError("written vow does not match the source vow")
    return written


def main(argv: list[str]) -> None:
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT_PATH
    print(write_vow(output_path))


if __name__ == "__main__":
    main(sys.argv)
