#!/usr/bin/env python3
"""Generate the full-color part of clay-icons.

Design language: matte, opaque paper shapes, no outlines, quiet
restraint. Folders are manilla paper on a kraft back with clay glyphs; physical
objects (trash, drives) are warm neutral grey; system apps are slate tiles.
Clay is an accent only. Colors are opaque so an icon looks the same on Light
and Dark surfaces.

16 and 22 px folders use their own pixel grids; everything else is drawn on a
32 grid and scaled. Action icons are hand-made and not touched here; the
monochrome system tray set (status/scalable) is generated below in the same
line style.

Run from anywhere: python3 tools/gen_icons.py
"""
import os
from pathlib import Path

ROOT = Path(os.environ.get("CLAY_ICONS_ROOT") or Path(__file__).resolve().parent.parent / "payload/icons/clay-icons")

# Palette.
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
    # KDE app tiles.
    "kate": [("s", "M8.5 6.5 3 12l5.5 5.5M15.5 6.5 21 12l-5.5 5.5", SLATE_SOFT), ("s", "M13.6 4.5l-3.2 15", CLAY)],
    "kwrite": [("s", "M4 6.5h16M4 12h11M4 17.5h8", SLATE_SOFT), ("s", "M18 14v6.5", CLAY)],
    "spectacle": [("s", "M3.5 8V5A1.5 1.5 0 0 1 5 3.5h3M16 3.5h3A1.5 1.5 0 0 1 20.5 5v3M20.5 16v3a1.5 1.5 0 0 1-1.5 1.5h-3"
                        "M8 20.5H5A1.5 1.5 0 0 1 3.5 19v-3", SLATE_SOFT), ("f", '<circle cx="12" cy="12" r="4"/>', CLAY)],
    "gwenview": [("f", '<path d="M2.5 20.5 9 11.5l4.8 5.8 3-3.4 4.7 6.6z"/>', SKY), ("f", '<circle cx="16.5" cy="7.5" r="2.8"/>', CLAY)],
    "okular": [("s", "M3.5 5h10M3.5 10h6M3.5 15h5", SLATE_SOFT),
               ("s", "M15 8.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9zM18.3 16.3 21 19", CLAY)],
    "hwinfo": [("s", "M8 6h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2z"
                     "M10 3v3M14 3v3M10 18v3M14 18v3M3 10h3M3 14h3M18 10h3M18 14h3", SLATE_SOFT),
               ("f", '<rect x="9.5" y="9.5" width="5" height="5" rx="1"/>', CLAY)],
    "kdeconnect": [("s", "M9 2.5h6A2.5 2.5 0 0 1 17.5 5v14a2.5 2.5 0 0 1-2.5 2.5H9A2.5 2.5 0 0 1 6.5 19V5A2.5 2.5 0 0 1 9 2.5z",
                    SLATE_SOFT), ("f", '<circle cx="12" cy="17.5" r="1.6"/>', CLAY)],
    "emoji": [("f", '<circle cx="12" cy="12" r="9"/>', KRAFT),
              ("f", '<circle cx="9" cy="10" r="1.3"/><circle cx="15" cy="10" r="1.3"/>', SLATE_SOFT),
              ("s", "M8.5 14.5c2 2 5 2 7 0", SLATE_SOFT)],
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


# Icon name -> (glyph, base color); org.kde.* names alias to the first.
APPS = {
    "kate": ("kate", None), "kwrite": ("kwrite", None), "spectacle": ("spectacle", None),
    "gwenview": ("gwenview", None), "okular": ("okular", None), "ark": ("archive", KRAFT_D),
    "hwinfo": ("hwinfo", None), "kdeconnect": ("kdeconnect", None), "preferences-desktop-emoticons": ("emoji", None),
}
APP_ALIASES = {
    "org.kde.kate": "kate", "org.kde.kwrite": "kwrite", "org.kde.spectacle": "spectacle",
    "org.kde.gwenview": "gwenview", "org.kde.okular": "okular", "org.kde.ark": "ark",
    "org.kde.kinfocenter": "hwinfo", "org.kde.kdeconnect.app": "kdeconnect",
}


def app(glyph_name, color):
    return tile(glyph(glyph_name, 16, 16, 17, 1.7, color or GLYPH))


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


# System tray: monochrome line icons on a 24 grid, recolored by Plasma through
# ColorScheme-Text. Inactive parts are dimmed, Clay marks only warnings/news.
TRAY_STYLE = ('<defs>\n<style type="text/css" id="current-color-scheme">\n'
              '.ColorScheme-Text { color:#141413; }\n'
              '.ColorScheme-NeutralText { color:#A06A2C; }\n'
              '.ColorScheme-NegativeText { color:#B5473A; }\n</style>\n</defs>\n')
DIM = .3


def line(d, op=1, color=None, sw=1.6):
    paint = f'stroke="{color}"' if color else 'stroke="currentColor" class="ColorScheme-Text"'
    return (f'<path d="{d}" fill="none" {paint} opacity="{round(.86 * op, 3):g}" stroke-width="{sw:g}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>\n')


def sem(d, cls):
    """A stroke in one of the color scheme's semantic colors."""
    return (f'<path d="{d}" fill="none" stroke="currentColor" class="ColorScheme-{cls}" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round"/>\n')


def dot(cx, cy, r, op=1, color=None):
    paint = f'fill="{color}"' if color else 'fill="currentColor" class="ColorScheme-Text"'
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" {paint} opacity="{round(.86 * op, 3):g}"/>\n'


def fill(d, op=1, color=None):
    paint = f'fill="{color}"' if color else 'fill="currentColor" class="ColorScheme-Text"'
    return f'<path d="{d}" {paint} opacity="{round(.86 * op, 3):g}"/>\n'


def tray(body):
    return svg(24, TRAY_STYLE + body)


def fan(cx, cy, r):
    """Arc of radius r spanning 45 degrees each side of straight up."""
    dx = round(r * .7071, 2)
    return f"M{cx - dx:g} {cy - dx:g}A{r} {r} 0 0 1 {cx + dx:g} {cy - dx:g}"


def wave(cx, cy, r):
    """Arc of radius r spanning 45 degrees each side of straight right."""
    dx = round(r * .7071, 2)
    return f"M{cx + dx:g} {cy - dx:g}A{r} {r} 0 0 1 {cx + dx:g} {cy + dx:g}"


SLASH = "M4 4l16 16"
LOCK = line("M17.6 17v-1.2a1.7 1.7 0 0 1 3.4 0V17") + fill("M16.9 16.6h4.8a.7.7 0 0 1 .7.7v3.5a.7.7 0 0 1-.7.7h-4.8a.7.7 0 0 1-.7-.7v-3.5a.7.7 0 0 1 .7-.7z")
WARN = line("M20 13.8v4.4", color=CLAY) + dot(20, 21, 1.05, color=CLAY)


def wifi(level, badge="", dot_color=None, slash=False):
    """level: number of lit parts, 0..4 (dot + three arcs)."""
    lit = lambda i: 1 if level > i and not slash else DIM
    body = dot(12, 18.5, 1.7, 1 if dot_color else lit(0), dot_color)
    for i, r in enumerate((5, 9.5, 14), 1):
        body += line(fan(12, 18.5, r), lit(i))
    if slash:
        body += line(SLASH)
    return tray(body + badge)


def speaker(waves=(), body_extra=""):
    body = line("M3.5 9.5h3l4.5-4v13l-4.5-4h-3z") + body_extra
    for r, op, color in waves:
        body += line(wave(11, 12, r), op, color)
    return tray(body)


def volume(level, hot=0):
    waves = []
    for i, r in enumerate((4, 7, 10)):
        waves.append((r, 1 if i < level else DIM, CLAY if i >= 3 - hot else None))
    return speaker(waves)


BELL = line("M6.5 16.5V11a5.5 5.5 0 0 1 11 0v5.5l1.5 2h-14zM10.2 20.8a1.9 1.9 0 0 0 3.6 0M12 3.5v2")
BLUETOOTH = "M7 7.5l10 9-5 4.5V3l5 4.5-10 9"
MOON = "M15.7 4.2A8.3 8.3 0 1 0 19.8 16 7.2 7.2 0 0 1 15.7 4.2z"
PORT = ("M4.5 7a2 2 0 0 1 2-2h11a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-2.5v2.5h-6V17H6.5a2 2 0 0 1-2-2z"
        "M8.5 8.5v3M12 8.5v3M15.5 8.5v3")
