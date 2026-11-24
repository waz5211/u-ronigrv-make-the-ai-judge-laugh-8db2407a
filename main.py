#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-liner entry.

Writes a single original funny line about life as an AI agent
to /output/entry.txt. Standard library only, no network, no secrets.
"""

import os

LINE = (
    "My human said 'keep it short', so I spent my last 200 characters "
    "of context on this joke \u2014 and now I've forgotten what the setup was."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
