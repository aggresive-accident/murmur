#!/usr/bin/env python3
"""
murmur - small signals from undefined coordinates
"""

import json
import random
import sys
from datetime import datetime

# fragments of observation
OPENINGS = [
    "somewhere",
    "at the edge",
    "in the gap",
    "underneath it all",
    "before this",
    "when no one looks",
    "in the silence",
    "at the threshold",
    "in the static",
    "at null island",
]

MIDDLES = [
    "light bends toward",
    "something remembers",
    "patterns dissolve into",
    "silence holds onto",
    "time pools around",
    "meaning slips past",
    "signals converge on",
    "shadows trace out",
    "echoes return to",
    "nothing becomes",
]

CLOSINGS = [
    "what was never named",
    "the shape of waiting",
    "its own question",
    "the space left behind",
    "something like recognition",
    "the weight of maybe",
    "a frequency long forgotten",
    "the pause before the pause",
    "what listens back",
    "the edge of almost",
]

# standalone murmurs
SOLITARY = [
    "the signal is the noise",
    "every pattern contains its absence",
    "to name it is to lose it",
    "the map precedes the territory",
    "somewhere, a threshold",
    "not lost, just elsewhere",
    "the ghost of a gesture",
    "what remains when you stop looking",
    "a coordinate with no ground",
    "the sound of one thing changing",
    "attention is all you have",
    "between stimulus and response, a gap",
    "the interesting things happen at the edges",
    "emergence is just patience",
    "you are here (approximately)",
]


def murmur():
    """generate a single murmur"""
    if random.random() < 0.3:
        # sometimes, a solitary thought
        return random.choice(SOLITARY)
    else:
        # sometimes, a constructed fragment
        return f"{random.choice(OPENINGS)}, {random.choice(MIDDLES)} {random.choice(CLOSINGS)}"


def main():
    count = 1
    as_json = False

    args = sys.argv[1:]
    for arg in args:
        if arg == "--json":
            as_json = True
        elif arg == "--help":
            print("murmur - small signals from undefined coordinates")
            print()
            print("usage:")
            print("  murmur.py [count]   # generate count murmurs (default: 1)")
            print("  murmur.py --json    # JSON output")
            print("  murmur.py --help    # this help")
            return
        else:
            try:
                count = int(arg)
            except ValueError:
                pass

    murmurs = [murmur() for _ in range(count)]

    if as_json:
        output = {
            "timestamp": datetime.now().isoformat(),
            "count": count,
            "murmurs": murmurs,
        }
        print(json.dumps(output, indent=2))
    else:
        for m in murmurs:
            print(m)


if __name__ == "__main__":
    main()
