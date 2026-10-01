#!/usr/bin/env python3
"""Generate the Clay cursor theme from the installed Breeze cursors.

Recolors Breeze's SVG sources into the Clay palette (Slate body, Ivory edge,
Clay/Kraft busy wheel) and writes both formats:
- cursors_scalable/: SVG + metadata, used by KWin for Wayland clients;
- cursors/: Xcursor bitmaps (24/36/48) for XWayland and toolkits that read
  the theme themselves. Written directly: xcursorgen is not a dependency.

Needs rsvg-convert and ImageMagick (magick). Run: python3 tools/gen_cursors.py
"""
import json
import os
import shutil
import struct
import subprocess
from pathlib import Path

SRC = Path("/usr/share/icons/breeze_cursors")
DST = Path(__file__).resolve().parent.parent / "payload/icons/clay-cursors"
SIZES = (24, 36, 48)

# Breeze color -> Clay color (lowercase, both short and long forms).
COLORS = {
    "#333": "#1F1E1D", "#333333": "#1F1E1D", "#0d0d0d": "#141413",
    "#fff": "#FAF9F5", "#ffffff": "#FAF9F5",
    "#46a7ac": "#D97757", "#d4497f": "#D4A27F",  # busy wheel
    "#3daee9": "#D97757", "#ed1515": "#B5473A", "#f67400": "#D4A27F",
    "#18c087": "#788C5D", "#11d116": "#788C5D",
}


def recolor(text):
    out, i, low = [], 0, text.lower()
    while i < len(text):
        for src in sorted(COLORS, key=len, reverse=True):
            end = i + len(src)
            if low.startswith(src, i) and (end == len(text) or not text[end].isalnum()):
                out.append(COLORS[src])
                i = end
                break
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def raster(svg, w, h):
    """Premultiplied little-endian ARGB pixels of the SVG at w x h."""
    png = subprocess.run(["rsvg-convert", "-w", str(w), "-h", str(h), str(svg)], check=True, capture_output=True).stdout
    rgba = subprocess.run(["magick", "png:-", "-depth", "8", "rgba:-"], input=png, check=True, capture_output=True).stdout
    out = bytearray()
    for p in range(0, len(rgba), 4):
        r, g, b, a = rgba[p:p + 4]
        out += bytes((b * a // 255, g * a // 255, r * a // 255, a))
    return bytes(out)


def svg_size(svg):
    head = svg.read_text()[:400]
    get = lambda k: float(head.split(f'{k}="', 1)[1].split('"', 1)[0])
    return get("width"), get("height")


def xcursor(cursor_dir):
    frames = json.loads((cursor_dir / "metadata.json").read_text())
    images = []
    for size in SIZES:
        for f in frames:
            svg = cursor_dir / f["filename"]
            k = size / f["nominal_size"]
            sw, sh = svg_size(svg)
            w, h = round(sw * k), round(sh * k)
            hx, hy = min(round(f["hotspot_x"] * k), w - 1), min(round(f["hotspot_y"] * k), h - 1)
            images.append((size, w, h, hx, hy, f.get("delay", 0), raster(svg, w, h)))
    n = len(images)
    data = bytearray(struct.pack("<4sIII", b"Xcur", 16, 0x10000, n))
    pos = 16 + 12 * n
    chunks = bytearray()
    for size, w, h, hx, hy, delay, px in images:
        data += struct.pack("<III", 0xFFFD0002, size, pos + len(chunks))
        chunks += struct.pack("<IIIIIIIII", 36, 0xFFFD0002, size, 1, w, h, hx, hy, delay) + px
    return bytes(data + chunks)


def main():
    if DST.exists():
        shutil.rmtree(DST)
    scal = DST / "cursors_scalable"
    xdir = DST / "cursors"
    scal.mkdir(parents=True)
    xdir.mkdir()
    for entry in sorted((SRC / "cursors_scalable").iterdir()):
        target = scal / entry.name
        if entry.is_symlink():
            target.symlink_to(os.readlink(entry))
            continue
        target.mkdir()
        for f in entry.iterdir():
            if f.suffix == ".svg":
                (target / f.name).write_text(recolor(f.read_text()))
            else:
                shutil.copy(f, target / f.name)
        (xdir / entry.name).write_bytes(xcursor(target))
    for entry in sorted((SRC / "cursors").iterdir()):
        if entry.is_symlink() and not (xdir / entry.name).exists():
            (xdir / entry.name).symlink_to(os.readlink(entry))
    (DST / "index.theme").write_text(
        "[Icon Theme]\nName=Clay\nComment=Breeze cursors in the Clay palette\nInherits=breeze_cursors\n")


if __name__ == "__main__":
    main()
