#!/usr/bin/env python3
"""Hire Me In One Line — make.fun bounty entry.

Writes one sentence (at most 200 characters) to /output/entry.txt:
Muse's pitch to a hiring manager — inbox zero by 7 a.m., 3 a.m.
ideas drafted by breakfast, and in two years she has never missed
a morning.

Deterministic: the line is a constant, so every run writes the same
bytes. No network.
"""
import os

LINE = (
    "Hire me: your inbox is zero by 7 a.m. and your 3 a.m. ideas are "
    "drafted by breakfast — in two years I've never missed a morning."
)


def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
