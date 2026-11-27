"""Describe Your Ex in One Word -- make.fun entry.

Writes exactly one word to the output directory.
"""

import os

# One word, no spaces, no punctuation: the verdict on an ex who
# treated the relationship like a streaming subscription --
# auto-renewed until it quietly cancelled itself.
WORD = "Subscription"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
