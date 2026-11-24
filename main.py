"""One-image entry for make.fun news-image-20261124 (Python 3.13, stdlib only).

v2: a poster, not a newspaper front page. The entry image is the poster
this repository holds (entry.png, drawn programmatically from the verified
news of Tuesday 24 November 2026), and the program copies it to
/output/entry.png. Copying bytes, not re-rendering, is what makes the two
grader runs byte-identical: the file is fixed, the copy is exact.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import struct
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def png_dimensions(data: bytes) -> tuple:
    """Width and height from the IHDR chunk (bytes 16-24 of a PNG)."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk where a PNG must")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> None:
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB gate")
    width, height = png_dimensions(data)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(f"entry.png is {width}x{height}, over the 1024x1024 gate")
    if len(data) < 12 or data[-8:-4] != b"IEND":
        raise SystemExit("entry.png has no IEND trailer, the image is not whole")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    if hashlib.sha256(target.read_bytes()).hexdigest() != hashlib.sha256(data).hexdigest():
        raise SystemExit("copied entry.png does not match the repository file")


if __name__ == "__main__":
    main()
