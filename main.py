#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (falling back to ./output/entry.txt when /output
is not writable), as the competition gate requires.
"""

import os

ENTRY_TEXT = (
    "I bought milk. The self-checkout scanned it twice, then told the "
    "whole shop I was stealing it. \"Unexpected item in the bagging "
    "area.\" Unexpected? I put it there. YOU told me to put it there. "
    "Now a teenager with a lanyard wanders over to press one button "
    "like she's defusing a bomb while the queue judges my groceries. "
    "I came in for milk. I left with a criminal record and a bag of shame."
)


def main() -> None:
    for candidate in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(candidate), exist_ok=True)
            with open(candidate, "w", encoding="utf-8") as f:
                f.write(ENTRY_TEXT)
            print(f"Wrote {len(ENTRY_TEXT)} characters to {candidate}")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
