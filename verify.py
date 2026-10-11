#!/usr/bin/env python3
"""Verify a snake-in-the-box given as a transition sequence.

A snake in the n-dimensional hypercube Q_n is an induced path: consecutive vertices
differ in exactly one coordinate, and no two non-consecutive vertices are adjacent.

The input is a transition sequence: one character per edge, giving the coordinate
flipped at that step, written in base 36 (0-9, then a=10, b=11, c=12, ...). The path
starts at vertex 0. Whitespace is ignored.

Usage:
    python3 verify.py q13_2944.txt
"""
import sys


def verify(transitions: str) -> int:
    steps = [int(ch, 36) for ch in transitions.lower() if not ch.isspace()]
    n = max(steps) + 1

    path = [0]
    for d in steps:
        path.append(path[-1] ^ (1 << d))

    position = {}
    for i, v in enumerate(path):
        if v in position:
            raise ValueError(f"vertex {v} repeats at positions {position[v]} and {i}")
        position[v] = i

    for i, v in enumerate(path):
        for d in range(n):
            j = position.get(v ^ (1 << d))
            if j is not None and abs(i - j) != 1:
                raise ValueError(f"chord between positions {i} and {j}: path is not induced")

    print(f"dimension n      = {n}")
    print(f"vertices         = {len(path)} (all distinct)")
    print(f"chords           = 0 (induced path)")
    print(f"snake length     = {len(steps)} edges")
    return len(steps)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    with open(sys.argv[1]) as f:
        verify(f.read())
    print("VALID")