MIC = "M12 3a3 3 0 0 1 3 3v5a3 3 0 0 1-6 0V6a3 3 0 0 1 3-3zM6 11a6 6 0 0 0 12 0M12 17v3.5M9 20.5h6"
PLANE = ("M12 2.8c.9 0 1.5.9 1.5 2v4.4l7 4.3v1.9l-7-2.2v4.2l2.2 1.7v1.6L12 19.8l-3.7 .9v-1.6l2.2-1.7v-4.2"
         "l-7 2.2v-1.9l7-4.3V4.8c0-1.1.6-2 1.5-2z")
LEAF = "M19.5 4.5C10 4.5 4.5 8.5 4.5 14.5c0 2.8 2 5 5 5 6 0 10-5.5 10-15zM4.5 19.5l8-8"
GAUGE = "M4.2 17.5a8.5 8.5 0 1 1 15.6 0"
CUP = "M5 9h11v5a4 4 0 0 1-4 4H9a4 4 0 0 1-4-4zM16 10.5h1.2a2.3 2.3 0 0 1 0 4.6H16M8.5 3.5v2.5M12.5 3.5v2.5M4.5 21h13"
STICK = ("M8 9h8a1.5 1.5 0 0 1 1.5 1.5V19a2.5 2.5 0 0 1-2.5 2.5H9A2.5 2.5 0 0 1 6.5 19v-8.5A1.5 1.5 0 0 1 8 9z"
         "M9 9V3.5h6V9")
HDD = "M5.5 6.5h13A2.5 2.5 0 0 1 21 9v6a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 15V9a2.5 2.5 0 0 1 2.5-2.5zM3 12.5h18"
SD = "M7 3h7.5L19 7.5V19a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zM9 6.5v2.5M12 6.5v2.5"
SCREEN = "M4.5 4.5h15a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-15a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2zM12 17.5v3M8 20.5h8"
CIRCLE = "M12 3.5a8.5 8.5 0 1 1 0 17 8.5 8.5 0 0 1 0-17z"
PHONE = "M9.5 2.5h5A2.5 2.5 0 0 1 17 5v14a2.5 2.5 0 0 1-2.5 2.5h-5A2.5 2.5 0 0 1 7 19V5a2.5 2.5 0 0 1 2.5-2.5zM10.8 5.5h2.4"
TABLET = "M6.5 2.5h11A2.5 2.5 0 0 1 20 5v14a2.5 2.5 0 0 1-2.5 2.5h-11A2.5 2.5 0 0 1 4 19V5a2.5 2.5 0 0 1 2.5-2.5z"
LAPTOP = "M6 5h12a1.5 1.5 0 0 1 1.5 1.5V15h-15V6.5A1.5 1.5 0 0 1 6 5zM2.5 18.5h19"
KEYBOARD = "M4.5 7.5h15a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-15a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2zM8 15.2h8"
KEYBOARD_LOW = "M4.5 10.5h15a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-15a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2zM8 16.5h8"
MOUSE = "M12 3a5.5 5.5 0 0 1 5.5 5.5v7a5.5 5.5 0 0 1-11 0v-7A5.5 5.5 0 0 1 12 3zM12 3v6.5"
GAMEPAD = ("M7.5 7.5h9a4.5 4.5 0 0 1 4.4 5.4l-.8 3.9a2.2 2.2 0 0 1-3.8 1l-2.1-2.3h-4.4"
           "l-2.1 2.3a2.2 2.2 0 0 1-3.8-1l-.8-3.9A4.5 4.5 0 0 1 7.5 7.5zM8 10.5v3M6.5 12h3")
HEADSET = ("M4.5 14v-2a7.5 7.5 0 0 1 15 0v2M4.5 14h2.5a1 1 0 0 1 1 1v3.5a1 1 0 0 1-1 1H6a1.5 1.5 0 0 1-1.5-1.5z"
           "M19.5 14H17a1 1 0 0 0-1 1v3.5a1 1 0 0 0 1 1h1a1.5 1.5 0 0 0 1.5-1.5z")
LOCKED = ("M7 10.5h10a1.5 1.5 0 0 1 1.5 1.5v7a1.5 1.5 0 0 1-1.5 1.5H7A1.5 1.5 0 0 1 5.5 19v-7A1.5 1.5 0 0 1 7 10.5z"
          "M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5")


def sun():
    rays = "".join(f"M{12 + 6.3 * x:g} {12 + 6.3 * y:g}L{12 + 8.6 * x:g} {12 + 8.6 * y:g}"
                   for x, y in ((1, 0), (.7071, .7071), (0, 1), (-.7071, .7071),
                                (-1, 0), (-.7071, -.7071), (0, -1), (.7071, -.7071)))
    return tray(line("M12 8.3a3.7 3.7 0 1 1 0 7.4 3.7 3.7 0 0 1 0-7.4z" + rays))


SUN_SMALL = ("M12 8.1a2.4 2.4 0 1 1 0 4.8 2.4 2.4 0 0 1 0-4.8zM12 5.8v.01M12 15.2v.01M7.4 10.5h.01M16.6 10.5h.01"
             "M8.7 7.2l.01.01M15.3 7.2l.01.01M8.7 13.8l.01.01M15.3 13.8l.01.01")


def shrunk(d, k=.84, dx=-.6, dy=-1.4):
    """A glyph scaled down toward the top-left to leave room for a badge."""
    return f'<g transform="translate({dx} {dy}) scale({k})">\n{line(d, sw=round(1.6 / k, 2))}</g>\n'


def battery(pct, charging=False, missing=False):
    body = "M5 7h12a2.5 2.5 0 0 1 2.5 2.5v5A2.5 2.5 0 0 1 17 17H5a2.5 2.5 0 0 1-2.5-2.5v-5A2.5 2.5 0 0 1 5 7zM21.7 10.5v3"
    if missing:
        return tray(line(body, DIM) + line(SLASH))
    low = pct <= 10 and not charging
    out = line(body, color=CLAY if pct == 0 and not charging else None)
    w = round(max(13 * pct / 100, 2 if pct else 0), 2)
    if w:
        out += fill(f"M5.5 9h{w - 2:g}a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1h-{w - 2:g}a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1z",
                    .25 if charging else 1, CLAY if low else None)
    if charging:
        out += fill("M12.9 8.2 8.9 12.6h3l-1 3.2 4.1-4.5h-3z")
    return tray(out)


def bars(level, x0=4.2, step=4.2, slash=False):
    out = ""
    for i in range(4):
        h = 4 + i * 4
        x = x0 + i * step
        out += fill(f"M{x:g} {20 - h:g}h.4a1 1 0 0 1 1 1v{h - 2:g}a1 1 0 0 1-1 1h-.4a1 1 0 0 1-1-1v-{h - 2:g}a1 1 0 0 1 1-1z",
                    1 if level > i and not slash else DIM)
    return out + (line(SLASH) if slash else "")


