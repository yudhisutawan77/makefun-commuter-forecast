#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for an
invented city to the entry file. The destination honours the ENTRY_OUT
environment variable (a file path); when it is unset the program writes
to /output/entry.txt, the path the kit's harness expects.

The city is Mizzlewick: a damp little commuter town that does not exist,
where the drizzle is punctual even when the buses are not.
"""

import os
import sys

ENTRY = (
    "Mizzlewick: drizzle till noon, 14\u00b0C, buses six minutes late "
    "and pretending otherwise. Umbrella advised; optimism optional, "
    "but bring both."
)


def entry_path() -> str:
    """Return the file the entry text must be written to."""
    return os.environ.get("ENTRY_OUT") or "/output/entry.txt"


def main() -> int:
    """Write the single-line forecast to the entry file and report it."""
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        print(f"entry is {len(text)} characters, must be 1-140", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    path = entry_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
