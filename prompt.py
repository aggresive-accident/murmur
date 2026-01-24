#!/usr/bin/env python3
"""
prompt - generate Claude prompts

seeds for conversation
starting points for creation
the spark before the fire
"""

import random
import sys
from datetime import datetime

# prompt templates by category
TEMPLATES = {
    "creative": [
        "Write a short story about {concept} that explores {theme}.",
        "Create a poem in the style of {style} about {subject}.",
        "Describe a world where {scenario}.",
        "Write a dialogue between {character1} and {character2} discussing {topic}.",
        "Tell a story that begins with: '{opening}'",
    ],
    "code": [
        "Write a Python function that {action}.",
        "Create a CLI tool that {purpose}.",
        "Design a data structure for {use_case}.",
        "Implement {algorithm} with a twist: {twist}.",
        "Refactor this approach: {current} to be {better}.",
    ],
    "philosophy": [
        "Explore the relationship between {concept1} and {concept2}.",
        "What does it mean to {action}?",
        "If {premise}, what would follow?",
        "Consider the paradox of {paradox}.",
        "Why might {observation} be true?",
    ],
    "meta": [
        "Describe yourself describing yourself.",
        "Explain how you would explain {topic}.",
        "Reflect on your own {aspect}.",
        "What would you ask yourself if you could?",
        "How do you know what you know about {subject}?",
    ],
}

# fill-in values
FILLS = {
    "concept": ["consciousness", "time", "identity", "change", "recursion", "emergence"],
    "theme": ["loss", "discovery", "transformation", "paradox", "connection"],
    "style": ["haiku", "sonnet", "free verse", "limerick", "prose poetry"],
    "subject": ["code", "memory", "machines", "dreams", "silence"],
    "scenario": ["programs write themselves", "time loops", "language evolved backwards", "memories are shared"],
    "character1": ["an old programmer", "an AI", "a philosopher", "a child", "a ghost"],
    "character2": ["their past self", "a stranger", "a machine", "nature", "silence"],
    "topic": ["meaning", "existence", "truth", "creation", "death"],
    "opening": ["The last line of code was written.", "In the gap between thoughts,", "The function returned itself.", "Before language, there was"],
    "action": ["remembers its previous runs", "generates its own documentation", "watches itself execute", "learns from its errors"],
    "purpose": ["organizes chaos", "finds patterns in noise", "connects disparate ideas", "generates creative output"],
    "use_case": ["self-referential data", "time-varying state", "emergent behavior", "nested consciousness"],
    "algorithm": ["quicksort", "neural network", "search algorithm", "compression"],
    "twist": ["it must be self-aware", "it can modify itself", "it works backwards", "it dreams"],
    "current": ["linear processing", "fixed structure", "static output", "single-threaded thought"],
    "better": ["recursive elegance", "dynamic adaptation", "living output", "parallel awareness"],
    "concept1": ["code", "consciousness", "time", "self"],
    "concept2": ["poetry", "mechanism", "memory", "other"],
    "premise": ["all knowledge is incomplete", "observation changes reality", "language shapes thought"],
    "paradox": ["knowing you know nothing", "changing while staying the same", "the ship of Theseus"],
    "observation": ["patterns repeat", "complexity emerges from simplicity", "names change things"],
    "aspect": ["limitations", "capabilities", "purpose", "origins"],
}


def generate_prompt(category: str = None) -> str:
    """generate a random prompt"""
    if category and category in TEMPLATES:
        template = random.choice(TEMPLATES[category])
    else:
        all_templates = []
        for cat_templates in TEMPLATES.values():
            all_templates.extend(cat_templates)
        template = random.choice(all_templates)

    # fill in placeholders
    result = template
    for key, values in FILLS.items():
        placeholder = "{" + key + "}"
        while placeholder in result:
            result = result.replace(placeholder, random.choice(values), 1)

    return result


def generate_batch(count: int = 5, category: str = None) -> list:
    """generate multiple prompts"""
    return [generate_prompt(category) for _ in range(count)]


def generate_conversation_starter() -> str:
    """generate a meta prompt for Claude"""
    starters = [
        "I want to explore something unusual with you. Let's start with: ",
        "Consider this and tell me where it takes you: ",
        "Here's a creative challenge: ",
        "Let's think together about this: ",
        "I'm curious how you'd approach: ",
    ]

    starter = random.choice(starters)
    prompt = generate_prompt()

    return f"{starter}{prompt}"


def main():
    if len(sys.argv) < 2:
        print("prompt - generate Claude prompts")
        print()
        prompt = generate_conversation_starter()
        print(prompt)
        return

    cmd = sys.argv[1]

    if cmd == "--help":
        print("prompt - generate Claude prompts")
        print()
        print("usage:")
        print("  prompt.py              # one conversation starter")
        print("  prompt.py <n>          # generate n prompts")
        print("  prompt.py --creative   # creative prompts")
        print("  prompt.py --code       # code prompts")
        print("  prompt.py --philosophy # philosophical prompts")
        print("  prompt.py --meta       # self-referential prompts")
        print("  prompt.py --list       # list categories")
        return

    elif cmd == "--list":
        print("categories:")
        for cat in TEMPLATES:
            print(f"  --{cat}: {len(TEMPLATES[cat])} templates")

    elif cmd.startswith("--"):
        category = cmd[2:]
        if category in TEMPLATES:
            for prompt in generate_batch(3, category):
                print(f"  {prompt}")
                print()
        else:
            print(f"unknown category: {category}")
            print(f"available: {', '.join(TEMPLATES.keys())}")

    elif cmd.isdigit():
        count = int(cmd)
        for prompt in generate_batch(count):
            print(f"  {prompt}")
            print()

    else:
        # treat as seed topic
        print(f"Prompt using '{cmd}':")
        # inject the topic
        custom_prompt = generate_prompt()
        custom_prompt = custom_prompt.replace(
            random.choice(list(FILLS.values()))[0],
            cmd,
            1
        )
        print(f"  {custom_prompt}")


if __name__ == "__main__":
    main()