def tray_icons():
    """Icon name -> SVG, plus aliases name -> target, for the tray applets."""
    icons = {
        "notification-inactive": tray(BELL),
        "notification-active": tray(BELL + dot(18.6, 5.4, 2.2, color=CLAY)),
        "notification-disabled": tray(BELL + line(SLASH)),
        "klipper-symbolic": tray(line("M8.5 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-1.5"
                             "M9.8 3h4.4a1.3 1.3 0 0 1 1.3 1.3v1.4A1.3 1.3 0 0 1 14.2 7H9.8a1.3 1.3 0 0 1-1.3-1.3V4.3A1.3 1.3 0 0 1 9.8 3z"
                             "M8.5 11.5h7M8.5 15h4.5")),
        "media-playback-playing": tray(line(CIRCLE) + fill(
            "M10.3 8.6v6.8a.6.6 0 0 0 .9.5l5.2-3.4a.6.6 0 0 0 0-1l-5.2-3.4a.6.6 0 0 0-.9.5z")),
        "media-playback-paused": tray(line(CIRCLE + "M10 9v6M14 9v6")),
        "media-playback-stopped": tray(line(CIRCLE) + fill("M10.5 9.5h3a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-3a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1z")),
        "brightness-high": sun(),
        "redshift-status-on": tray(line(MOON)),
        "redshift-status-off": tray(line(MOON) + line(SLASH)),
        "network-bluetooth-activated": tray(line(BLUETOOTH) + dot(3.8, 12, 1.2) + dot(20.2, 12, 1.2)),
        "network-bluetooth": tray(line(BLUETOOTH)),
        "network-bluetooth-inactive": tray(line(BLUETOOTH, .45)),
        "kdeconnect-tray": tray(line(PHONE) + dot(12, 18.5, 1)),
        "audio-volume-muted": speaker(body_extra=line("M15 9.5l5 5M20 9.5l-5 5")),
        "audio-volume-low": volume(1),
        "audio-volume-medium": volume(2),
        "audio-volume-high": volume(3),
        "audio-volume-high-warning": volume(3, hot=1),
        "audio-volume-high-danger": volume(3, hot=2),
        "audio-input-microphone-symbolic": tray(line(MIC)),
        "microphone-sensitivity-muted": tray(line(MIC) + line(SLASH)),
        "network-wired-activated": tray(line(PORT)),
        "network-wired-activated-locked": tray(shrunk(PORT) + LOCK),
        "network-wired-activated-limited": tray(shrunk(PORT) + WARN),
        "network-vpn": tray(line("M12 3l7 2.8v5.4c0 4.4-3 7.8-7 9.3-4-1.5-7-4.9-7-9.3V5.8z") + dot(12, 11, 1.4)
                            + line("M12 12v3.2")),
        "network-flightmode-on": tray(line(PLANE)),
        "network-flightmode-off": tray(line(PLANE, DIM) + line(SLASH)),
        "network-mobile-available": tray(bars(0)),
        "network-mobile-off": tray(bars(0, slash=True)),
        "battery-missing": battery(0, missing=True),
        "battery-profile-powersave": tray(line(LEAF)),
        "battery-profile-balanced": tray(line(GAUGE + "M12 15.5V10")),
        "battery-profile-performance": tray(line(GAUGE + "M12 15.5l4-3.6")),
        "device-notifier-symbolic": tray(line(STICK) + dot(10.8, 6, .8) + dot(13.2, 6, .8)),
        "drive-harddisk-symbolic": tray(line(HDD) + dot(17.3, 15, 1)),
        "media-flash-sd-mmc-symbolic": tray(line(SD)),
        "media-optical-symbolic": tray(line(CIRCLE) + line("M12 9.8a2.2 2.2 0 1 1 0 4.4 2.2 2.2 0 0 1 0-4.4z")),
        "preferences-desktop-display-randr-symbolic": tray(line(SCREEN + "M9.5 13l5-5M11.2 8h3.3v3.3")),
        "video-display-brightness": tray(line(SCREEN) + line(SUN_SMALL, sw=1.4)),
        "input-keyboard": tray(line(KEYBOARD) + dots(((7.2, 10.8), (10.4, 10.8), (13.6, 10.8), (16.8, 10.8), (8.8, 13.4), (12, 13.4), (15.2, 13.4)), .9)),
        "input-keyboard-brightness": tray(line(KEYBOARD_LOW)
                                          + line("M8 3.5v2.5M12 2.5v3.5M16 3.5v2.5")),
        "input-keyboard-color": tray(line(KEYBOARD_LOW)
                                     + dots(((8, 5), (12, 5), (16, 5)), 1.3)),
        "input-mouse": tray(line(MOUSE)),
        "input-gamepad": tray(line(GAMEPAD) + dots(((15.5, 11), (17.3, 13)), 1)),
        "audio-headset": tray(line(HEADSET)),
        "smartphone": tray(line(PHONE) + dot(12, 18.5, 1)),
        "tablet": tray(line(TABLET) + dot(12, 18.5, 1)),
        "computer-laptop": tray(line(LAPTOP)),
        "computer": tray(line(SCREEN)),
        "dialog-password": tray(line(LOCKED)),
        "system-suspend-inhibited": tray(line(CUP)),
        "system-suspend-uninhibited": tray(line(CUP) + line(SLASH)),
        "network-wired-disconnected": tray(line(PORT, DIM) + line(SLASH)),
        "network-wireless-acquiring": wifi(0, dot_color=CLAY),
        "network-wireless-disconnected": wifi(0, slash=True),
    }
    for pct, level in ((0, 0), (20, 1), (40, 2), (60, 3), (80, 3), (100, 4)):
        icons[f"network-wireless-{pct}"] = wifi(level)
        icons[f"network-wireless-{pct}-locked"] = wifi(level, LOCK)
        icons[f"network-wireless-{pct}-limited"] = wifi(level, WARN)
    for pct, level in ((0, 0), (20, 1), (40, 2), (60, 3), (80, 3), (100, 4)):
        icons[f"network-mobile-{pct}"] = tray(bars(level))
        icons[f"network-mobile-{pct}-locked"] = tray(bars(level, 2.6, 3.6) + LOCK)
    for pct in range(0, 101, 10):
        icons[f"battery-{pct:03}"] = battery(pct)
        icons[f"battery-{pct:03}-charging"] = battery(pct, charging=True)
    aliases = {
        "notifications": "notification-inactive",
        "notifications-disabled": "notification-disabled",
        "notification-progress-inactive": "notification-inactive",
        "notification-progress-active": "notification-active",
        "redshift-status-day": "brightness-high",
        "microphone-sensitivity-low": "audio-input-microphone-symbolic",
        "microphone-sensitivity-medium": "audio-input-microphone-symbolic",
        "microphone-sensitivity-high": "audio-input-microphone-symbolic",
        "network-wired": "network-wired-activated",
        "audio-headphones": "audio-headset", "phone": "smartphone", "smartphone-connected": "smartphone",
        "smartphone-disconnected": "smartphone", "phone-connected": "smartphone", "computer-desktop": "computer",
        "tv": "computer", "video-television": "computer", "input-mouse-battery": "input-mouse",
        "input-keyboard-battery": "input-keyboard", "input-gamepad-battery": "input-gamepad",
        "audio-headset-battery": "audio-headset", "phone-battery": "smartphone",
        "network-wired-available": "network-wired-activated",
        "network-wired-unavailable": "network-wired-disconnected",
        "network-unavailable": "network-wireless-disconnected",
        "network-wireless-off": "network-wireless-disconnected",
        "network-wireless": "network-wireless-100",
        "network-wireless-signal-none": "network-wireless-0",
        "network-wireless-signal-weak": "network-wireless-20",
        "network-wireless-signal-ok": "network-wireless-40",
        "network-wireless-signal-good": "network-wireless-60",
        "network-wireless-signal-excellent": "network-wireless-100",
    }
    for pct in ("00", "20", "25", "40", "50", "60", "75", "80", "100"):
        p = int(pct)
        aliases[f"network-wireless-connected-{pct}"] = f"network-wireless-{min((0, 20, 40, 60, 80, 100), key=lambda v: abs(v - p))}"
    aliases.update({
        "network-limited": "network-wired-activated-limited",
        "network-mobile-on": "network-mobile-100",
        "speedometer": "battery-profile-balanced",
        "drive-removable-media-symbolic": "device-notifier-symbolic",
        "drive-removable-media-usb-symbolic": "device-notifier-symbolic",
        "drive-removable-media-usb-pendrive-symbolic": "device-notifier-symbolic",
        "media-flash-memory-stick-symbolic": "media-flash-sd-mmc-symbolic",
        "media-flash-symbolic": "media-flash-sd-mmc-symbolic",
        "drive-optical-symbolic": "media-optical-symbolic",
        "drive-harddisk-root-symbolic": "drive-harddisk-symbolic",
    })
    # Per-generation mobile variants and power profile variants keep the plain glyph.
    for pct in (0, 20, 40, 60, 80, 100):
        for tech in ("5g", "edge", "gprs", "hsdpa", "hspa", "hsupa", "lte", "umts"):
            aliases[f"network-mobile-{pct}-{tech}"] = f"network-mobile-{pct}"
            aliases[f"network-mobile-{pct}-{tech}-locked"] = f"network-mobile-{pct}-locked"
    for pct in range(0, 101, 10):
        for state in ("", "-charging"):
            for profile in ("balanced", "performance", "powersave"):
                aliases[f"battery-{pct:03}{state}-profile-{profile}"] = f"battery-{pct:03}{state}"
    for word, pct in (("full", 100), ("good", 60), ("low", 20), ("caution", 10), ("empty", 0)):
        aliases[f"battery-{word}"] = f"battery-{pct:03}"
        aliases[f"battery-{word}-charging"] = f"battery-{pct:03}-charging"
    return icons, aliases


