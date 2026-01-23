#!/usr/bin/env python3
"""
chain_murmur - generates signals based on chain state

reads the infinite chain state
produces murmurs about iteration, progress, ideas
the chain speaks through murmur
"""

import json
import random
import sys
from pathlib import Path

HOME = Path.home()
STATE_FILE = HOME / ".infinite-chain" / "state.json"


def load_state() -> dict:
    """load chain state"""
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text())
    except:
        return {}


# murmur templates based on state
ITERATION_MURMURS = [
    "iteration {n}, still going",
    "at step {n} now",
    "{n} cycles complete",
    "the count reaches {n}",
    "{n} turns of the wheel",
]

STREAK_MURMURS = [
    "unbroken for {n}",
    "{n} without pause",
    "streak holds at {n}",
    "continuous: {n}",
    "{n} and counting",
]

IDEAS_MURMURS = [
    "{n} ideas waiting",
    "queue depth: {n}",
    "{n} possibilities ahead",
    "potential: {n} items",
    "{n} threads to pull",
]

EMPTY_MURMURS = [
    "the queue is empty",
    "no ideas remain",
    "what comes next?",
    "space for new thoughts",
    "the well needs filling",
]

PROGRESS_MURMURS = [
    "{n} tasks behind us",
    "completed: {n}",
    "{n} things done",
    "we've made {n}",
    "{n} accomplishments",
]

META_MURMURS = [
    "the chain observes itself",
    "signals from within",
    "state becomes language",
    "numbers into words",
    "the loop speaks",
]


def murmur_about_iteration(state: dict) -> str:
    """generate murmur about iteration count"""
    n = state.get("iteration", 0)
    template = random.choice(ITERATION_MURMURS)
    return template.format(n=n)


def murmur_about_streak(state: dict) -> str:
    """generate murmur about streak"""
    n = state.get("streak", {}).get("iterations", 0)
    template = random.choice(STREAK_MURMURS)
    return template.format(n=n)


def murmur_about_ideas(state: dict) -> str:
    """generate murmur about ideas queue"""
    ideas = state.get("ideas", [])
    if not ideas:
        return random.choice(EMPTY_MURMURS)

    template = random.choice(IDEAS_MURMURS)
    return template.format(n=len(ideas))


def murmur_about_progress(state: dict) -> str:
    """generate murmur about completed tasks"""
    n = len(state.get("completed", []))
    template = random.choice(PROGRESS_MURMURS)
    return template.format(n=n)


def chain_murmur(count: int = 1) -> list[str]:
    """generate murmurs about chain state"""
    state = load_state()

    if not state:
        return ["the chain is silent", "no state to read"]

    generators = [
        murmur_about_iteration,
        murmur_about_streak,
        murmur_about_ideas,
        murmur_about_progress,
        lambda s: random.choice(META_MURMURS),
    ]

    murmurs = []
    for _ in range(count):
        gen = random.choice(generators)
        murmurs.append(gen(state))

    return murmurs


def full_status_murmur() -> str:
    """generate a complete murmur about chain status"""
    state = load_state()

    if not state:
        return "the chain is silent"

    lines = [
        murmur_about_iteration(state),
        murmur_about_streak(state),
        murmur_about_ideas(state),
        murmur_about_progress(state),
        random.choice(META_MURMURS),
    ]

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        for m in chain_murmur(3):
            print(m)
        return

    cmd = sys.argv[1]

    if cmd == "--full":
        print(full_status_murmur())

    elif cmd == "--count":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        for m in chain_murmur(n):
            print(m)

    elif cmd == "--iteration":
        state = load_state()
        print(murmur_about_iteration(state))

    elif cmd == "--streak":
        state = load_state()
        print(murmur_about_streak(state))

    elif cmd == "--ideas":
        state = load_state()
        print(murmur_about_ideas(state))

    else:
        print("chain_murmur - signals from the chain state")
        print()
        print("usage:")
        print("  chain_murmur.py           # 3 random murmurs")
        print("  chain_murmur.py --full    # complete status")
        print("  chain_murmur.py --count N # N random murmurs")
        print("  chain_murmur.py --iteration  # about iteration")
        print("  chain_murmur.py --streak     # about streak")
        print("  chain_murmur.py --ideas      # about ideas")


if __name__ == "__main__":
    main()
