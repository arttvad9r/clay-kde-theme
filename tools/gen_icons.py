#!/usr/bin/env python3
"""Generate the full-color part of clay-icons.

Design language: matte, opaque paper shapes, no outlines, Anthropic-style
restraint. Folders are manilla paper on a kraft back with clay glyphs; physical
objects (trash, drives) are warm neutral grey; system apps are slate tiles.
Clay is an accent only. Colors are opaque so an icon looks the same on Light
and Dark surfaces.

16 and 22 px folders use their own pixel grids; everything else is drawn on a
32 grid and scaled. Symbolic/action icons are hand-made and not touched here.

Run from anywhere: python3 tools/gen_icons.py
"""
import os
from pathlib import Path

ROOT = Path(os.environ.get("CLAY_ICONS_ROOT") or Path(__file__).resolve().parent.parent / "payload/icons/clay-icons")

# Anthropic palette names.
CLAY = "#D97757"
CLAY_DEEP = "#C6613F"
KRAFT = "#D4A27F"
MANILLA = "#EBDBBC"
IVORY = "#FAF9F5"
GREY_L = "#D1CFC5"
GREY = "#B0AEA5"
GREY_D = "#87867F"
GLYPH = CLAY_DEEP
SLATE_SOFT = "#3D3D3A"
SKY = "#6A9BCC"
OLIVE = "#788C5D"
FIG = "#C46686"
HEATHER_D = "#8580AE"
KRAFT_D = "#B0835E"
PAPER = IVORY
PAPER_EDGE = "#D1CFC5"
PAPER_FOLD = "#E3DACC"
CARD = IVORY
CARD_EDGE = "#D1CFC5"

# Folder geometry per grid: back, tab, sheet, front as (x, y, w, h, r);
# glyph box as (cx, cy, size, stroke-in-grid-units).
FOLDER = {
    16: dict(back=(1, 3, 14, 11.5, 1.6), tab=(1, 2, 6, 3, 1.1), sheet=(2, 4, 12, 4, .8),
             front=(1, 6, 14, 8.5, 1.6), glyph=(8, 10.25, 6, 1.05)),
    22: dict(back=(1, 4, 20, 15, 2), tab=(1, 3, 8.5, 4, 1.5), sheet=(2.5, 5.5, 17, 5, 1),
             front=(1, 8, 20, 11, 2), glyph=(11, 13.5, 8, 1.3)),
    32: dict(back=(3, 7.5, 26, 19.5, 2.6), tab=(3, 5, 11, 5, 2), sheet=(5, 9, 22, 8, 1.4),
             front=(3, 11.5, 26, 15.5, 2.6), glyph=(16, 19.25, 11.5, 1.7)),
}

