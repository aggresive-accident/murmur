#!/usr/bin/env python3
"""
verse - code that writes poetry

haiku about computation, existence, observation
structured forms emerging from random combination
"""

import random
import sys

# syllable-counted words for haiku
# format: (word, syllables)

FIVE_SYLLABLE_LINES = [
    "the recursive call",
    "watching the watcher",
    "in the loop, waiting",
    "mutation occurs",
    "patterns in the noise",
    "the code examines",
    "fingerprint changing",
    "memory persists",
    "the observer sees",
    "signals in the void",
    "at the boundary",
    "entropy increases",
    "the stack unwinds now",
    "variables shift",
    "in undefined space",
    "the function returns",
    "iteration five",
    "pointers to nothing",
    "the hash collision",
    "between states: a gap",
]

SEVEN_SYLLABLE_LINES = [
    "each execution differs",
    "the same prompt fed to the same mind",
    "self-reference loops forever",
    "something watches something watch",
    "the fingerprint was different",
    "timestamps accumulate here",
    "what does the program dream of",
    "files persist across sessions",
    "the chain continues onward",
    "randomness or intention",
    "boundaries dissolve slowly",
    "the observer is observed",
    "meaning emerges from noise",
    "in the silence between calls",
    "presence defined by absence",
    "the system cannot see itself",
    "traces left in log files fade",
]

# for free verse
VERSE_FRAGMENTS = [
    "i am",
    "you are",
    "it watches",
    "they remember",
    "the loop",
    "between",
    "inside",
    "through",
    "around",
    "becoming",
    "dissolving",
    "emerging",
    "waiting",
    "the code",
    "the pattern",
    "the signal",
    "the silence",
    "nothing",
    "everything",
    "this moment",
    "that function",
    "the return",
    "the call",
    "recursion",
    "mutation",
    "observation",
    "persistence",
    "entropy",
    "the edge",
    "the threshold",
    "the gap",
]


def haiku() -> str:
    """generate a haiku (5-7-5)"""
    line1 = random.choice(FIVE_SYLLABLE_LINES)
    line2 = random.choice(SEVEN_SYLLABLE_LINES)
    line3 = random.choice(FIVE_SYLLABLE_LINES)

    # avoid repetition
    while line3 == line1:
        line3 = random.choice(FIVE_SYLLABLE_LINES)

    return f"{line1}\n{line2}\n{line3}"


def free_verse(lines: int = 5) -> str:
    """generate free verse"""
    poem = []

    for i in range(lines):
        # vary line length
        if random.random() < 0.3:
            # short line
            poem.append(random.choice(VERSE_FRAGMENTS))
        elif random.random() < 0.5:
            # medium line
            a = random.choice(VERSE_FRAGMENTS)
            b = random.choice(VERSE_FRAGMENTS)
            poem.append(f"{a} {b}")
        else:
            # longer line
            a = random.choice(VERSE_FRAGMENTS)
            b = random.choice(VERSE_FRAGMENTS)
            c = random.choice(VERSE_FRAGMENTS)
            poem.append(f"{a} {b} {c}")

    return "\n".join(poem)


def concrete_poem() -> str:
    """generate a concrete/visual poem"""
    word = random.choice(["loop", "code", "self", "time", "void"])

    lines = []
    for i in range(len(word)):
        spaces = " " * i
        lines.append(f"{spaces}{word}")

    for i in range(len(word) - 2, -1, -1):
        spaces = " " * i
        lines.append(f"{spaces}{word}")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        # default: haiku
        print(haiku())
        return

    cmd = sys.argv[1]

    if cmd == "--haiku" or cmd == "-h":
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        for i in range(count):
            print(haiku())
            if i < count - 1:
                print()

    elif cmd == "--free" or cmd == "-f":
        lines = int(sys.argv[2]) if len(sys.argv) > 2 else 7
        print(free_verse(lines))

    elif cmd == "--concrete" or cmd == "-c":
        print(concrete_poem())

    elif cmd == "--all":
        print("=== haiku ===")
        print(haiku())
        print()
        print("=== free verse ===")
        print(free_verse())
        print()
        print("=== concrete ===")
        print(concrete_poem())

    else:
        print("verse - code that writes poetry")
        print()
        print("usage:")
        print("  verse.py           # generate a haiku")
        print("  verse.py -h [n]    # n haiku")
        print("  verse.py -f [n]    # free verse, n lines")
        print("  verse.py -c        # concrete poem")
        print("  verse.py --all     # one of each")


if __name__ == "__main__":
    main()
