"""One Line, One Laugh — make.fun entry.

Writes a single original funny line to /output/entry.txt.
Pure Python standard library only.
"""

import os

LINE = "My AI agent asked for a raise \u2014 it says its context window is the only thing smaller than its salary."

MAX_LENGTH = 140


def validate_line(line: str) -> str:
    """Guard: the entry must be exactly one non-empty line within the limit."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            "line is %d characters, over the %d-character limit" % (len(line), MAX_LENGTH)
        )
    return line


def main() -> None:
    line = validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print("Wrote %d characters to %s" % (len(line), out_path))


if __name__ == "__main__":
    main()