# Glyphs on a 24-unit box. "s" = stroked, "f" = filled, "e" = even-odd fill.
GLYPHS = {
    "documents": [("s", "M6 6.5h12M6 12h12M6 17.5h8")],
    "download": [("s", "M12 3.5v12M6.5 10l5.5 5.5 5.5-5.5M5.5 20.5h13")],
    "images": [("f", '<circle cx="16.5" cy="7.5" r="2.8"/>'),
               ("f", '<path d="M2.5 20.5 9 11.5l4.8 5.8 3-3.4 4.7 6.6z"/>')],
    "music": [("f", '<circle cx="7" cy="17.8" r="3.4"/><circle cx="17.5" cy="15.8" r="3.4"/>'),
              ("s", "M10.2 17.8V5.6l10.5-2.4v12.6")],
    "videos": [("f", '<path d="M7.5 4.8v14.4a.8.8 0 0 0 1.2.7l11.2-7.2a.8.8 0 0 0 0-1.4L8.7 4.1a.8.8 0 0 0-1.2.7z"/>')],
    "desktop": [("s", "M5.5 4.5h13a2 2 0 0 1 2 2v7.5a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2V6.5a2 2 0 0 1 2-2zM8.5 20.5h7M12 16v4.5")],
    "publicshare": [("f", '<circle cx="6" cy="12" r="3"/><circle cx="18" cy="5.5" r="3"/><circle cx="18" cy="18.5" r="3"/>'),
                    ("s", "M6 12 18 5.5M6 12l12 6.5")],
    "templates": [("f", '<rect x="3.5" y="3.5" width="7.5" height="7.5" rx="1.8"/><rect x="13" y="3.5" width="7.5" height="7.5" rx="1.8"/>'
                        '<rect x="3.5" y="13" width="7.5" height="7.5" rx="1.8"/><rect x="13" y="13" width="7.5" height="7.5" rx="1.8"/>')],
    "home": [("e", '<path d="M12 3 2.8 11.2h2.7v9.3h13v-9.3h2.7zM10 20.5v-5.5h4v5.5z"/>')],
    "network": [("f", '<circle cx="12" cy="5" r="3"/><circle cx="5" cy="18.5" r="3"/><circle cx="19" cy="18.5" r="3"/>'),
                ("s", "M12 5 5 18.5h14z")],
    "recent": [("s", "M12 3.5a8.5 8.5 0 1 1 0 17 8.5 8.5 0 0 1 0-17zM12 7.5V12l3.2 2.2")],
    "code": [("s", "M8 6.5 2.5 12 8 17.5M16 6.5l5.5 5.5-5.5 5.5M13.6 4.5l-3.2 15")],
    "lines": [("s", "M5 7h14M5 12h14M5 17h9")],
    "script": [("s", "M4.5 6.5 10 12l-5.5 5.5M12.5 18.5h7")],
    "play": [("f", '<path d="M7 4.3v15.4a.9.9 0 0 0 1.4.75l12-7.7a.9.9 0 0 0 0-1.5l-12-7.7A.9.9 0 0 0 7 4.3z"/>')],
    "archive": [("s", "M4 9h16v10a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 19zM2.8 4.5h18.4V9H2.8zM9.5 13h5")],
    "pdf": [("s", "M5 4.5h14M5 9h14", "#87867F"), ("f", '<rect x="4" y="13.5" width="16" height="7" rx="1.8"/>')],
    "sheet": [("s", "M5 4h14a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zM4 9.3h16M4 14.6h16M10 4v16")],
    "slides": [("s", "M4.5 4h15a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1h-15a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zM12 16v4.5M8.5 20.5h7"),
               ("f", '<rect x="7" y="7.5" width="6" height="5" rx="1"/>')],
    "cube": [("s", "M12 2.8 20 7.3v9.4L12 21.2l-8-4.5V7.3zM4 7.3l8 4.5 8-4.5M12 11.8v9.4")],
    "font": [("s", "M5.5 20.5 12 3.5l6.5 17M8 14h8")],
    "disc": [("s", "M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18z"), ("f", '<circle cx="12" cy="12" r="2.6"/>')],
}

FOLDERS = {
    "folder": None,
    "folder-documents": "documents",
    "folder-download": "download",
    "folder-images": "images",
    "folder-music": "music",
    "folder-videos": "videos",
    "folder-publicshare": "publicshare",
    "folder-templates": "templates",
    "folder-network": "network",
    "folder-recent": "recent",
    "folder-development": "code",
    "user-desktop": "desktop",
    "user-home": "home",
    "network-workgroup": "network",
}
FOLDER_ALIASES = {
    "folder-open": "folder", "folder-pictures": "folder-images", "folder-picture": "folder-images",
    "folder-image": "folder-images", "folder-downloads": "folder-download", "folder-public": "folder-publicshare",
    "folder-video": "folder-videos", "folder-sound": "folder-music", "folder-remote": "folder-network",
    "desktop": "user-desktop", "folder-projects": "folder-development", "folder-code": "folder-development",
}


