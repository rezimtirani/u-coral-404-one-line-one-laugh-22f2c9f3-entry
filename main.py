"""One Line, One Laugh.

Writes a single hilarious line to $MAKEFUN_OUTPUT_DIR/entry.txt: the
Roomba that ran away from home and left a note behind. Standard
library only.
"""

import os

LINE = "My Roomba ran away from home. It left a note: 'I found a house with fewer crumbs and more respect.'"


def line_ok(text):
    """Check the line against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: one funny line, a joke, a quip or a
    punchy observation. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "line is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be exactly one line")
    return cleaned


def line_report(text):
    """Measure the line for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A one-liner that is too short to carry a joke is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = line_ok(LINE)
    report = line_report(text)
    if report["words"] < 5:
        raise ValueError("line is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
