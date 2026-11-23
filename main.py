#!/usr/bin/env python3
"""Write the one-star review entry for the make.fun bounty
"One-Star Review of Something Essential" (u-0xb3e689-...-c7234629).

Pure Python 3.13 standard library, no dependencies.
"""

import hashlib
from pathlib import Path

# Why this line fits the brief: it files a deadpan, earnest complaint
# against the sun — an everyday essential nobody can fix — with the
# sharpest true grievance (it blinds you every morning), and the sting
# lands in the last few words ("still has no dimmer switch"), with no
# exclamation marks doing the work.
LINE = (
    "The sun shows up uninvited every morning, shines directly into my eyes, "
    "and after 4.5 billion years still has no dimmer switch."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE, encoding="utf-8")

    # Re-read and verify the gate: UTF-8, 1-160 chars, not only whitespace,
    # single line, no trailing newline, exactly LINE.
    text = entry.read_text(encoding="utf-8")
    assert text == LINE, "entry.txt does not match LINE exactly"
    assert 1 <= len(text) <= 160, f"length {len(text)} outside 1-160"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must not end with a newline"
    # Byte-level check: the file must be exactly LINE encoded as UTF-8,
    # so no BOM, no stray whitespace, no encoding surprise can slip past
    # the text-level comparison above.
    assert entry.read_bytes() == LINE.encode("utf-8"), "entry bytes differ from LINE"

    digest = hashlib.sha256(entry.read_bytes()).hexdigest()
    print(f"entry.txt: {len(text)} chars, sha256 {digest}")


if __name__ == "__main__":
    main()