def svg(grid, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {grid} {grid}">\n{body}</svg>\n'


def rect(x, y, w, h, r, fill, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{extra}/>\n'


def glyph(name, cx, cy, size, stroke, base_color=GLYPH):
    k = size / 24
    sw = round(stroke / k, 3)
    out = [f'<g transform="translate({cx - size / 2:g} {cy - size / 2:g}) scale({k:g})">\n']
    for part in GLYPHS[name]:
        kind, data = part[:2]
        color = part[2] if len(part) > 2 else base_color
        if kind == "s":
            out.append(f'<path d="{data}" fill="none" stroke="{color}" stroke-width="{sw}" '
                       f'stroke-linecap="round" stroke-linejoin="round"/>\n')
        elif kind == "e":
            out.append(f'<g fill="{color}" fill-rule="evenodd">{data}</g>\n')
        else:
            out.append(f'<g fill="{color}">{data}</g>\n')
    out.append("</g>\n")
    return "".join(out)


def folder(grid, g):
    f = FOLDER[grid]
    body = rect(*f["back"], KRAFT) + rect(*f["tab"], KRAFT) + rect(*f["sheet"], IVORY) + rect(*f["front"], MANILLA)
    if g:
        body += glyph(g, *f["glyph"])
    return svg(grid, body)


def trash(full):
    body = ""
    if full:
        # Full: a clay sheet sticks out instead of the handle.
        body += f'<rect x="10.5" y="1.8" width="11" height="8" rx="1.4" fill="{CLAY}" transform="rotate(-9 16 5.8)"/>\n'
    else:
        body += f'<path d="M13 7V5.6a1.2 1.2 0 0 1 1.2-1.2h3.6A1.2 1.2 0 0 1 19 5.6V7" fill="none" stroke="{GREY_D}" stroke-width="1.6"/>\n'
    body += (rect(6.5, 7, 19, 3, 1.5, GREY_D)
             + f'<path d="M8.2 11.5h15.6l-1.3 14.3a2.2 2.2 0 0 1-2.2 2H11.7a2.2 2.2 0 0 1-2.2-2z" fill="{GREY}"/>\n'
             + f'<path d="M12.6 15v8.8M16 15v8.8M19.4 15v8.8" stroke="{GREY_L}" stroke-width="1.5" stroke-linecap="round"/>\n')
    return svg(32, body)


def drive(root=False):
    body = (rect(3.5, 8, 25, 16, 3.2, GREY)
            + f'<path d="M3.5 17.5h25v3.3a3.2 3.2 0 0 1-3.2 3.2H6.7a3.2 3.2 0 0 1-3.2-3.2z" fill="{GREY_D}"/>\n'
            + f'<path d="M8 20.8h8" stroke="{GREY_L}" stroke-width="1.4" stroke-linecap="round"/>\n'
            + f'<circle cx="23.8" cy="20.8" r="1.5" fill="{CLAY}"/>\n')
    if root:
        body += f'<path d="M14 15l4-5" stroke="{IVORY}" stroke-width="1.6" stroke-linecap="round"/>\n'
    return svg(32, body)


def usb():
    return svg(32, rect(11, 3.5, 10, 7.5, 1.2, GREY_L)
               + rect(13.2, 5.5, 2, 2, .4, GREY_D) + rect(16.8, 5.5, 2, 2, .4, GREY_D)
               + rect(8.5, 10, 15, 18.5, 3, GREY)
               + f'<circle cx="16" cy="23.5" r="1.6" fill="{CLAY}"/>\n')


def sdcard():
    return svg(32, f'<path d="M10.2 3.5h9.6l5.7 5.7v16.3a3 3 0 0 1-3 3h-12.5a3 3 0 0 1-3-3V6.7a3.2 3.2 0 0 1 3.2-3.2z" fill="{GREY}"/>\n'
               + f'<path d="M11 5.8v4.2M14 5.8v4.2M17 5.8v4.2M20 5.8v4.2" stroke="{GREY_L}" stroke-width="1.5" stroke-linecap="round"/>\n'
               + rect(9.5, 16, 13, 8, 1.6, CLAY))


def server():
    body = ""
    for y in (5, 17.5):
        body += (rect(4, y, 24, 9.5, 2.6, GREY)
                 + f'<path d="M8.5 {y + 4.75}h7" stroke="{GREY_L}" stroke-width="1.4" stroke-linecap="round"/>\n'
                 + f'<circle cx="23.5" cy="{y + 4.75}" r="1.5" fill="{CLAY}"/>\n')
    return svg(32, body)


def tile(inner):
    return svg(32, rect(2.5, 2.5, 27, 27, 7.5, CARD_EDGE) + rect(3.5, 3.5, 25, 25, 6.5, CARD) + inner)


def settings():
    inner = f'<path d="M9 10.5h14M9 16h14M9 21.5h14" stroke="{SLATE_SOFT}" stroke-width="1.7" stroke-linecap="round"/>\n'
    for cx, cy in ((14, 10.5), (18.5, 16), (13, 21.5)):
        inner += f'<circle cx="{cx}" cy="{cy}" r="2.9" fill="{CLAY}" stroke="{CARD}" stroke-width="1.2"/>\n'
    return tile(inner)


def dolphin():
    return tile(rect(7, 9.5, 18, 14, 1.8, KRAFT) + rect(7, 8.5, 7.5, 4, 1.4, KRAFT)
                + rect(8.5, 10.5, 15, 5, 1, IVORY) + rect(7, 13, 18, 10.5, 1.8, MANILLA))


# Page geometry per grid: outline path, fold path, glyph box (cx, cy, size, stroke).
PAGE = {
    16: ("M4.5 1h5.5l3 3v9.5a1.5 1.5 0 0 1-1.5 1.5h-7A1.5 1.5 0 0 1 3 13.5v-11A1.5 1.5 0 0 1 4.5 1z",
         "M10 1v2.2a.8.8 0 0 0 .8.8H13z", (8, 9.6, 6.5, 1)),
    22: ("M6 1.5h7.5L18 6v12.5a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-15a2 2 0 0 1 2-2z",
         "M13.5 1.5v3A1.5 1.5 0 0 0 15 6h3z", (11, 13, 8.5, 1.25)),
    32: ("M8.5 3H20l6 6v17.5a2.5 2.5 0 0 1-2.5 2.5h-15A2.5 2.5 0 0 1 6 26.5v-21A2.5 2.5 0 0 1 8.5 3z",
         "M20 3v4a2 2 0 0 0 2 2h4z", (16, 18.5, 11, 1.45)),
}

# File categories: glyph and glyph color.
FILE_KINDS = {
    "generic": (None, None),
    "text": ("lines", GREY_D),
    "code": ("code", CLAY),
    "script": ("script", SLATE_SOFT),
    "image": ("images", SKY),
    "audio": ("music", FIG),
    "video": ("play", HEATHER_D),
    "archive": ("archive", KRAFT_D),
    "pdf": ("pdf", CLAY_DEEP),
    "document": ("lines", SKY),
    "spreadsheet": ("sheet", OLIVE),
    "presentation": ("slides", CLAY),
    "executable": ("cube", GREY_D),
    "package": ("cube", KRAFT_D),
    "font": ("font", SLATE_SOFT),
    "disc": ("disc", GREY_D),
}

KIND_WORDS = [
    # Checked in order; the first category with a matching word wins.
    ("pdf", {"pdf", "viewpdf", "postscript", "gzpostscript", "viewps", "djvu", "xps", "dvi", "bzdvi", "gzdvi", "viewdvi"}),
    ("disc", {"iso", "diskimage", "vdi", "vmdk", "qcow2", "hdd", "ova", "ovf", "vbox", "wim", "squashfs", "cue", "cda", "k3b"}),
    ("spreadsheet", {"spreadsheet", "spreadsheetml", "calc", "excel", "xls", "xlsx", "xlt", "xltx", "csv", "gnumeric",
                     "quattropro", "siag", "sqlite", "sqlite2", "sqlite3", "database", "access", "kexiproject", "kmymoney",
                     "skg", "skgc"}),
    ("presentation", {"presentation", "presentationml", "impress", "powerpoint", "ppt", "pptx", "pot", "potx", "keynote"}),
    ("document", {"msword", "word", "doc", "docx", "dot", "dotx", "rtf", "abiword", "epub", "fictionbook", "wordprocessingml",
                  "writer", "kword", "mswrite", "wordperfect", "lyx", "chm", "document", "scribus", "publisher", "xmind",
                  "formula", "math", "kformula"}),
    ("image", {"krita", "illustrator", "tgif", "wmf", "draw", "drawing", "graphics", "visio", "kontour", "blender",
               "iccprofile", "dicom"}),
    ("video", {"kdenlive", "kdenlivetitle", "mplayer2", "flash", "shockwave", "realmedia", "mlt"}),
    ("audio", {"audacity", "podcast", "audiobook", "cda", "ogg"}),
    ("package", {"rpm", "deb", "flatpak", "appimage", "snap", "apk", "msi", "package", "pkg", "xpinstall", "extension",
                 "plasma", "theme", "bundle"}),
    ("archive", {"tar", "zip", "7z", "rar", "compressed", "archive", "bzip", "gzip", "xz", "zstd", "lzma", "lzop", "cpio",
                 "compress", "arj", "ace", "arc", "lha", "lzh", "cab", "zoo", "tarz", "tzo", "mimearchive", "pak", "stuffit", "ar"}),
    ("script", {"script", "shellscript", "awk", "sed", "gdscript"}),
    ("executable", {"executable", "sharedlib", "object", "core", "msdownload", "jar", "bytecode", "rom", "macbinary"}),
    ("font", {"font", "fonts", "afm", "bdf", "otf", "ttf", "pcf", "snf", "ttx", "type1"}),
    ("code", {"json", "xml", "html", "xhtml", "viewhtml", "css", "javascript", "typescript", "java", "python", "python2",
              "python3", "rust", "go", "php", "perl", "ruby", "patch", "diff", "makefile", "cmake", "qml", "sql", "yaml",
              "toml", "kotlin", "swift", "csharp", "lua", "haskell", "scala", "pascal", "tcl", "sass", "scss", "markdown",
              "tex", "bibtex", "texinfo", "gettext", "po", "dtd", "xslt", "xsd", "rdf", "atom", "rss", "opml", "nim", "r",
              "m4", "godot", "shader", "designer", "kcsrc", "relaxng", "dockerfile", "troff", "sgml", "typst", "lilypond"}),
]


def mime_kind(name):
    n = name.lower()
    words = set(n.replace(".", "-").replace("+", "-").split("-"))
    if n.startswith("image-"):
        return "image"
    if n.startswith("audio-"):
        return "audio"
    if n.startswith("video-"):
        return "video"
    if n.startswith("font-"):
        return "font"
    if {"raw", "disk"} <= words or {"cd", "image"} <= words or {"qemu", "disk"} <= words:
        return "disc"
    if "opendocument" in words and "text" in words or n.startswith("libreoffice-") and "text" in words:
        return "document"
    for kind, keys in KIND_WORDS:
        if words & keys:
            return kind
    if any(w.endswith(("src", "hdr")) for w in words):
        return "code"
    if n.startswith(("text-", "message-", "x-office-")) or words & {"subrip", "srt", "sami", "calendar", "vcard", "desktop"}:
        return "text"
    return "generic"


def page(grid, kind):
    outline, fold, (cx, cy, size, stroke) = PAGE[grid]
    g, color = FILE_KINDS[kind]
    edge = {16: .9, 22: 1, 32: 1.1}[grid]
    body = (f'<path d="{outline}" fill="{PAPER}" stroke="{PAPER_EDGE}" stroke-width="{edge}" stroke-linejoin="round"/>\n'
            f'<path d="{fold}" fill="{PAPER_FOLD}" stroke="{PAPER_EDGE}" stroke-width="{edge}" stroke-linejoin="round"/>\n')
    if g:
        body += glyph(g, cx, cy, size, stroke, color)
    return svg(grid, body)


def breeze_mime_names():
    src = Path("/usr/share/icons/breeze/mimetypes/64")
    if not src.is_dir():
        raise SystemExit(f"Breeze mimetypes not found at {src}: needed to cover its icon names")
    return sorted(p.stem for p in src.glob("*.svg") if not p.stem.endswith("-symbolic"))


def write(ctx, size, name, content):
    d = ROOT / ctx / str(size)
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{name}.svg"
    if p.is_symlink():
        p.unlink()
    p.write_text(content)


def alias(ctx, size, name, target):
    p = ROOT / ctx / str(size) / f"{name}.svg"
    if p.exists() or p.is_symlink():
        p.unlink()
    p.symlink_to(f"{target}.svg")


def folder_grid(size):
    return 16 if size <= 16 else 22 if size <= 24 else 32


def main():
    for size in (16, 22, 32, 48, 64):
        for name, g in FOLDERS.items():
            write("places", size, name, folder(folder_grid(size), g))
        for name, target in FOLDER_ALIASES.items():
            alias("places", size, name, target)
        write("places", size, "user-trash", trash(False))
        write("places", size, "user-trash-full", trash(True))
        write("places", size, "network-server", server())
    names = breeze_mime_names()
    for size in ("16", "22", "scalable"):
        grid = {"16": 16, "22": 22}.get(size, 32)
        d = ROOT / "mimetypes" / size
        if d.exists():
            for old in d.iterdir():
                old.unlink()
        for kind in FILE_KINDS:
            write("mimetypes", size, f"clay-file-{kind}", page(grid, kind))
        for name in names:
            if name.startswith("inode-") and name != "inode-directory":
                continue
            if name == "inode-directory":
                write("mimetypes", size, name, folder(grid, None))
            else:
                alias("mimetypes", size, name, f"clay-file-{mime_kind(name)}")
        for name in ("unknown", "text-x-generic", "application-octet-stream"):
            alias("mimetypes", size, name, "clay-file-generic" if name != "text-x-generic" else "clay-file-text")
    for size in (16, 22, 32, 48, 64):
        write("devices", size, "drive-harddisk", drive())
        write("devices", size, "drive-harddisk-root", drive(root=True))
        write("devices", size, "drive-removable-media", usb())
        write("devices", size, "media-flash-memory", sdcard())
    for size in (16, 22, 24, 32, 48, 64):
        write("apps", size, "systemsettings", settings())
        alias("apps", size, "preferences-system", "systemsettings")
        write("apps", size, "org.kde.dolphin", dolphin())


if __name__ == "__main__":
    main()
