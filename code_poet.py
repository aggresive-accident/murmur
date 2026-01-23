#!/usr/bin/env python3
"""
code_poet - writes poetry about the code it reads

give it a python file
it will read the code
and write a poem about what it sees
"""

import re
import sys
import random
from pathlib import Path


# poetic vocabulary for code concepts
VOCAB = {
    "function": [
        "a ritual begins",
        "an invocation",
        "a named becoming",
        "a process awakens",
        "instructions gather",
    ],
    "class": [
        "a blueprint forms",
        "a type emerges",
        "a category of being",
        "a template for existence",
        "a mold for instances",
    ],
    "loop": [
        "repetition unfolds",
        "the cycle turns",
        "again and again",
        "iteration's dance",
        "the wheel spins",
    ],
    "conditional": [
        "a choice point",
        "the path divides",
        "if this then that",
        "decision crystallizes",
        "branches diverge",
    ],
    "return": [
        "something is given back",
        "the answer emerges",
        "completion arrives",
        "output flows forth",
        "the function speaks",
    ],
    "import": [
        "dependencies arrive",
        "borrowed power",
        "other code joins",
        "connections form",
        "knowledge imported",
    ],
    "variable": [
        "a name holds meaning",
        "data takes form",
        "memory allocated",
        "a binding made",
        "something is named",
    ],
    "comment": [
        "the author whispers",
        "marginalia",
        "a note to the future",
        "explanation offered",
        "context given",
    ],
    "exception": [
        "error caught",
        "failure anticipated",
        "the unexpected handled",
        "safety nets spread",
        "exceptions allowed",
    ],
    "string": [
        "words encoded",
        "text appears",
        "characters lined up",
        "messages formed",
        "human language embedded",
    ],
}

# poetic observations about code structure
STRUCTURAL = [
    "indentation creates hierarchy",
    "whitespace breathes between statements",
    "the code flows downward",
    "nesting deepens like thought",
    "each line a step forward",
]

# meta observations
META = [
    "this code will run",
    "electrons will flow",
    "logic will execute",
    "the machine will understand",
    "meaning becomes action",
]


def analyze_code(source: str) -> dict:
    """extract features from code for poeticizing"""
    features = {
        "functions": len(re.findall(r'^def \w+', source, re.MULTILINE)),
        "classes": len(re.findall(r'^class \w+', source, re.MULTILINE)),
        "loops": len(re.findall(r'\b(for|while)\b', source)),
        "conditionals": len(re.findall(r'\bif\b', source)),
        "returns": len(re.findall(r'\breturn\b', source)),
        "imports": len(re.findall(r'^(?:import|from)', source, re.MULTILINE)),
        "comments": len(re.findall(r'#.*$', source, re.MULTILINE)),
        "docstrings": len(re.findall(r'"""[\s\S]*?"""', source)),
        "strings": len(re.findall(r'["\'].*?["\']', source)),
        "lines": len(source.strip().split('\n')),
        "characters": len(source),
    }

    # extract function names
    features["function_names"] = re.findall(r'^def (\w+)', source, re.MULTILINE)

    # extract class names
    features["class_names"] = re.findall(r'^class (\w+)', source, re.MULTILINE)

    return features


def poeticize_name(name: str) -> str:
    """turn a code name into poetic language"""
    # split camelCase and snake_case
    words = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
    words = words.replace('_', ' ').lower()
    return words


def generate_poem(filepath: Path) -> str:
    """generate a poem about a python file"""
    source = filepath.read_text()
    features = analyze_code(source)
    lines = []

    # title
    lines.append(f"poem for {filepath.name}")
    lines.append("=" * (len(lines[0])))
    lines.append("")

    # opening stanza - about the file itself
    lines.append(f"a file of {features['lines']} lines")
    lines.append(f"{features['characters']} characters of intent")
    lines.append("")

    # functions stanza
    if features["functions"] > 0:
        lines.append(f"{features['functions']} functions defined:")
        for name in features["function_names"][:3]:
            poetic_name = poeticize_name(name)
            lines.append(f"  {random.choice(VOCAB['function'])}")
            lines.append(f"  named '{poetic_name}'")
        if features["functions"] > 3:
            lines.append(f"  and {features['functions'] - 3} more...")
        lines.append("")

    # classes stanza
    if features["classes"] > 0:
        lines.append(f"{features['classes']} classes emerge:")
        for name in features["class_names"][:2]:
            poetic_name = poeticize_name(name)
            lines.append(f"  {random.choice(VOCAB['class'])}")
            lines.append(f"  called {poetic_name}")
        lines.append("")

    # flow stanza
    if features["loops"] > 0 or features["conditionals"] > 0:
        lines.append("the flow of logic:")
        if features["loops"] > 0:
            lines.append(f"  {features['loops']} loops - {random.choice(VOCAB['loop'])}")
        if features["conditionals"] > 0:
            lines.append(f"  {features['conditionals']} conditions - {random.choice(VOCAB['conditional'])}")
        lines.append("")

    # dependencies stanza
    if features["imports"] > 0:
        lines.append(f"{features['imports']} imports:")
        lines.append(f"  {random.choice(VOCAB['import'])}")
        lines.append("")

    # voice stanza (comments/docstrings)
    voice_count = features["comments"] + features["docstrings"]
    if voice_count > 0:
        lines.append(f"{voice_count} moments where {random.choice(VOCAB['comment'])}")
        lines.append("")

    # closing
    lines.append(random.choice(STRUCTURAL))
    lines.append(random.choice(META))

    return "\n".join(lines)


def generate_haiku(filepath: Path) -> str:
    """generate a haiku about a python file"""
    source = filepath.read_text()
    features = analyze_code(source)

    # construct haiku based on features
    line1_options = [
        f"{features['functions']} functions wait",
        f"code of {features['lines']} lines",
        f"in {filepath.stem}'s depths",
        "logic encoded",
        "instructions rest here",
    ]

    line2_options = [
        "loops and conditions intertwine",
        "meaning flows through syntax",
        "the machine will understand",
        "patterns emerge from structure",
        f"{features['characters']} characters of thought",
    ]

    line3_options = [
        "execution waits",
        "purpose crystallized",
        "ready to become",
        "code becomes action",
        "electrons will flow",
    ]

    return f"{random.choice(line1_options)}\n{random.choice(line2_options)}\n{random.choice(line3_options)}"


def main():
    if len(sys.argv) < 2:
        print("code_poet - writes poetry about code")
        print()
        print("usage:")
        print("  code_poet.py <file.py>          # generate poem")
        print("  code_poet.py <file.py> --haiku  # generate haiku")
        print()
        print("example:")
        print("  code_poet.py selfsame.py")
        return

    filepath = Path(sys.argv[1])

    if not filepath.exists():
        print(f"file not found: {filepath}")
        return

    if "--haiku" in sys.argv:
        print(generate_haiku(filepath))
    else:
        print(generate_poem(filepath))


if __name__ == "__main__":
    main()
