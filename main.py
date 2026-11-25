"""Funniest One-Line Out-of-Office Reply.

make.fun bounty u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.

Design: the entry is one fixed line of plain text -- a deadpan
out-of-office auto-reply. The line was chosen by a local tournament over
20 freshly written candidates, judged against the bounty judge's own brief
(a real one-line away message first, then a laugh that lands on the first
read, then a message a person would gladly switch on, then freshness
against the usual beach / inbox / limited-email lines, then brevity).
The winner is a single clean punch: the office has not noticed the
absence yet. No setup, nothing to explain afterwards, 58 characters.

The program is deliberately boring: no input, no randomness, no network,
no clock, no files read. It writes the single winning line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output/entry.txt`` when the variable
is unset), so two runs are byte-identical by construction.
"""

import os

# The winning line (58 characters, one line, plain UTF-8 text).
# Chosen by the local tournament in ../CANDIDATES.md (playoff record 3-0).
# Verified byte-identical across two runs in a clean read-only dir:
# sha256 f9e97dc9d2174f10ee9e1eeb88b449b7cbc4de62e442816d042c40a2a2ef362d.
ENTRY = "I'm out of the office, and the office has not noticed yet."


def main() -> int:
    # Gate self-check: the sealed scorer only accepts 1-160 characters.
    if not 1 <= len(ENTRY) <= 160 or not ENTRY.strip() or "\n" in ENTRY:
        raise SystemExit("entry violates the 1-160 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
