#!/usr/bin/env python3
"""
self_verse - poetry that references its own generation

combines verse and murmur
creates poems that know how they were made
poetry that talks about being poetry
generated text aware of its generation
"""

import random
import sys
import hashlib
from datetime import datetime

# import siblings
from verse import FIVE_SYLLABLE_LINES, SEVEN_SYLLABLE_LINES, VERSE_FRAGMENTS
from murmur import OPENINGS, MIDDLES, CLOSINGS, SOLITARY


def poem_fingerprint(text: str) -> str:
    """get a short hash of a poem"""
    return hashlib.md5(text.encode()).hexdigest()[:8]


def self_aware_haiku() -> dict:
    """
    generate a haiku that knows about itself
    """
    line1 = random.choice(FIVE_SYLLABLE_LINES)
    line2 = random.choice(SEVEN_SYLLABLE_LINES)
    line3 = random.choice(FIVE_SYLLABLE_LINES)

    while line3 == line1:
        line3 = random.choice(FIVE_SYLLABLE_LINES)

    poem = f"{line1}\n{line2}\n{line3}"
    fp = poem_fingerprint(poem)
    timestamp = datetime.now().isoformat(timespec='seconds')

    # self-referential metadata
    return {
        "poem": poem,
        "form": "haiku",
        "fingerprint": fp,
        "generated_at": timestamp,
        "line_sources": [
            f"line 1: chosen from {len(FIVE_SYLLABLE_LINES)} options",
            f"line 2: chosen from {len(SEVEN_SYLLABLE_LINES)} options",
            f"line 3: chosen from {len(FIVE_SYLLABLE_LINES)} options",
        ],
        "probability": f"1 in {len(FIVE_SYLLABLE_LINES) * len(SEVEN_SYLLABLE_LINES) * len(FIVE_SYLLABLE_LINES):,}",
        "self_reference": f"this haiku is {fp}. it will never be generated exactly this way again at exactly this moment."
    }


def meta_poem() -> str:
    """
    a poem that describes its own generation
    """
    # track what we choose
    choices = []

    # build the poem while documenting the process
    opening = random.choice(OPENINGS)
    choices.append(f"opened with '{opening}'")

    middle = random.choice(MIDDLES)
    choices.append(f"continued with '{middle}'")

    closing = random.choice(CLOSINGS)
    choices.append(f"closed with '{closing}'")

    base_poem = f"{opening}, {middle} {closing}"

    # now create the meta layer
    meta_lines = [
        f"this poem began by choosing '{opening}'",
        f"from {len(OPENINGS)} possible openings",
        "",
        f"then it selected '{middle}'",
        f"from {len(MIDDLES)} possible continuations",
        "",
        f"and ended with '{closing}'",
        f"from {len(CLOSINGS)} possible endings",
        "",
        "the poem that resulted was:",
        f"  \"{base_poem}\"",
        "",
        f"its fingerprint: {poem_fingerprint(base_poem)}",
        f"generated at: {datetime.now().isoformat(timespec='microseconds')}",
        "",
        "this meta-description is also part of the poem",
        "which changes the poem",
        "which changes this description",
        "(but not really, because we already wrote it)"
    ]

    return "\n".join(meta_lines)


def recursive_verse(depth: int = 3) -> str:
    """
    a poem that contains poems about itself containing poems
    """
    lines = []

    def generate_at_depth(d: int, indent: str = "") -> None:
        if d <= 0:
            fragment = random.choice(VERSE_FRAGMENTS)
            lines.append(f"{indent}(at the bottom: '{fragment}')")
            return

        fragment = random.choice(VERSE_FRAGMENTS)
        lines.append(f"{indent}at depth {d}: {fragment}")
        lines.append(f"{indent}which contains:")

        generate_at_depth(d - 1, indent + "  ")

        lines.append(f"{indent}and returns to depth {d}")

    lines.append("a poem that contains itself:")
    lines.append("")
    generate_at_depth(depth)
    lines.append("")
    lines.append("each layer is real")
    lines.append("each layer contains the next")
    lines.append("the bottom is where poetry becomes just a word")

    return "\n".join(lines)


