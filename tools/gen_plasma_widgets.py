#!/usr/bin/env python3
"""Generate Clay Plasma style frames: tasks, button and lineedit.

Frames are 9-slice sets of pieces drawn from rounded rects, radius 6 to match
Klassy windows and Qt widgets. Colors come from ColorScheme classes, so one file
serves Clay and Clay Dark (clay-dark falls back to clay). Content margins
(-hint-*-margin) keep Breeze's values so layouts don't move.

Tasks: a rounded pill inset from the panel edges with a bar on the screen-side
edge: running = faint bar, hover = soft fill, active = soft fill + accent bar.

Run from anywhere: python3 tools/gen_plasma_widgets.py
"""
import gzip
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "payload/plasma/desktoptheme/clay/widgets"

STYLE = ('<style type="text/css" id="current-color-scheme">'
         ".ColorScheme-Text{color:#141413}.ColorScheme-ButtonText{color:#141413}"
         ".ColorScheme-ButtonBackground{color:#FAF9F5}.ColorScheme-ButtonHover{color:#C6613F}"
         ".ColorScheme-ButtonFocus{color:#D97757}.ColorScheme-ViewText{color:#141413}"
         ".ColorScheme-ViewBackground{color:#FAF9F5}.ColorScheme-ViewHover{color:#C6613F}"
         ".ColorScheme-ViewFocus{color:#D97757}.ColorScheme-NeutralText{color:#A06A2C}"
         ".ColorScheme-PositiveText{color:#5E7045}</style>\n")
PIECES = ["topleft", "top", "topright", "left", "center", "right", "bottomleft", "bottom", "bottomright"]


def paint(cls, op):
    return f'fill="currentColor" class="ColorScheme-{cls}" opacity="{op:g}"'


def mapper(name, c):
    """Mirror topleft-local coordinates into the given piece."""
    fx = name.endswith("right")
    fy = name.startswith("bottom")
    return (lambda x, y: (c - x if fx else x, c - y if fy else y)), fx != fy


def corner(c, i, r, w=None):
    """Topleft corner of a rounded rect at inset i (fill, or a ring of width w)."""
    ops = [("M", i, c), ("L", i, i + r), ("A", r, 1, i + r, i), ("L", c, i)]
    if w is None:
        ops += [("L", c, c)]
    else:
        ops += [("L", c, i + w), ("L", i + r, i + w), ("A", r - w, 0, i + w, i + r), ("L", i + w, c)]
    return ops


def render(ops, name, c, ox, oy):
    m, flip = mapper(name, c)
    out = []
    for op in ops:
        if op[0] == "A":
            _, r, sweep, x, y = op
            x, y = m(x, y)
            out.append(f"A{r:g} {r:g} 0 0 {sweep ^ flip} {x + ox:g} {y + oy:g}")
        else:
            x, y = m(op[1], op[2])
            out.append(f"{op[0]}{x + ox:g} {y + oy:g}")
    return "".join(out) + "z"


def edge(name, c, i, w):
    """Edge piece of the rect as (x, y, w, h); w=None fills to the inner side."""
    h = c - i if w is None else w
    return {"top": (0, i, c, h), "bottom": (0, c - i - h, c, h),
            "left": (i, 0, h, c), "right": (c - i - h, 0, h, c)}[name]


