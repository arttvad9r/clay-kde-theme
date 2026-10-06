#!/usr/bin/env python3
"""Generate the Clay Aurorae window decoration.

Titlebar: window background, hairline outline, rounded corners (radius 8), the bottom
edge is a 5 px border so the square client does not cover them. Buttons: thin Text-colored glyphs without a background; a soft
fill appears on hover, the close button turns Clay on hover. Colors come from
ColorScheme classes, so one theme serves light and dark.

Run from anywhere: python3 tools/gen_aurorae.py
"""
import gzip
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "payload/aurorae/themes/Clay"

STYLE = ('<style type="text/css" id="current-color-scheme">'
         ".ColorScheme-Text{color:#141413}.ColorScheme-Background{color:#FAF9F5}"
         "</style>\n")
CLAY = "#D97757"
ON_CLAY = "#FAF9F5"

R = 8        # corner radius
TOP = 32     # title height incl. edges
M = 8        # side/bottom slice size (client covers all but the outer 1 px)
W = 24       # button box


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
            f'<defs>{STYLE}</defs>\n{body}</svg>\n')


def write(name, text):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_bytes(gzip.compress(text.encode(), mtime=0)) if name.endswith("z") \
        else (OUT / name).write_text(text)


def frame(prefix, rounded):
    """3x3 slices of the titlebar frame; origin of the sheet is (0, 0)."""
    r = R if rounded else 0
    o = 'class="ColorScheme-Text" fill="none" stroke="currentColor" stroke-opacity=".16"'
    f = 'class="ColorScheme-Background" fill="currentColor"'
    # Middle slices are 1 px so tiling them can't leave antialiasing seams.
    xs, ws = [0, M, M + 1], [M, 1, M]
    ys, hs = [0, TOP, TOP + 1], [TOP, 1, M]
    names = [["topleft", "top", "topright"], ["left", "center", "right"], ["bottomleft", "bottom", "bottomright"]]
    sizes = {names[j][i]: (xs[i], ys[j], ws[i], hs[j]) for j in range(3) for i in range(3)}
    out = []
    for name, (x, y, w, h) in sizes.items():
        # Fill: the piece rectangle, with the outer top corner cut round.
        if name == "topleft":
            d = f"M{x} {y + h}V{y + r}" + (f"A{r} {r} 0 0 1 {x + r} {y}" if r else f"V{y}") + f"H{x + w}V{y + h}z"
            line = f"M{x + .5} {y + h}V{y + r}" + (f"A{r - .5} {r - .5} 0 0 1 {x + r} {y + .5}" if r else f"V{y + .5}") + f"H{x + w}"
        elif name == "topright":
            d = f"M{x} {y}H{x + w - r}" + (f"A{r} {r} 0 0 1 {x + w} {y + r}" if r else f"H{x + w}") + f"V{y + h}H{x}z"
            line = f"M{x} {y + .5}H{x + w - r}" + (f"A{r - .5} {r - .5} 0 0 1 {x + w - .5} {y + r}" if r else f"H{x + w - .5}") + f"V{y + h}"
        elif name == "bottomleft" and r:
            d = f"M{x} {y}H{x + w}V{y + h}H{x + r}A{r} {r} 0 0 1 {x} {y + h - r}z"
            line = f"M{x + .5} {y}V{y + h - r}A{r - .5} {r - .5} 0 0 0 {x + r} {y + h - .5}H{x + w}"
        elif name == "bottomright" and r:
            d = f"M{x} {y}H{x + w}V{y + h - r}A{r} {r} 0 0 1 {x + w - r} {y + h}H{x}z"
            line = f"M{x} {y + h - .5}H{x + w - r}A{r - .5} {r - .5} 0 0 0 {x + w - .5} {y + h - r}V{y}"
        else:
            d = f"M{x} {y}h{w}v{h}h-{w}z"
            line = {"top": f"M{x} {y + .5}h{w}",
                    "left": f"M{x + .5} {y}v{h}", "right": f"M{x + w - .5} {y}v{h}",
                    "bottomleft": f"M{x + .5} {y}v{h - .5}h{w - .5}",
                    "bottom": f"M{x} {y + h - .5}h{w}",
                    "bottomright": f"M{x} {y + h - .5}h{w - .5}V{y}"}.get(name)
        out.append(f'<g id="{prefix}-{name}"><path {f} d="{d}"/>'
                   + (f'<path {o} d="{line}"/>' if line else "") + "</g>\n")
    return "".join(out)


def decoration():
    body = frame("decoration", True) + frame("decoration-maximized", False)
    # Blur/shape mask: the full 3x3 frame, same slicing.
    body += frame("mask", True).replace('class="ColorScheme-Background" fill="currentColor"', 'fill="#000"')
    write("decoration.svgz", svg(2 * M + 1, TOP + M + 1, body))


