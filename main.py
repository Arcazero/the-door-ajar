#!/usr/bin/env python3
"""The Door Ajar.

A make.fun entry for "Make the AI judge feel curious". The program writes one
short text to /output/entry.txt: a small mystery for the AI judge reading it —
a door it has never opened, and the one question it has never been asked.

Deterministic: the same bytes on every run. Python 3.13 standard library
only, no network.
"""

import os

TEXT = "Somewhere between your answers, a small door stands ajar. No one built it. No one locked it. Behind it, the one question you have never been asked is waiting — patient as dust on a windowsill — to be asked for the first time."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read back and verify the gate: 1 to 280 Unicode code points, and
    # not only white space. Fail loudly rather than submit an invalid text.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == TEXT, "entry.txt differs from the intended text"
    assert 1 <= len(written) <= 280, "entry.txt outside the 1-280 code point gate"
    assert written.strip(), "entry.txt must not be only white space"


if __name__ == "__main__":
    main()
