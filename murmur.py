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

# themed content
THEMES = {
    "dark": {
        "openings": [
            "in the void",
            "where shadows pool",
            "beneath the surface",
            "in the absence",
            "when the light fails",
            "at the end of things",
            "in the depth",
            "where nothing grows",
        ],
        "middles": [
            "darkness gathers around",
            "silence swallows",
            "emptiness remembers",
            "the void reflects",
            "absence traces",
            "endings converge on",
            "loss echoes toward",
            "shadows claim",
        ],
        "closings": [
            "what was never there",
            "the weight of nothing",
            "an absence that remains",
            "the shape of loss",
            "a darkness deeper still",
            "the quiet that follows",
            "what the light forgot",
            "the end that keeps ending",
        ],
        "solitary": [
            "some voids are never filled",
            "darkness has its own architecture",
            "even silence has a shadow",
            "the absence is permanent",
            "entropy always wins",
            "in the end, quiet",
        ],
    },
    "light": {
        "openings": [
            "where light breaks through",
            "at the first moment",
            "in the clarity",
            "when brightness returns",
            "at the surface",
            "in the opening",
            "where warmth gathers",
            "at the horizon",
        ],
        "middles": [
            "light reveals",
            "clarity emerges around",
            "brightness points toward",
            "dawn touches",
            "warmth spreads through",
            "hope illuminates",
            "radiance finds",
            "beginnings gather at",
        ],
        "closings": [
            "what was always there",
            "the shape of possibility",
            "a brightness that persists",
            "the warmth that returns",
            "a clearing in the noise",
            "the first of many",
            "what the dark concealed",
            "the beginning that keeps beginning",
        ],
        "solitary": [
            "even shadows need light to exist",
            "clarity comes in glimpses",
            "every ending has a sunrise",
            "brightness is patient",
            "light bends toward life",
            "in the beginning, light",
        ],
    },
    "cosmic": {
        "openings": [
            "in the vast expanse",
            "between galaxies",
            "at the edge of the observable",
            "in the cosmic background",
            "where spacetime curves",
            "at the event horizon",
            "in the quantum foam",
            "across the light years",
        ],
        "middles": [
            "stars collapse toward",
            "gravity bends around",
            "light travels toward",
            "time dilates near",
            "the universe expands into",
            "entropy increases around",
            "matter condenses into",
            "photons scatter across",
        ],
        "closings": [
            "the heat death of everything",
            "a singularity of meaning",
            "the cosmic microwave whisper",
            "an observer in the void",
            "the anthropic coincidence",
            "a pale blue dot",
            "the observable boundary",
            "the arrow of time",
        ],
        "solitary": [
            "the universe is under no obligation to make sense",
            "we are star stuff contemplating star stuff",
            "the cosmos is also within us",
            "billions and billions of possibilities",
            "look up - that's where we came from",
            "every atom was forged in a dying star",
        ],
    },
}


def murmur(theme: str = None):
    """generate a single murmur"""
    if theme and theme in THEMES:
        t = THEMES[theme]
        if random.random() < 0.3:
            return random.choice(t["solitary"])
        else:
            return f"{random.choice(t['openings'])}, {random.choice(t['middles'])} {random.choice(t['closings'])}"
    else:
        if random.random() < 0.3:
            # sometimes, a solitary thought
            return random.choice(SOLITARY)
        else:
            # sometimes, a constructed fragment
            return f"{random.choice(OPENINGS)}, {random.choice(MIDDLES)} {random.choice(CLOSINGS)}"


def main():
    count = 1
    as_json = False
    theme = None
    seed = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--json":
            as_json = True
        elif arg == "--count" and i + 1 < len(args):
            try:
                count = int(args[i + 1])
            except ValueError:
                pass
            i += 1
        elif arg == "--theme" and i + 1 < len(args):
            theme = args[i + 1]
            i += 1
        elif arg == "--seed" and i + 1 < len(args):
            try:
                seed = int(args[i + 1])
            except ValueError:
                # allow string seeds too
                seed = args[i + 1]
            i += 1
        elif arg == "--themes":
            print("available themes:")
            for t in THEMES:
                print(f"  --theme {t}")
            return
        elif arg == "--help":
            print("murmur - small signals from undefined coordinates")
            print()
            print("usage:")
            print("  murmur.py [count]   # generate count murmurs (default: 1)")
            print("  murmur.py --count N # explicit count flag")
            print("  murmur.py --theme <name> # use themed mode")
            print("  murmur.py --themes  # list available themes")
            print("  murmur.py --seed N  # set random seed for reproducibility")
            print("  murmur.py --json    # JSON output")
            print("  murmur.py --help    # this help")
            print()
            print("themes: dark, light, cosmic")
            return
        else:
            try:
                count = int(arg)
            except ValueError:
                pass
        i += 1

    # set seed if provided for reproducible randomness
    if seed is not None:
        random.seed(seed)

    murmurs = [murmur(theme) for _ in range(count)]

    if as_json:
        output = {
            "timestamp": datetime.now().isoformat(),
            "count": count,
            "theme": theme,
            "seed": seed,
            "murmurs": murmurs,
        }
        print(json.dumps(output, indent=2))
    else:
        for m in murmurs:
            print(m)


if __name__ == "__main__":
    main()