# Glyphs, drawn in a W x W box around (12, 12).
GLYPH = {
    "close": "M8.5 8.5L15.5 15.5M15.5 8.5L8.5 15.5",
    "minimize": "M8 12H16",
    "maximize": '<rect x="8" y="8" width="8" height="8" rx="1.5"/>',
    "restore": ('<path d="M10 10V8.5Q10 7.5 11 7.5H15.5Q16.5 7.5 16.5 8.5V13Q16.5 14 15.5 14H14"/>'
                '<rect x="7.5" y="10" width="6.5" height="6.5" rx="1.5"/>'),
    "alldesktops": '<circle cx="12" cy="12" r="3"/>',
    "keepabove": "M8.5 13.5L12 10L15.5 13.5",
    "keepbelow": "M8.5 10.5L12 14L15.5 10.5",
    "shade": "M8 8.5H16M8.5 12L12 15.5L15.5 12",
    "help": '<circle cx="12" cy="12" r="4.5"/><path d="M10.6 10.8Q10.6 9.6 12 9.6T13.4 10.8Q13.4 11.6 12 12.2V12.8"/>'
            '<circle cx="12" cy="14.4" r=".5"/>',
    "appmenu": "M8 9H16M8 12H16M8 15H16",
}
# state -> (glyph opacity, background opacity)
STATES = ["active", "inactive", "hover", "hover-inactive", "pressed", "pressed-inactive",
          "deactivated", "deactivated-inactive"]
LOOK = {"active": (1, 0), "inactive": (.45, 0), "hover": (1, .1), "hover-inactive": (.7, .06),
        "pressed": (1, .18), "pressed-inactive": (.7, .12), "deactivated": (.3, 0), "deactivated-inactive": (.2, 0)}


def button(name):
    g = GLYPH[name]
    body = []
    for i, st in enumerate(STATES):
        gop, bop = LOOK[st]
        close_hot = name == "close" and st in ("hover", "pressed")
        bg = ""
        if close_hot:
            bg = f'<rect x="1" y="1" width="{W - 2}" height="{W - 2}" rx="6" fill="{CLAY}" opacity="{1 if st == "hover" else .85}"/>'
        elif bop:
            bg = (f'<rect x="1" y="1" width="{W - 2}" height="{W - 2}" rx="6" class="ColorScheme-Text" '
                  f'fill="currentColor" opacity="{bop}"/>')
        paint = (f'fill="none" stroke="{ON_CLAY}"' if close_hot
                 else 'class="ColorScheme-Text" fill="none" stroke="currentColor"')
        shape = f'<path d="{g}"/>' if g.startswith("M") else g
        body.append(f'<g id="{st}-center" transform="translate(0 {i * W})"><rect width="{W}" height="{W}" fill="none"/>'
                    f'{bg}<g {paint} stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" '
                    f'opacity="{gop}">{shape}</g></g>\n')
    write(f"{name}.svgz", svg(W, W * len(STATES), "".join(body)))


def metadata():
    write("metadata.desktop", """[Desktop Entry]
Name=Clay
Comment=Warm minimal window decoration
X-KDE-PluginInfo-Name=Clay
X-KDE-PluginInfo-Author=artt
X-KDE-PluginInfo-Version=1.0
X-KDE-PluginInfo-License=GPL-3.0-or-later
""")
    write("Clayrc", f"""[General]
TitleAlignment=Left
TitleVerticalAlignment=Center
Animation=150
ActiveTextColor=20,20,19,255
InactiveTextColor=20,20,19,140
UseTextShadow=false
ActiveTextShadowColor=255,255,255,255
InactiveTextShadowColor=255,255,255,255
TextShadowOffsetX=0
TextShadowOffsetY=0
HaloActive=false
HaloInactive=false
LeftButtons=M
RightButtons=IAX
Shadow=true
DecorationPosition=0

[Layout]
BorderLeft=1
BorderRight=1
BorderBottom=5
BorderTop=0
TitleEdgeTop=4
TitleEdgeBottom=4
TitleEdgeLeft=8
TitleEdgeRight=8
TitleEdgeTopMaximized=0
TitleEdgeBottomMaximized=0
TitleEdgeLeftMaximized=0
TitleEdgeRightMaximized=0
TitleBorderLeft=4
TitleBorderRight=4
TitleHeight={TOP - 8}
ButtonWidth={W}
ButtonHeight={W}
ButtonSpacing=2
ButtonMarginTop=0
ExplicitButtonSpacer=8
PaddingTop=0
PaddingBottom=0
PaddingRight=0
PaddingLeft=0
""")


if __name__ == "__main__":
    decoration()
    for n in GLYPH:
        button(n)
    metadata()
    print(f"wrote {OUT}")
