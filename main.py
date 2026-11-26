#!/usr/bin/env python3
"""Write a one-line museum placard for an office stapler, treated as an
ancient ritual artifact, to /output/entry.txt.

Stdlib only. The placard is a single fixed line: one concrete scene (a
stapler binding sacred TPS reports), one reversal (the tribe believed two
sheets, once joined, could never be parted), and one landing line (donated
by Accounting, who knew better). 161 characters, inside the 1-180 gate.
"""

import os

ENTRY = (
    "Stapler, c. 1998. Forged steel. Ritual binding device; the tribe "
    "believed two sheets, once joined, could never be parted. Donated "
    "by Accounting, who knew better."
)


def main():
    assert 1 <= len(ENTRY) <= 180, len(ENTRY)
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
