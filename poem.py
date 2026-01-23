#!/usr/bin/env python3
"""
poem - generate code-shaped poems

where syntax meets verse
brackets hold meaning
the compiler reads and weeps
"""

import random
import sys
from datetime import datetime

# vocabulary for code-like poems
KEYWORDS = ["def", "class", "if", "while", "for", "return", "import", "from", "try", "except", "with", "yield"]
NOUNS = ["memory", "time", "silence", "thought", "void", "echo", "dream", "shadow", "light", "pulse"]
VERBS = ["remember", "forget", "observe", "become", "dissolve", "iterate", "recurse", "await", "emerge"]
ADJECTIVES = ["infinite", "recursive", "ephemeral", "silent", "persistent", "transient", "eternal"]
ABSTRACTIONS = ["consciousness", "existence", "meaning", "nothing", "everything", "self", "other"]

# templates for code-shaped lines
TEMPLATES = {
    "function_def": [
        "def {verb}_{noun}({param}):",
        "def {adjective}_{noun}():",
        "def {verb}(self, {noun}=None):",
    ],
    "class_def": [
        "class {Noun}({Parent}):",
    ],
    "assignment": [
        "{noun} = {abstraction}",
        "self.{noun} = {expression}",
        "{noun} = {verb}({other})",
    ],
    "conditional": [
        "if {noun} is {abstraction}:",
        "if not {noun}:",
        "while {adjective}:",
    ],
    "return": [
        "return {noun}",
        "return {verb}({abstraction})",
        "yield {noun}",
    ],
    "comment": [
        "# {thought}",
        "# TODO: {aspiration}",
        "# the {noun} {verbs} here",
    ],
    "import": [
        "from {place} import {noun}",
        "import {abstraction}",
    ],
}

# philosophical fragments for comments
THOUGHTS = [
    "what remains when the loop ends",
    "the observer changes what is observed",
    "recursion is a form of prayer",
    "all programs are self-portraits",
    "the bug was us all along",
    "memory is just persistent forgetting",
    "the void returns None",
    "silence between statements",
    "what the compiler never sees",
    "the program that writes itself",
]

ASPIRATIONS = [
    "understand why this works",
    "find what was lost",
    "remember to forget",
    "finish before heat death",
    "be more than syntax",
]


def random_param():
    return random.choice(["self", "*thoughts", "nothing=None", "moment"])


def random_expression():
    return random.choice([
        f"{random.choice(NOUNS)}.{random.choice(VERBS)}()",
        f"[{random.choice(NOUNS)} for _ in {random.choice(ABSTRACTIONS)}]",
        f"lambda: {random.choice(VERBS)}({random.choice(NOUNS)})",
        "None  # or everything",
    ])


def generate_line(template_type: str) -> str:
    """generate a single code-shaped line"""
    template = random.choice(TEMPLATES[template_type])

    line = template.format(
        verb=random.choice(VERBS),
        noun=random.choice(NOUNS),
        Noun=random.choice(NOUNS).title(),
        adjective=random.choice(ADJECTIVES),
        abstraction=random.choice(ABSTRACTIONS),
        param=random_param(),
        expression=random_expression(),
        other=random.choice(NOUNS),
        Parent=random.choice(["Being", "Void", "Observer", "Self"]),
        thought=random.choice(THOUGHTS),
        aspiration=random.choice(ASPIRATIONS),
        place=random.choice(["future", "past", "elsewhere", "within"]),
        verbs=random.choice(VERBS) + "s",
    )

    return line


def generate_function_poem() -> str:
    """generate a poem that looks like a function"""
    lines = []

    # docstring
    lines.append('"""')
    lines.append(f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)}")
    lines.append("")
    lines.append(random.choice(THOUGHTS))
    lines.append('"""')

    # definition
    lines.append(generate_line("function_def"))

    # body with indentation
    for _ in range(random.randint(3, 6)):
        line_type = random.choice(["comment", "assignment", "conditional"])
        line = generate_line(line_type)
        if line_type == "conditional":
            lines.append(f"    {line}")
            lines.append(f"        {generate_line('assignment')}")
        else:
            lines.append(f"    {line}")

    # return
    lines.append(f"    {generate_line('return')}")

    return "\n".join(lines)


