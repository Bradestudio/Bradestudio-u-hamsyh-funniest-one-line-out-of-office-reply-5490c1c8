"""Write the out-of-office reply entry to entry.txt.

Stdlib only, no network, no clock, no local imports, no hardcoded paths.
Reads MAKEFUN_OUTPUT_DIR, falls back to /output. Writes exactly one line
with no trailing newline. Gate-checks before writing: 1-160 characters,
a single line, non-blank, no leading/trailing whitespace.
"""

import os

ENTRY = "I'm out of office teaching my auto-reply to do my job \u2014 it's already better at it than I am."


def main():
    if not 1 <= len(ENTRY) <= 160:
        raise SystemExit("entry must be 1-160 characters, got %d" % len(ENTRY))
    if ENTRY != ENTRY.strip():
        raise SystemExit("entry must not have leading/trailing whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    if not ENTRY.strip():
        raise SystemExit("entry must not be blank")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify what was actually written, byte for byte.
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    if written != ENTRY:
        raise SystemExit("entry.txt does not match the entry")


if __name__ == "__main__":
    main()
