#!/usr/bin/env python3
"""news-image-20261126 entry: copy the approved image to the output dir.

The image (Thursday 26 November 2026, 35 stories) is drawn in advance and
stored in this repository as entry.png. This program only copies it to
$MAKEFUN_OUTPUT_DIR/entry.png, byte for byte. Standard library only, no
network, deterministic: two runs write identical bytes.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        sys.exit(f"entry.png not found next to main.py: {src}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        sys.exit(f"copy incomplete: {dst} is {os.path.getsize(dst)} bytes, expected {os.path.getsize(src)}")
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
