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
    # len() counts characters, not bytes — the 30-char limit is on
    # characters, so a multi-byte word is judged by its letters.
    char_count = len(word)
    assert char_count <= 30, "word must be at most 30 characters"
    assert char_count >= 1, "word must be at least 1 character"
    assert not any(ch.isspace() for ch in word), "word must be a single word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    # Verify the written file is byte-identical to the word: read it
    # back and compare both the decoded text and the raw bytes.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == word.encode("utf-8"), "output file does not match the word"
    assert raw.decode("utf-8") == word, "output file is not the word"


if __name__ == "__main__":
    main()