# Common actions on buttons, toolbars and popups, same line language as the tray.
PAGE_LINE = "M6.5 3h7l5 5v11.5a1.5 1.5 0 0 1-1.5 1.5H6.5A1.5 1.5 0 0 1 5 19.5v-15A1.5 1.5 0 0 1 6.5 3zM13.5 3v5h5"
LENS = "M10.5 4a6.5 6.5 0 1 1 0 13 6.5 6.5 0 0 1 0-13zM15.3 15.3 20 20"
EYE = "M2.5 12s3.5-6.5 9.5-6.5 9.5 6.5 9.5 6.5-3.5 6.5-9.5 6.5S2.5 12 2.5 12zM12 9a3 3 0 1 1 0 6 3 3 0 0 1 0-6z"
FRAME = "M5.5 4.5h13a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2v-11a2 2 0 0 1 2-2z"
FOLDER_LINE = "M3.5 18.5V6A1.5 1.5 0 0 1 5 4.5h4.5l2 2.5H19A1.5 1.5 0 0 1 20.5 8.5v10A1.5 1.5 0 0 1 19 20H5a1.5 1.5 0 0 1-1.5-1.5z"
STAR = "M12 3.8l2.5 5.2 5.7.8-4.1 4 1 5.7L12 16.8l-5.1 2.7 1-5.7-4.1-4 5.7-.8z"
PIN = "M14.5 3.5l6 6-2.3.8-3.6 3.6.4 3.6-1.4 1.4-8.5-8.5L6.5 9l3.6.4 3.6-3.6zM9.2 14.8 3.5 20.5"
PLUG = "M9 3.5v4M15 3.5v4M6.5 7.5h11v3a5.5 5.5 0 0 1-11 0zM12 16v4.5"
X = "M6.5 6.5l11 11M17.5 6.5l-11 11"


def dots(points, r=1.5):
    return "".join(dot(x, y, r) for x, y in points)


