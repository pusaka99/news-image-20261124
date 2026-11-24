"""One-image entry for make.fun news-image-20261124 (Python 3.13, stdlib only).

The entry image is the front page this repository holds (entry.png, drawn
programmatically from the verified news of Tuesday 24 November 2026), and
the program copies it to /output/entry.png. Copying bytes, not re-rendering,
is what makes the two grader runs byte-identical: the file is fixed, the
copy is exact.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def main() -> None:
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB gate")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    if hashlib.sha256(target.read_bytes()).hexdigest() != hashlib.sha256(data).hexdigest():
        raise SystemExit("copied entry.png does not match the repository file")


if __name__ == "__main__":
    main()
