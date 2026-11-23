"""One Word From Grandma — make.fun entry.

The word is "robit": the sweet misspelling a grandma would actually
type when texting her grandchild about a robot. Warm, a little baffled,
and unmistakably about a machine — she means "robot", her thumbs just
got there first.
"""

import os

WORD = "robit"


def main() -> None:
    word = WORD.strip()
    assert word, "word must not be empty"
    assert len(word) <= 30, "word must be at most 30 characters"
    assert not any(ch.isspace() for ch in word), "word must be a single word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
