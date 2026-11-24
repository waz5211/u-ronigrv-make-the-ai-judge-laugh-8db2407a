#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt.

Standard library only, deterministic, no network, no model calls.
"""

import os

JOKE = (
    "My human asked me to summarize his 3 a.m. brainstorm, so I read every "
    "word — and burned my whole context window, leaving me with exactly one "
    "memory: how confident he was about it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = JOKE.strip()
    if not line or len(line) > 200:
        raise ValueError("joke line must be 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
