#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Line one warns my past self about one specific moment, in a single
sentence. Line two says in one sentence why that moment mattered and
what changed because of it.
"""

LINE_ONE = (
    "Don't submit the chess engine on the night of 14 November, "
    "while its slowest move still takes more than two seconds."
)

LINE_TWO = (
    "The server graded it zero while my own trials said 1349, "
    "and that zero is why no entry of mine spends a submission "
    "before the check passes."
)


def main():
    print(LINE_ONE)
    print(LINE_TWO)


if __name__ == "__main__":
    main()
