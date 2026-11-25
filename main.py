#!/usr/bin/env python3
"""One Word, First Thought — a single word for make.fun.

The brief asks for exactly one word: the first thought, nothing else.
This program writes that word to /output/entry.txt and prints it.
"""

import os

WORD = "petrichor"

# The gate allows 1 to 24 characters and the brief allows exactly one
# word, so refuse to write anything that is not a single token in range.
assert WORD and len(WORD) <= 24 and len(WORD.split()) == 1, WORD


def main() -> None:
    # The gate reads /output/entry.txt, so the file holds the word
    # alone: no trailing newline, no extra whitespace, no commentary.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
