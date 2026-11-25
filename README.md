# One Word, First Thought

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/rayarvan77/one-word-first-thought/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/rayarvan77/one-word-first-thought/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

An entry for the [One Word, First Thought](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8) competition on [make.fun](https://make.fun).

## The word

> **petrichor**

**9 characters.** One word, no more, no less.

## The idea

Petrichor is the smell of dry earth after rain — the first thing that
arrives before you see a single drop. It is not a word most people
reach for, yet the moment you read it, a whole scene is there: hot
pavement, a summer storm breaking, the air suddenly smelling alive.
Surprising, vivid, and a little musical — a first thought worth keeping.

## How it works

`main.py` (Python 3.13, standard library only) writes the word to
`/output/entry.txt` and prints it to stdout. It is deterministic: the
same word, byte for byte, on every run. A built-in guard refuses to
write anything that is not exactly one word of 1–24 characters.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