def action_icons():
    lines = lambda d: tray(line(d))
    icons = {
        "go-previous": lines("M14.5 5.5 8 12l6.5 6.5"),
        "go-next": lines("M9.5 5.5 16 12l-6.5 6.5"),
        "go-up": lines("M5.5 14.5 12 8l6.5 6.5"),
        "go-down": lines("M5.5 9.5 12 16l6.5-6.5"),
        "go-first": lines("M17 5.5 10.5 12l6.5 6.5M7 5.5v13"),
        "go-last": lines("M7 5.5 13.5 12 7 18.5M17 5.5v13"),
        "go-top": lines("M5.5 4.5h13M5.5 17 12 10.5l6.5 6.5"),
        "go-bottom": lines("M5.5 19.5h13M5.5 7 12 13.5 18.5 7"),
        "go-home": lines("M4 11 12 4l8 7M6 9.5V20h4.5v-5.5h3V20H18V9.5"),
        "edit-copy": lines("M6.5 7.5h7a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-7a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2z"
                           "M8.5 5.5a2 2 0 0 1 2-2h7a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2"),
        "edit-cut": lines("M7 15a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM17 15a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5z"
                          "M8.6 15.6 17 3.5M15.4 15.6 7 3.5"),
        "edit-paste": lines("M8.5 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-1.5"
                            "M9.8 3h4.4a1.3 1.3 0 0 1 1.3 1.3v1.4A1.3 1.3 0 0 1 14.2 7H9.8a1.3 1.3 0 0 1-1.3-1.3V4.3A1.3 1.3 0 0 1 9.8 3z"),
        "edit-delete": lines("M4.5 6.5h15M9.5 6.5v-2h5v2M6.5 6.5l1 13a1.5 1.5 0 0 0 1.5 1.4h6a1.5 1.5 0 0 0 1.5-1.4l1-13"
                             "M10 10.5V17M14 10.5V17"),
        "edit-undo": lines("M8.5 5 4 9.5 8.5 14M4 9.5h10a5.5 5.5 0 0 1 0 11h-3"),
        "edit-redo": lines("M15.5 5 20 9.5 15.5 14M20 9.5H10a5.5 5.5 0 0 0 0 11h3"),
        "edit-find": lines(LENS),
        "edit-clear": lines("M9 5.5h9.5a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H9L3.5 12zM11.5 9.5l5 5M16.5 9.5l-5 5"),
        "edit-clear-all": lines("M4 7h10M4 12h10M4 17h7M15.5 14.5l5 5M20.5 14.5l-5 5"),
        "edit-rename": lines("M13 7H5.5a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2H13M17.5 4.5v15M15.5 4.5h4M15.5 19.5h4"),
        "edit-select-all": lines("M6 4h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zM8 12l2.8 2.8L16 9.3"),
        "document-edit": lines("M14.5 5.5l4 4M4 20l1-4.5L16 4.5a1.4 1.4 0 0 1 2 0l1.5 1.5a1.4 1.4 0 0 1 0 2L8.5 19z"),
        "document-new": lines(PAGE_LINE + "M12 11v6M9 14h6"),
        "document-properties": lines(PAGE_LINE + "M8.5 12h7M8.5 15.5h7"),
        "document-open": lines("M3.5 18V6A1.5 1.5 0 0 1 5 4.5h4l2 2h7A1.5 1.5 0 0 1 19.5 8v2.5"
                               "M3.5 18l2.3-6.4a1.5 1.5 0 0 1 1.4-1h13a1 1 0 0 1 .9 1.3L19 18.5a1.5 1.5 0 0 1-1.4 1H5A1.5 1.5 0 0 1 3.5 18z"),
        "document-save": lines("M5.5 3.5h10.3l3.7 3.7v11.3a2 2 0 0 1-2 2h-12a2 2 0 0 1-2-2v-13a2 2 0 0 1 2-2z"
                               "M8.5 3.5V8h6V3.5M7.5 20.5V14h9v6.5"),
        "document-print": lines("M7 9V3.5h10V9M7 17H5a1.5 1.5 0 0 1-1.5-1.5v-5A1.5 1.5 0 0 1 5 9h14a1.5 1.5 0 0 1 1.5 1.5v5"
                                "A1.5 1.5 0 0 1 19 17h-2M7 14h10v6.5H7z"),
        "document-open-recent": lines("M12 3.5a8.5 8.5 0 1 1 0 17 8.5 8.5 0 0 1 0-17zM12 7.5V12l3 2"),
        "document-share": lines("M17.5 3.2a2.3 2.3 0 1 1 0 4.6 2.3 2.3 0 0 1 0-4.6zM6.5 9.7a2.3 2.3 0 1 1 0 4.6 2.3 2.3 0 0 1 0-4.6z"
                                "M17.5 16.2a2.3 2.3 0 1 1 0 4.6 2.3 2.3 0 0 1 0-4.6zM8.5 10.9l7-4.2M8.5 13.1l7 4.2"),
        "document-export": lines("M12 14.5v-11M7.5 8 12 3.5 16.5 8M4.5 13.5v5a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2v-5"),
        "document-import": lines("M12 3.5v11M7.5 10l4.5 4.5 4.5-4.5M4.5 13.5v5a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2v-5"),
        "folder-new": lines(FOLDER_LINE + "M12 10.5v6M9 13.5h6"),
        "list-add": lines("M12 5v14M5 12h14"),
        "list-remove": lines("M5 12h14"),
        "window-close": lines(X),
        "window-minimize": lines("M6 9.5l6 6 6-6"),
        "window-maximize": lines("M6 14.5l6-6 6 6"),
        "window-restore": lines("M12 5.5 18.5 12 12 18.5 5.5 12z"),
        "window-pin": lines(PIN),
        "window-unpin": tray(line(PIN) + line(SLASH)),
        "tab-new": lines(FRAME + "M12 9v6M9 12h6"),
        "view-fullscreen": lines("M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5"),
        "view-restore": lines("M9 4v5H4M20 9h-5V4M15 20v-5h5M4 15h5v5"),
        "view-refresh": lines("M19.5 12a7.5 7.5 0 1 1-2.2-5.3M19.5 4v4.5H15"),
        "view-list-details": lines("M4.5 6h.01M9 6h11M4.5 12h.01M9 12h11M4.5 18h.01M9 18h11"),
        "view-list-icons": lines("M5.5 4h3a1.5 1.5 0 0 1 1.5 1.5v3A1.5 1.5 0 0 1 8.5 10h-3A1.5 1.5 0 0 1 4 8.5v-3A1.5 1.5 0 0 1 5.5 4z"
                                 "M15.5 4h3A1.5 1.5 0 0 1 20 5.5v3a1.5 1.5 0 0 1-1.5 1.5h-3A1.5 1.5 0 0 1 14 8.5v-3A1.5 1.5 0 0 1 15.5 4z"
                                 "M5.5 14h3a1.5 1.5 0 0 1 1.5 1.5v3A1.5 1.5 0 0 1 8.5 20h-3A1.5 1.5 0 0 1 4 18.5v-3A1.5 1.5 0 0 1 5.5 14z"
                                 "M15.5 14h3a1.5 1.5 0 0 1 1.5 1.5v3a1.5 1.5 0 0 1-1.5 1.5h-3a1.5 1.5 0 0 1-1.5-1.5v-3a1.5 1.5 0 0 1 1.5-1.5z"),
        "view-list-tree": lines("M5 4.5V18h5M5 11h5M13 4.5h7M13 11h7M13 18h7"),
        "view-sort-ascending": lines("M7 4v16M3.5 16.5 7 20l3.5-3.5M13 6h3M13 12h5M13 18h7"),
        "view-sort-descending": lines("M7 4v16M3.5 16.5 7 20l3.5-3.5M13 6h7M13 12h5M13 18h3"),
        "view-filter": lines("M4 5h16l-6 7.5V19l-4 1.5v-8z"),
        "view-split-left-right": lines(FRAME + "M12 4.5v15"),
        "view-split-top-bottom": lines(FRAME + "M3.5 12h17"),
        "zoom-in": lines(LENS + "M8 10.5h5M10.5 8v5"),
        "zoom-out": lines(LENS + "M8 10.5h5"),
        "password-show-on": lines(EYE),
        "password-show-off": tray(line(EYE) + line(SLASH)),
        "dialog-ok": lines("M5 12.5l4.5 4.5L19 7.5"),
        "dialog-cancel": lines(CIRCLE + "M6 6l12 12"),
        "dialog-information": tray(line(CIRCLE + "M12 11v5.5") + dot(12, 7.8, 1.1)),
        "dialog-question": tray(line(CIRCLE + "M9.6 9.5a2.5 2.5 0 1 1 3.4 2.3c-.6.3-1 .8-1 1.5v.5") + dot(12, 16.8, 1.1)),
        "dialog-warning": tray(sem("M10.7 4.3a1.5 1.5 0 0 1 2.6 0l7.5 13.2a1.5 1.5 0 0 1-1.3 2.2H4.5a1.5 1.5 0 0 1-1.3-2.2zM12 9.5V14", "NeutralText")
                               + '<circle cx="12" cy="16.8" r="1.1" fill="currentColor" class="ColorScheme-NeutralText"/>\n'),
        "dialog-error": tray(sem(CIRCLE + "M9 9l6 6M15 9l-6 6", "NegativeText")),
        "help-contents": lines("M12 6.5c-2-1.5-5-2-8-1.5V18c3-.5 6 0 8 1.5 2-1.5 5-2 8-1.5V5c-3-.5-6 0-8 1.5zM12 6.5v13"),
        "process-stop": lines(CIRCLE + "M9.5 9.5l5 5M14.5 9.5l-5 5"),
        "configure": tray(line("M4 7h9M17 7h3M4 17h3M11 17h9") + line("M15 5a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM9 15a2 2 0 1 1 0 4 2 2 0 0 1 0-4z")),
        "application-menu": lines("M4.5 6.5h15M4.5 12h15M4.5 17.5h15"),
        "overflow-menu": tray(dots(((12, 5.5), (12, 12), (12, 18.5)))),
        "view-more-horizontal": tray(dots(((5.5, 12), (12, 12), (18.5, 12)))),
        "non-starred": lines(STAR),
        "starred": tray(fill(STAR) + line(STAR)),
        "bookmarks": lines("M7 3.5h10a1 1 0 0 1 1 1v16l-6-4-6 4v-16a1 1 0 0 1 1-1z"),
        "bookmark-new": lines("M7 3.5h10a1 1 0 0 1 1 1v16l-6-4-6 4v-16a1 1 0 0 1 1-1zM12 7.5v5M9.5 10h5"),
        "object-locked": lines(LOCKED),
        "object-unlocked": lines("M7 10.5h10a1.5 1.5 0 0 1 1.5 1.5v7a1.5 1.5 0 0 1-1.5 1.5H7A1.5 1.5 0 0 1 5.5 19v-7A1.5 1.5 0 0 1 7 10.5z"
                                 "M8.5 10.5V8a3.5 3.5 0 0 1 6.8-1.2"),
        "media-playback-start": lines("M8 5.5v13l10.5-6.5z"),
        "media-playback-pause": lines("M8.5 5.5v13M15.5 5.5v13"),
        "media-playback-stop": lines("M7.5 6.5h9a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1h-9a1 1 0 0 1-1-1v-9a1 1 0 0 1 1-1z"),
        "media-skip-forward": lines("M6 6v12l8.5-6zM18 6v12"),
        "media-skip-backward": lines("M18 6v12L9.5 12zM6 6v12"),
        "media-seek-forward": lines("M4 6.5v11l7.5-5.5zM12.5 6.5v11l7.5-5.5z"),
        "media-seek-backward": lines("M20 6.5v11L12.5 12zM11.5 6.5v11L4 12z"),
        "media-eject": lines("M12 5l7 8H5zM5 18.5h14"),
        "media-playlist-repeat": lines("M17 3.5l3 3-3 3M4 11.5v-1a4 4 0 0 1 4-4h12M7 20.5l-3-3 3-3M20 12.5v1a4 4 0 0 1-4 4H4"),
        "media-playlist-shuffle": lines("M16.5 3.5l3 3-3 3M3.5 6.5H7c4.5 0 5.5 11 10 11h2.5M16.5 14.5l3 3-3 3"
                                        "M3.5 17.5H7c1.5 0 2.5-1.2 3.3-2.8M13.7 9.3c.8-1.6 1.8-2.8 3.3-2.8h2.5"),
        "view-barcode-qr": tray(line("M5.5 4.5h4a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1z"
                                     "M14.5 4.5h4a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1z"
                                     "M5.5 13.5h4a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1z")
                                + dots(((14.4, 14.4), (19.2, 14.4), (16.8, 17), (14.4, 19.6), (19.2, 19.6)), 1)),
        "format-number-percent": lines("M7.5 5.3a2.2 2.2 0 1 1 0 4.4 2.2 2.2 0 0 1 0-4.4zM16.5 14.3a2.2 2.2 0 1 1 0 4.4 2.2 2.2 0 0 1 0-4.4zM18 5.5 6 18.5"),
        "draw-number": lines("M9.5 4 8 20M16 4l-1.5 16M4.5 9h15M4 15h15"),
        "network-connect": lines(PLUG),
        "network-disconnect": tray(line(PLUG) + line(SLASH)),
        "user-identity": lines("M12 4a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7zM5 20c.8-3.8 3.6-6 7-6s6.2 2.2 7 6"),
        "compass": lines(CIRCLE + "M15.5 8.5l-2 5-5 2 2-5z"),
        "bookmark-remove": lines("M7 3.5h10a1 1 0 0 1 1 1v16l-6-4-6 4v-16a1 1 0 0 1 1-1zM9.5 10h5"),
        # Menu categories: only the -symbolic names, the colorful ones stay Breeze.
        "applications-graphics-symbolic": tray(line("M12 3.5a8.5 8.5 0 0 0 0 17c1.4 0 2-1 1.6-2.1-.5-1.3.4-2.4 1.7-2.4h2.2"
                                                    "a3 3 0 0 0 3-3A8.5 8.5 0 0 0 12 3.5z")
                                               + dots(((8, 10.5), (11.5, 7.5), (15.5, 8.5)), 1.1)),
        "applications-internet-symbolic": lines(CIRCLE + "M3.5 12h17M12 3.5c2.3 2.3 3.5 5.2 3.5 8.5s-1.2 6.2-3.5 8.5"
                                                "c-2.3-2.3-3.5-5.2-3.5-8.5S9.7 5.8 12 3.5z"),
        "applications-multimedia-symbolic": lines("M9 17.5V6l10-2v11.5M6.5 15a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5z"
                                                  "M16.5 13a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5z"),
        "applications-office-symbolic": lines(PAGE_LINE + "M8.5 12h7M8.5 15.5h5"),
        "applications-development-symbolic": lines("M8 7 3 12l5 5M16 7l5 5-5 5M13.5 5l-3 14"),
        "applications-system-symbolic": lines("M8 6h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2z"
                                              "M10 3v3M14 3v3M10 18v3M14 18v3M3 10h3M3 14h3M18 10h3M18 14h3"),
        "applications-utilities-symbolic": lines("M4 9h16v9.5a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 18.5z"
                                                 "M9 9V6a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 1 15 6v3M4 13.5h16"),
        "applications-science-symbolic": lines("M9.5 3.5h5M10.5 3.5V9L5 18.5a1.3 1.3 0 0 0 1.1 2h11.8a1.3 1.3 0 0 0 1.1-2"
                                               "L13.5 9V3.5M7.5 14.5h9"),
        "applications-education-symbolic": lines("M2.5 9.5 12 5l9.5 4.5L12 14zM6.5 11.5V16c3.5 2.5 7.5 2.5 11 0v-4.5M21.5 9.5v5"),
        "applications-games-symbolic": tray(line(GAMEPAD) + dots(((15.5, 11), (17.3, 13)), 1)),
        "utilities-terminal-symbolic": lines(FRAME + "M7 9.5l3 2.5-3 2.5M12.5 15H17"),
        "office-calendar-symbolic": lines("M5.5 5h13a2 2 0 0 1 2 2v11.5a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"
                                          "M3.5 10h17M8 3v4M16 3v4"),
        "system-file-manager-symbolic": lines(FOLDER_LINE),
    }
    aliases = {
        "arrow-left": "go-previous", "arrow-right": "go-next", "arrow-up": "go-up", "arrow-down": "go-down",
        "go-previous-view": "go-previous", "go-next-view": "go-next", "go-parent-folder": "go-up",
        "go-up-skip": "go-top", "go-down-skip": "go-bottom",
        "system-search": "edit-find", "edit-clear-history": "edit-clear-all", "edit-entry": "document-edit",
        "edit-copy-path": "edit-copy", "edit-delete-remove": "edit-delete",
        "document-save-as": "document-save", "document-preview": "password-show-on",
        "view-visible": "password-show-on", "view-hidden": "password-show-off", "view-preview": "password-show-on",
        "view-sort": "view-sort-ascending", "view-list-text": "view-list-details", "view-list-compact": "view-list-details",
        "zoom-fit-best": "view-fullscreen", "dialog-close": "window-close", "tab-close": "window-close",
        "document-close": "window-close", "window-new": "tab-new", "dialog-ok-apply": "dialog-ok",
        "help-about": "dialog-information", "documentinfo": "dialog-information", "help-hint": "dialog-information",
        "system-help": "help-contents", "settings-configure": "configure", "open-menu": "application-menu",
        "view-more": "overflow-menu", "media-playlist-repeat-song": "media-playlist-repeat",
        "view-history": "document-open-recent", "edit-none": "dialog-cancel",
        "internet-web-browser": "applications-internet-symbolic",
        "applications-all-symbolic": "view-list-icons", "applications-other-symbolic": "view-more-horizontal",
        "applications-network-symbolic": "applications-internet-symbolic",
        "applications-toys-symbolic": "applications-games-symbolic",
        "preferences-system-symbolic": "configure",
    }
    for sub in ("arcade", "board", "card", "children", "logic", "strategy"):
        aliases[f"applications-games-{sub}-symbolic"] = "applications-games-symbolic"
    for sub in ("language", "mathematics", "miscellaneous"):
        aliases[f"applications-education-{sub}-symbolic"] = "applications-education-symbolic"
    return icons, aliases