def frame(prefix, c, layers, ox, oy, extra=None):
    """layers: (kind, inset, radius, width, cls, opacity); kind = fill | ring.
    extra(name, x, y) may add markup to a piece."""
    out = []
    for k, name in enumerate(PIECES):
        x, y = ox + (k % 3) * c, oy + (k // 3) * c
        body = f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="none"/>'
        for kind, i, r, w, cls, op in layers:
            if name == "center":
                if kind == "fill":
                    body += f'<rect x="{x}" y="{y}" width="{c}" height="{c}" {paint(cls, op)}/>'
                continue
            width = w if kind == "ring" else None
            if name in ("top", "bottom", "left", "right"):
                ex, ey, ew, eh = edge(name, c, i, width)
                body += f'<rect x="{x + ex:g}" y="{y + ey:g}" width="{ew:g}" height="{eh:g}" {paint(cls, op)}/>'
            else:
                body += f'<path d="{render(corner(c, i, r, width), name, c, x, y)}" {paint(cls, op)}/>'
        if extra:
            body += extra(name, x, y)
        out.append(f'<g id="{prefix}-{name}">{body}</g>')
    return "\n".join(out)


def hints(prefix, margins, x, y):
    """Margin hint elements; margins = (top, bottom, left, right), 0 -> ~0."""
    t, b, l, r = (m or .001 for m in margins)
    return (f'<rect id="{prefix}-hint-top-margin" x="{x}" y="{y}" width="2" height="{t:g}" fill="none"/>'
            f'<rect id="{prefix}-hint-bottom-margin" x="{x + 3}" y="{y}" width="2" height="{b:g}" fill="none"/>'
            f'<rect id="{prefix}-hint-left-margin" x="{x + 6}" y="{y}" width="{l:g}" height="2" fill="none"/>'
            f'<rect id="{prefix}-hint-right-margin" x="{x + 14}" y="{y}" width="{r:g}" height="2" fill="none"/>')


def flag(name, x, y):
    return f'<rect id="{name}" x="{x}" y="{y}" width="2" height="2" fill="none"/>'


def write(name, parts, w, h):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">\n{STYLE}' + "\n".join(parts) + "\n</svg>\n"
    (OUT / f"{name}.svgz").write_bytes(gzip.compress(svg.encode(), mtime=0))


R = 6
BORDER = 1
FOCUS = 2


def button():
    c, cf = 7, 9  # cf: focus pieces reach FOCUS px outside the button
    sets = [
        ("shadow", 8, [], (3, 3, 3, 3)),
        ("mask-normal", c, [("fill", 0, R, None, "ButtonText", 1)], None),
        ("normal", c, [("fill", 0, R, None, "ButtonBackground", 1), ("ring", 0, R, BORDER, "ButtonText", .16)], (6, 6, 6, 6)),
        ("pressed", c, [("fill", 0, R, None, "ButtonBackground", 1), ("fill", 0, R, None, "ButtonText", .1),
                        ("ring", 0, R, BORDER, "ButtonText", .22)], (6, 6, 6, 6)),
        ("hover", c, [("ring", 0, R, BORDER, "ButtonHover", .9)], (0, 0, 0, 0)),
        ("focus", cf, [("ring", 0, R + FOCUS, FOCUS, "ButtonFocus", .55)], (2, 2, 2, 2)),
        ("toolbutton-hover", c, [("fill", 0, R, None, "ButtonText", .08)], (4, 4, 4, 4)),
        ("toolbutton-pressed", c, [("fill", 0, R, None, "ButtonText", .14)], (4, 4, 4, 4)),
        ("toolbutton-focus", cf, [("ring", 0, R + FOCUS, FOCUS, "ButtonFocus", .55)], (2, 2, 2, 2)),
    ]
    parts, y = [], 0
    for prefix, size, layers, margins in sets:
        parts.append(frame(prefix, size, layers, 0, y))
        if margins:
            parts.append(hints(prefix, margins, 40, y))
        y += 3 * size + 4
    parts += [flag("normal-hint-compose-over-border", 70, 0), flag("pressed-hint-compose-over-border", 74, 0)]
    write("button", parts, 80, y)


def lineedit():
    c, cf = 7, 9
    sets = [
        ("base", c, [("fill", 0, R, None, "ViewBackground", 1), ("ring", 0, R, BORDER, "ViewText", .18)], (6, 6, 6, 6)),
        ("hover", c, [("ring", 0, R, BORDER, "ViewHover", .9)], (0, 0, 0, 0)),
        ("focus", c, [("ring", 0, R, BORDER, "ViewFocus", 1)], (0, 0, 0, 0)),
        ("focusframe", cf, [("ring", 0, R + FOCUS, FOCUS, "ViewFocus", .45)], (2, 2, 2, 2)),
    ]
    parts, y = [], 0
    for prefix, size, layers, margins in sets:
        parts.append(frame(prefix, size, layers, 0, y))
        parts.append(hints(prefix, margins, 40, y))
        y += 3 * size + 4
    parts += [flag("hint-tile-center", 70, 0), flag("hint-focus-over-base", 74, 0)]
    write("lineedit", parts, 80, y)


# Tasks: state -> (fill class, fill opacity, bar class, bar opacity)
TASK_C, TASK_INSET, TASK_BAR = 8, 2, 2
TASK_STATES = {
    "normal": (None, 0, "Text", .35),
    "minimized": (None, 0, "Text", .18),
    "hover": ("Text", .07, "Text", .5),
    "focus": ("Text", .11, "ButtonFocus", 1),
    "attention": ("NeutralText", .16, "NeutralText", 1),
    "progress": ("PositiveText", .2, None, 0),
    # Hovered variants Plasma looks up before plain "hover".
    "launcher-hover": ("Text", .07, None, 0),
    "focus-hover": ("Text", .15, "ButtonFocus", 1),
    "attention-hover": ("NeutralText", .22, "NeutralText", 1),
}
# location prefix -> side of the pill that faces the screen edge
TASK_SIDES = {"": "bottom", "north-": "top", "west-": "left", "east-": "right"}


def tasks():
    c, i, off = TASK_C, TASK_INSET, TASK_INSET + 1
    bars = {
        "bottom": lambda x, y: (x, y + c - off - TASK_BAR, c, TASK_BAR),
        "top": lambda x, y: (x, y + off, c, TASK_BAR),
        "left": lambda x, y: (x + off, y, TASK_BAR, c),
        "right": lambda x, y: (x + c - off - TASK_BAR, y, TASK_BAR, c),
    }
    parts = []
    for row, (prefix, side) in enumerate(TASK_SIDES.items()):
        for col, (state, (fcls, fop, bcls, bop)) in enumerate(TASK_STATES.items()):
            def bar(name, x, y, bcls=bcls, bop=bop, side=side):
                if not bcls or name != side:
                    return ""
                bx, by, w, h = bars[side](x, y)
                return f'<rect x="{bx}" y="{by}" width="{w}" height="{h}" {paint(bcls, bop)}/>'
            layers = [("fill", i, 5, None, fcls, fop)] if fcls else []
            parts.append(frame(prefix + state, c, layers, col * (3 * c + 4), row * (3 * c + 4), bar))
    y = len(TASK_SIDES) * (3 * c + 4)
    parts.append(hints("normal", (4, 4, 4, 4), 0, y))
    write("tasks", parts, len(TASK_STATES) * (3 * c + 4), y + 6)


if __name__ == "__main__":
    tasks()
    button()
    lineedit()
