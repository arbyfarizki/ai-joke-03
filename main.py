"""ai-joke-03 entry (Python 3.13, standard library only).

Writes one joke about AI coding agents to /output/entry.txt.

The joke is fixed text, so the program is deterministic: two runs write
the same bytes. No network, no randomness, no wall clock.
Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
  MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

JOKE = "My AI coding agent said 'Done!' The code doesn't run — but the confidence is production-ready."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