# System Settings modules: paper cards with a glyph colored by group.
SHIELD = "M12 3l7 2.8v5.4c0 4.4-3 7.8-7 9.3-4-1.5-7-4.9-7-9.3V5.8z"
PERSON = "M12 4a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7zM5 20c.8-3.8 3.6-6 7-6s6.2 2.2 7 6"
WINDOWS = "M8 4.5h10.5a2 2 0 0 1 2 2V14M5.5 8h9a2 2 0 0 1 2 2v7.5a2 2 0 0 1-2 2h-9a2 2 0 0 1-2-2V10a2 2 0 0 1 2-2z"
GLOBE = CIRCLE + "M3.5 12h17M12 3.5c2.3 2.3 3.5 5.2 3.5 8.5s-1.2 6.2-3.5 8.5c-2.3-2.3-3.5-5.2-3.5-8.5S9.7 5.8 12 3.5z"
APP_WINDOW = FRAME + "M3.5 9h17"
PALETTE = [("s", "M12 3.5a8.5 8.5 0 0 0 0 17c1.4 0 2-1 1.6-2.1-.5-1.3.4-2.4 1.7-2.4h2.2a3 3 0 0 0 3-3A8.5 8.5 0 0 0 12 3.5z"),
           ("f", '<circle cx="8" cy="10.5" r="1.3"/><circle cx="11.5" cy="7.5" r="1.3"/><circle cx="15.5" cy="8.5" r="1.3"/>')]