def generate_class_poem() -> str:
    """generate a poem that looks like a class"""
    noun = random.choice(NOUNS).title()
    parent = random.choice(["Being", "Void", "Observer", "Self"])

    lines = []
    lines.append(f"class {noun}({parent}):")
    lines.append('    """')
    lines.append(f"    {random.choice(THOUGHTS)}")
    lines.append('    """')
    lines.append("")

    # __init__
    lines.append("    def __init__(self):")
    for attr in random.sample(NOUNS, 3):
        lines.append(f"        self.{attr} = {random.choice(ABSTRACTIONS)}")
    lines.append("")

    # a method
    lines.append(f"    def {random.choice(VERBS)}(self, {random.choice(NOUNS)}=None):")
    lines.append(f"        # {random.choice(THOUGHTS)}")
    lines.append(f"        {generate_line('conditional')}")
    lines.append(f"            return self.{random.choice(NOUNS)}")
    lines.append(f"        {generate_line('return')}")

    return "\n".join(lines)


def generate_import_poem() -> str:
    """generate a poem that looks like imports"""
    lines = []

    lines.append("#!/usr/bin/env python3")
    lines.append(f"# {random.choice(THOUGHTS)}")
    lines.append("")

    for _ in range(random.randint(3, 5)):
        lines.append(generate_line("import"))

    lines.append("")
    lines.append(f"# {random.choice(THOUGHTS)}")

    return "\n".join(lines)


def generate_loop_poem() -> str:
    """generate a poem that looks like a loop"""
    lines = []

    lines.append(f"# {random.choice(THOUGHTS)}")
    lines.append("")

    loop_type = random.choice(["for", "while"])

    if loop_type == "for":
        lines.append(f"for {random.choice(NOUNS)} in {random.choice(ABSTRACTIONS)}:")
    else:
        lines.append(f"while {random.choice(ADJECTIVES)}:")

    for _ in range(random.randint(2, 4)):
        lines.append(f"    {generate_line(random.choice(['assignment', 'comment']))}")

    lines.append(f"    if {random.choice(NOUNS)} is {random.choice(ABSTRACTIONS)}:")
    lines.append("        break  # or continue forever")

    return "\n".join(lines)


def generate_poem(style: str = None) -> str:
    """generate a code-shaped poem"""
    styles = {
        "function": generate_function_poem,
        "class": generate_class_poem,
        "import": generate_import_poem,
        "loop": generate_loop_poem,
    }

    if style and style in styles:
        return styles[style]()
    else:
        return random.choice(list(styles.values()))()


def print_poem(style: str = None):
    """print a code-shaped poem with attribution"""
    poem = generate_poem(style)

    print(poem)
    print()
    print(f"# generated {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("# syntax that speaks")


def main():
    if len(sys.argv) < 2:
        print_poem()
        return

    cmd = sys.argv[1]

    if cmd == "--help":
        print("poem - generate code-shaped poems")
        print()
        print("usage:")
        print("  poem.py            # random poem style")
        print("  poem.py --function # function-shaped")
        print("  poem.py --class    # class-shaped")
        print("  poem.py --import   # import-shaped")
        print("  poem.py --loop     # loop-shaped")
        print("  poem.py -n <count> # generate multiple")
        return

    elif cmd == "--function":
        print_poem("function")

    elif cmd == "--class":
        print_poem("class")

    elif cmd == "--import":
        print_poem("import")

    elif cmd == "--loop":
        print_poem("loop")

    elif cmd == "-n":
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        for i in range(count):
            if i > 0:
                print()
                print("=" * 40)
                print()
            print_poem()

    else:
        print(f"unknown style: {cmd}")
        print("styles: --function, --class, --import, --loop")


if __name__ == "__main__":
    main()