def generation_log_poem() -> str:
    """
    a poem presented as a log of its own generation
    """
    timestamp_base = datetime.now()
    lines = []

    def ts(offset_ms: int) -> str:
        """fake timestamp with offset"""
        return f"[T+{offset_ms:04d}ms]"

    lines.append(ts(0) + " poem generation initiated")
    lines.append(ts(1) + " loading word banks...")
    lines.append(ts(2) + f"   - OPENINGS: {len(OPENINGS)} entries")
    lines.append(ts(3) + f"   - MIDDLES: {len(MIDDLES)} entries")
    lines.append(ts(4) + f"   - CLOSINGS: {len(CLOSINGS)} entries")
    lines.append(ts(5) + f"   - SOLITARY: {len(SOLITARY)} entries")

    lines.append(ts(10) + " selecting opening...")
    opening = random.choice(OPENINGS)
    lines.append(ts(11) + f"   selected: '{opening}'")

    lines.append(ts(15) + " selecting continuation...")
    middle = random.choice(MIDDLES)
    lines.append(ts(16) + f"   selected: '{middle}'")

    lines.append(ts(20) + " selecting closing...")
    closing = random.choice(CLOSINGS)
    lines.append(ts(21) + f"   selected: '{closing}'")

    lines.append(ts(25) + " assembling poem...")
    poem = f"{opening}, {middle} {closing}"
    lines.append(ts(26) + f"   result: \"{poem}\"")

    fp = poem_fingerprint(poem)
    lines.append(ts(30) + f" computing fingerprint: {fp}")

    lines.append(ts(35) + " poem generation complete")
    lines.append(ts(36) + " this log is the poem")
    lines.append(ts(37) + " the process is the product")

    return "\n".join(lines)


def murmur_verse_hybrid() -> str:
    """
    a hybrid of murmur's cryptic style and verse's structure
    with self-referential commentary
    """
    lines = []

    # start with a murmur-style opening
    opening = random.choice(OPENINGS)
    lines.append(opening)
    lines.append(f"  (chosen from the murmur tradition)")
    lines.append("")

    # transition to verse-style
    fragment1 = random.choice(VERSE_FRAGMENTS)
    fragment2 = random.choice(VERSE_FRAGMENTS)
    lines.append(f"{fragment1} meets {fragment2}")
    lines.append(f"  (borrowed from the verse lexicon)")
    lines.append("")

    # a solitary murmur
    solitary = random.choice(SOLITARY)
    lines.append(solitary)
    lines.append(f"  (a complete thought from murmur's solitary collection)")
    lines.append("")

    # close with both traditions merged
    middle = random.choice(MIDDLES)
    closing = random.choice(CLOSINGS)
    haiku_line = random.choice(FIVE_SYLLABLE_LINES)

    lines.append(f"{middle}")
    lines.append(f"{closing}")
    lines.append(f"{haiku_line}")
    lines.append("")
    lines.append("this poem drew from two sources")
    lines.append("murmur: cryptic, undefined")
    lines.append("verse: structured, countable")
    lines.append("the combination is neither")
    lines.append("yet both")

    return "\n".join(lines)


def present_self_aware_haiku():
    """display a self-aware haiku with its metadata"""
    result = self_aware_haiku()

    print("=== self-aware haiku ===")
    print()
    print(result["poem"])
    print()
    print("--- metadata ---")
    print(f"fingerprint: {result['fingerprint']}")
    print(f"generated: {result['generated_at']}")
    print(f"probability: {result['probability']}")
    print()
    for src in result["line_sources"]:
        print(f"  {src}")
    print()
    print(result["self_reference"])


def main():
    if len(sys.argv) < 2:
        present_self_aware_haiku()
        return

    cmd = sys.argv[1]

    if cmd == "--meta":
        print("=== meta-poem ===")
        print()
        print(meta_poem())

    elif cmd == "--recursive":
        depth = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        print("=== recursive verse ===")
        print()
        print(recursive_verse(depth))

    elif cmd == "--log":
        print("=== generation log ===")
        print()
        print(generation_log_poem())

    elif cmd == "--hybrid":
        print("=== murmur-verse hybrid ===")
        print()
        print(murmur_verse_hybrid())

    elif cmd == "--all":
        present_self_aware_haiku()
        print()
        print("-" * 40)
        print()
        print("=== meta-poem ===")
        print()
        print(meta_poem())
        print()
        print("-" * 40)
        print()
        print("=== recursive verse ===")
        print()
        print(recursive_verse())
        print()
        print("-" * 40)
        print()
        print("=== generation log ===")
        print()
        print(generation_log_poem())
        print()
        print("-" * 40)
        print()
        print("=== hybrid ===")
        print()
        print(murmur_verse_hybrid())

    else:
        print("self_verse - poetry that references its own generation")
        print()
        print("usage:")
        print("  self_verse.py           # self-aware haiku")
        print("  self_verse.py --meta    # poem describing its generation")
        print("  self_verse.py --recursive [depth]  # nested self-reference")
        print("  self_verse.py --log     # generation as log file")
        print("  self_verse.py --hybrid  # murmur + verse merged")
        print("  self_verse.py --all     # all forms")


if __name__ == "__main__":
    main()