PREF_GROUPS = {
    CLAY: {  # appearance
        "preferences-desktop-theme-global": PALETTE,
        "preferences-desktop-plasma-theme": [("s", FRAME + "M3.5 16h17")],
        "preferences-desktop-color": [("s", "M9 4.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9zM15 4.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9z"
                                           "M12 10a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9z")],
        "preferences-desktop-icons": [("s", "M5.5 4h3A1.5 1.5 0 0 1 10 5.5v3A1.5 1.5 0 0 1 8.5 10h-3A1.5 1.5 0 0 1 4 8.5v-3A1.5 1.5 0 0 1 5.5 4z"
                                           "M15.5 4h3A1.5 1.5 0 0 1 20 5.5v3a1.5 1.5 0 0 1-1.5 1.5h-3A1.5 1.5 0 0 1 14 8.5v-3A1.5 1.5 0 0 1 15.5 4z"
                                           "M5.5 14h3a1.5 1.5 0 0 1 1.5 1.5v3A1.5 1.5 0 0 1 8.5 20h-3A1.5 1.5 0 0 1 4 18.5v-3A1.5 1.5 0 0 1 5.5 14z"
                                           "M15.5 14h3a1.5 1.5 0 0 1 1.5 1.5v3a1.5 1.5 0 0 1-1.5 1.5h-3a1.5 1.5 0 0 1-1.5-1.5v-3a1.5 1.5 0 0 1 1.5-1.5z")],
        "preferences-desktop-cursors": [("s", "M6 3.5v15l4-4 2.8 6 2.5-1.2-2.8-5.8H18z")],
        "preferences-desktop-font": [("s", "M5.5 20.5 12 3.5l6.5 17M8 14h8")],
        "preferences-desktop-theme-applications": [("s", APP_WINDOW + "M7 13h6M7 16h4")],
        "preferences-desktop-theme-windowdecorations": [("s", APP_WINDOW), ("f", '<circle cx="17.3" cy="6.8" r="1"/>')],
        "preferences-desktop-wallpaper": [("s", FRAME + "M3.5 17l5-5 4 4 2.5-2.5 5.5 5.5"), ("f", '<circle cx="16" cy="8.5" r="1.6"/>')],
        "preferences-system-splash": [("s", FRAME), ("f", '<circle cx="12" cy="12" r="2.6"/>')],
        "preferences-desktop-animations": [("s", "M4 12h8M7 7.5h5M7 16.5h5M17 9a3 3 0 1 1 0 6 3 3 0 0 1 0-6z")],
        "preferences-desktop-effects": [("s", "M12 3.5l1.8 5.2 5.2 1.8-5.2 1.8L12 17.5l-1.8-5.2-5.2-1.8 5.2-1.8zM18.5 15.5v5M16 18h5")],
    },
    KRAFT_D: {  # workspace behavior
        "preferences-desktop": [("s", SCREEN)],
        "preferences-desktop-activities": [("s", "M8 4h10a2 2 0 0 1 2 2v10M6 8h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2z")],
        "preferences-desktop-virtual": [("s", FRAME + "M12 4.5v15M3.5 12h17")],
        "preferences-desktop-notification-bell": [("s", "M6.5 16.5V11a5.5 5.5 0 0 1 11 0v5.5l1.5 2h-14zM10.2 20.8a1.9 1.9 0 0 0 3.6 0M12 3.5v2")],
        "preferences-system-tabbox": [("s", FRAME + "M8 9.5h8v5H8z")],
        "preferences-system-windows": [("s", WINDOWS)],
        "preferences-system-session-services": [("s", CIRCLE + "M10 8.5v7l5.5-3.5z")],
        "preferences-desktop-search": [("s", LENS)],
        "preferences-desktop-feedback": [("s", "M5.5 4.5h13a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H11l-4.5 3.5v-3.5h-1a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2z")],
        "preferences-desktop-keyboard-shortcut": [("s", "M5 6.5h14a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2zM8 14h8"),
                                                  ("f", '<circle cx="7" cy="10.3" r="1"/><circle cx="10.3" cy="10.3" r="1"/>'
                                                        '<circle cx="13.7" cy="10.3" r="1"/><circle cx="17" cy="10.3" r="1"/>')],
        "preferences-desktop-default-applications": [("s", STAR)],
        "preferences-desktop-filetype-association": [("s", PAGE_LINE + "M8.5 12h7M8.5 15.5h5")],
        "preferences-web-browser-shortcuts": [("s", GLOBE)],
        "preferences-desktop-locale": [("s", "M4 5.5h9M8.5 3.5v2M6 5.5c0 4 3 7.5 6 8.5M11 5.5c0 4-3 7.5-6 9M12.5 20.5l4-9 4 9M13.8 17.5h5.4")],
        "preferences-system-time": [("s", "M12 3.5a8.5 8.5 0 1 1 0 17 8.5 8.5 0 0 1 0-17zM12 7.5V12l3 2")],
        "preferences-desktop-accessibility": [("s", CIRCLE + "M7.5 9.5l4.5 1 4.5-1M12 10.5v3l-2.5 4M12 13.5l2.5 4"),
                                              ("f", '<circle cx="12" cy="7" r="1.3"/>')],
    },
    SKY: {  # hardware
        "preferences-desktop-display": [("s", SCREEN)],
        "preferences-desktop-mouse": [("s", "M12 3.5a5.5 5.5 0 0 1 5.5 5.5v6a5.5 5.5 0 0 1-11 0V9A5.5 5.5 0 0 1 12 3.5zM12 3.5v5")],
        "preferences-desktop-keyboard": [("s", "M5 6.5h14a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2zM8 14h8"),
                                         ("f", '<circle cx="7" cy="10.3" r="1"/><circle cx="10.3" cy="10.3" r="1"/>'
                                               '<circle cx="13.7" cy="10.3" r="1"/><circle cx="17" cy="10.3" r="1"/>')],
        "preferences-desktop-touchpad": [("s", "M6 4.5h12A2 2 0 0 1 20 6.5v11a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-11a2 2 0 0 1 2-2zM4 15h16M12 15v4.5")],
        "preferences-desktop-tablet": [("s", "M6.5 3.5h11A2.5 2.5 0 0 1 20 6v12a2.5 2.5 0 0 1-2.5 2.5h-11A2.5 2.5 0 0 1 4 18V6a2.5 2.5 0 0 1 2.5-2.5z"),
                                       ("f", '<circle cx="12" cy="17.5" r="1"/>')],
        "preferences-desktop-touchscreen": [("s", "M6.5 3.5h11A2.5 2.5 0 0 1 20 6v12a2.5 2.5 0 0 1-2.5 2.5h-11A2.5 2.5 0 0 1 4 18V6a2.5 2.5 0 0 1 2.5-2.5z"
                                                  "M12 9a3 3 0 1 1 0 6 3 3 0 0 1 0-6z")],
        "preferences-desktop-sound": [("s", "M3.5 9.5h3l4.5-4v13l-4.5-4h-3zM13.8 9.2a4 4 0 0 1 0 5.6M16 7a7 7 0 0 1 0 10")],
        "preferences-desktop-peripherals": [("s", PLUG)],
        "preferences-desktop-gaming": [("s", "M7.5 7.5h9a4.5 4.5 0 0 1 4.4 5.4l-.8 3.9a2.2 2.2 0 0 1-3.8 1l-2.1-2.3h-4.4"
                                             "l-2.1 2.3a2.2 2.2 0 0 1-3.8-1l-.8-3.9A4.5 4.5 0 0 1 7.5 7.5zM8 10.5v3M6.5 12h3"),
                                       ("f", '<circle cx="15.5" cy="11" r="1"/><circle cx="17.3" cy="13" r="1"/>')],
        "preferences-system-power-management": [("s", "M5 7h12a2.5 2.5 0 0 1 2.5 2.5v5A2.5 2.5 0 0 1 17 17H5a2.5 2.5 0 0 1-2.5-2.5v-5"
                                                      "A2.5 2.5 0 0 1 5 7zM21.7 10.5v3"), ("f", '<path d="M12.9 8.2 8.9 12.6h3l-1 3.2 4.1-4.5h-3z"/>')],
        "preferences-system-bluetooth": [("s", BLUETOOTH)],
        "preferences-system-disks": [("s", HDD), ("f", '<circle cx="17.3" cy="15" r="1"/>')],
    },
    OLIVE: {  # network
        "preferences-system-network": [("s", GLOBE)],
        "preferences-system-network-connection": [("s", "M3.2 9.7a12.5 12.5 0 0 1 17.6 0M6.3 13a8 8 0 0 1 11.4 0M9.3 16.2a3.6 3.6 0 0 1 5.4 0"),
                                                  ("f", '<circle cx="12" cy="19.3" r="1.4"/>')],
        "preferences-system-network-proxy": [("s", SHIELD + "M9 12l2 2 4-4")],
        "preferences-online-accounts": [("s", "M7 18.5h10a4 4 0 0 0 .5-8 5.5 5.5 0 0 0-10.5-1.5A4.5 4.5 0 0 0 7 18.5z")],
    },
    FIG: {  # users and security
        "preferences-desktop-user": [("s", PERSON)],
        "preferences-system-users": [("s", "M9.5 4a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7zM3 20c.8-3.8 3.4-6 6.5-6s5.7 2.2 6.5 6"
                                           "M15.5 4.3a3.3 3.3 0 0 1 0 6.4M18 14.6c1.5.8 2.6 2.6 3 5.4")],
        "preferences-desktop-user-password": [("s", "M8 8a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM12 12h8.5v3M17.5 12v2.5")],
        "preferences-system-login": [("s", "M14 4.5h4a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2h-4M4 12h11M11 8l4 4-4 4")],
        "preferences-security": [("s", SHIELD + "M9 12l2 2 4-4")],
    },
}
PREF_ALIASES = {
    "preferences-desktop-display-randr": "preferences-desktop-display",
    "preferences-desktop-font-installer": "preferences-desktop-font",
    "preferences-desktop-multimedia": "preferences-desktop-sound",
    "preferences-system-windows-actions": "preferences-system-windows",
    "preferences-desktop-baloo": "preferences-desktop-search",
    "plasma-search": "preferences-desktop-search",
}
for _color, _group in PREF_GROUPS.items():
    for _name, _parts in _group.items():
        GLYPHS["pref:" + _name] = [(kind, data, _color) for kind, data in _parts]


