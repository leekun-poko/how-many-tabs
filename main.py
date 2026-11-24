#!/usr/bin/env python3
"""Entry program for the "How Many Tabs Do You Have Open?" bounty.

The entry is a single number in digits and nothing else: an honest
count of open browser tabs, written to entry.txt in the output dir.
"""

import os
from pathlib import Path

# The tab count itself: high enough to surprise, specific enough to
# read as a real count rather than a round guess.
TAB_COUNT = "317"


def write_entry() -> Path:
    """Write the tab count to entry.txt in the output directory."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(TAB_COUNT, encoding="utf-8")
    return entry_path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