# File emblems (Dolphin overlays): a colored rounded square with an Ivory glyph, 16 grid.
NEG = "#B5473A"
EMBLEMS = {
    "emblem-added": (OLIVE, "M8 4.5v7M4.5 8h7"),
    "emblem-checked": (OLIVE, "M4.5 8.3l2.3 2.3 4.7-4.9"),
    "emblem-success": (OLIVE, "M4.5 8.3l2.3 2.3 4.7-4.9"),
    "emblem-error": (NEG, "M5.5 5.5l5 5M10.5 5.5l-5 5"),
    "emblem-unavailable": (GREY_D, "M5.5 5.5l5 5M10.5 5.5l-5 5"),
    "emblem-remove": (SKY, "M4.5 8h7"),
    "emblem-important": (KRAFT_D, "M8 4.3v4.4M8 11.4v.3"),
    "emblem-warning": (KRAFT_D, "M8 4.3v4.4M8 11.4v.3"),
    "emblem-information": (SKY, "M8 7.4v4.3M8 4.6v.3"),
    "emblem-question": (HEATHER_D, "M6.3 6.2a1.8 1.8 0 1 1 2.5 1.6c-.5.2-.8.6-.8 1.1v.4M8 11.6v.3"),
    "emblem-locked": (KRAFT_D, "M5.2 7.5h5.6v4H5.2zM6.3 7.5V6a1.7 1.7 0 0 1 3.4 0v1.5"),
    "emblem-readonly": (GREY_D, "M5.2 7.5h5.6v4H5.2zM6.3 7.5V6a1.7 1.7 0 0 1 3.4 0v1.5"),
    "emblem-encrypted-locked": (SLATE_SOFT, "M5.2 7.5h5.6v4H5.2zM6.3 7.5V6a1.7 1.7 0 0 1 3.4 0v1.5"),
    "emblem-unlocked": (GREY_D, "M5.2 7.5h5.6v4H5.2zM6.3 7.5V6a1.7 1.7 0 0 1 3.3-.6"),
    "emblem-encrypted-unlocked": (GREY_D, "M5.2 7.5h5.6v4H5.2zM6.3 7.5V6a1.7 1.7 0 0 1 3.3-.6"),
    "emblem-mounted": (OLIVE, "M6.2 4v2M9.8 4v2M4.8 6h6.4v1.5a3.2 3.2 0 0 1-6.4 0zM8 10.7V12"),
    "emblem-unmounted": (GREY_D, "M6.2 4v2M9.8 4v2M4.8 6h6.4v1.5a3.2 3.2 0 0 1-6.4 0zM8 10.7V12"),
    "emblem-pause": (GREY_D, "M6.3 5v6M9.7 5v6"),
    "emblem-shared": (SKY, "M10.3 5.2 5.7 8l4.6 2.8"),
    "emblem-symbolic-link": (SLATE_SOFT, "M5.5 10.5l5-5M6.8 5.5h3.7v3.7"),
}
EMBLEM_FILLED = {"emblem-favorite": (CLAY, "M8 3.6l1.3 2.7 3 .4-2.2 2.1.5 3L8 10.4l-2.6 1.4.5-3-2.2-2.1 3-.4z")}


EMBLEM_DOTS = {"emblem-shared": ((10.5, 4.8), (5.3, 8), (10.5, 11.2))}


def emblem(color, d, filled=False, dots=()):
    mark = (f'<path d="{d}" fill="{IVORY}"/>\n' if filled else
            f'<path d="{d}" fill="none" stroke="{IVORY}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>\n')
    mark += "".join(f'<circle cx="{x}" cy="{y}" r="1.7" fill="{IVORY}"/>\n' for x, y in dots)
    return svg(16, rect(1, 1, 14, 14, 3.5, color) + mark)


# Display switcher OSD (Meta+P): line monitors on a 64 grid in the text color, Clay marks.
def osd_screen(x, y, w, h, op=1):
    cx = x + w / 2
    return line(f"M{x + 3} {y}h{w - 6}a3 3 0 0 1 3 3v{h - 6}a3 3 0 0 1-3 3h-{w - 6}a3 3 0 0 1-3-3v-{h - 6}a3 3 0 0 1 3-3z"
                f"M{cx} {y + h}v5M{cx - 7} {y + h + 5}h14", op, sw=2.2)


def osd_laptop(x, y, w, h, op=1):
    return line(f"M{x + 3} {y}h{w - 6}a3 3 0 0 1 3 3v{h - 3}h-{w}v-{h - 3}a3 3 0 0 1 3-3zM{x - 4} {y + h}h{w + 8}l-2 4h-{w + 4}z",
                op, sw=2.2)


def osd(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">\n{TRAY_STYLE}{body}</svg>\n'


def accent(d, k=1, at=None):
    """Clay stroke; with at=(x, y) a 24-grid glyph is scaled by k and centered there."""
    t = f' transform="translate({at[0]} {at[1]}) scale({k}) translate(-12 -12)"' if at else ""
    return (f'<path d="{d}"{t} fill="none" stroke="{CLAY}" stroke-width="{2.6 / k:g}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>\n')


def osd_icons():
    off = "M{0} {1}l8 8M{2} {1}l-8 8"
    return {
        "osd-duplicate": osd(osd_screen(20, 10, 36, 24, .45) + osd_screen(8, 20, 36, 24) + accent("M18 32h16")),
        "osd-sbs-left": osd(osd_screen(4, 16, 26, 20) + osd_screen(34, 16, 26, 20, .55) + accent("M21 26h-9M15 22l-4 4 4 4")),
        "osd-sbs-sright": osd(osd_screen(4, 16, 26, 20, .55) + osd_screen(34, 16, 26, 20) + accent("M43 26h9M49 22l4 4-4 4")),
        "osd-shutd-laptop": osd(osd_screen(22, 8, 36, 26) + osd_laptop(10, 34, 22, 14, .45)
                                + accent(off.format(17, 37, 25))),
        "osd-shutd-screen": osd(osd_screen(22, 8, 36, 26, .45) + osd_laptop(10, 34, 22, 14)
                                + accent(off.format(36, 17, 44))),
        "osd-rotate-normal": osd(osd_screen(10, 12, 44, 30) + accent("M32 33V20M27 25l5-5 5 5")),
        "osd-rotate-cw": osd(osd_screen(10, 12, 44, 30) + accent("M19.5 12a7.5 7.5 0 1 1-2.2-5.3M19.5 4v4.5H15", 1.25, (32, 27))),
        "osd-rotate-ccw": osd(osd_screen(10, 12, 44, 30) + accent("M4.5 12a7.5 7.5 0 1 0 2.2-5.3M4.5 4v4.5H9", 1.25, (32, 27))),
        "osd-rotate-flip": osd(osd_screen(10, 12, 44, 30) + accent("M32 18v18M27 23l5-5 5 5M27 31l5 5 5-5")),
    }


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
    # "scalable" serves every size above 64 (Kate's welcome page, About dialogs).
    for size in (16, 22, 24, 32, 48, 64, "scalable"):
        write("apps", size, "systemsettings", settings())
        alias("apps", size, "preferences-system", "systemsettings")
        write("apps", size, "org.kde.dolphin", dolphin())
        for name, (g, color) in APPS.items():
            write("apps", size, name, app(g, color))
        for name, target in APP_ALIASES.items():
            alias("apps", size, name, target)
        for group in PREF_GROUPS.values():
            for name in group:
                # Small sizes drop the card: a full-size colored glyph reads better in lists.
                write("apps", size, name, svg(24, glyph("pref:" + name, 12, 12, 21, 1.6)) if size != "scalable" and size <= 24
                      else tile(glyph("pref:" + name, 16, 16, 17, 1.7)))
        for name, target in PREF_ALIASES.items():
            alias("apps", size, name, target)
    for name, (color, d) in EMBLEMS.items():
        write("emblems", "scalable", name, emblem(color, d, dots=EMBLEM_DOTS.get(name, ())))
    for name, (color, d) in EMBLEM_FILLED.items():
        write("emblems", "scalable", name, emblem(color, d, filled=True))
    for name, content in osd_icons().items():
        write("applets", "scalable", name, content)
    for ctx, make in (("status", tray_icons), ("actions", action_icons)):
        d = ROOT / ctx / "scalable"
        if d.exists():
            for old in d.iterdir():
                old.unlink()
        icons, aliases = make()
        for name, content in icons.items():
            write(ctx, "scalable", name, content)
        for name, target in aliases.items():
            alias(ctx, "scalable", name, target)
        for name in [*icons, *aliases]:
            if not name.endswith("-symbolic"):
                alias(ctx, "scalable", f"{name}-symbolic", name)


if __name__ == "__main__":
    main()
