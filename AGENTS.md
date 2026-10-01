# Clay KDE Theme

Warm minimal theme for KDE Plasma 6 (Light/Dark): color schemes, Plasma style, global themes, icon overlay, cursors, Kate syntax themes, wallpapers, splash, logout, KWin Alt+Tab, Klassy preset, kitty/fastfetch extras. User-facing docs are in `README.md` (Russian).

## Layout
- `payload/` — everything installed into `~/.local/share` (`install.sh` replaces each component wholesale, with a backup).
- `payload/icons/clay-icons` — overlay icon theme, `Inherits=breeze`.
- `tools/gen_icons.py` — generates folders, mimetypes, devices, app tiles, tray (`status/scalable`) and action (`actions/scalable`) icons, Settings modules (`preferences-*`: glyph ≤24 px, card above), emblems, Meta+P OSD (`applets/scalable`). Edit the generator, not the SVGs. `actions/<size>/system-*` are hand-made.
- `tools/gen_plasma_widgets.py` — Plasma style `tasks`, `button`, `lineedit` (9-slice, radius 6; margin hints copied from Breeze). Other widgets are hand-tweaked Breeze copies.
- `tools/gen_cursors.py` — `clay-cursors` recolored from installed `breeze_cursors` (needs rsvg-convert, magick).
- `payload/org.kde.syntax-highlighting/themes` — Kate/KWrite themes, selected by `apply.sh`.
- `scripts/apply.sh` via `apply-light.sh` / `apply-dark.sh` — switches Plasma settings.

## Commands
- Regenerate: `python3 tools/gen_icons.py`, `python3 tools/gen_plasma_widgets.py`, `python3 tools/gen_cursors.py`
- Install: `./install.sh`, then `./apply-light.sh` or `./apply-dark.sh`
- Check install: `./verify.sh`
- Check an icon lookup: `kiconfinder6 <name>` ignores size; for a real size use KIconLoader::iconPath(name, -size) in a tiny C++ tool
- See icon/Plasma style changes: `rm -f ~/.cache/icon-cache.kcache ~/.cache/plasma_theme_clay*.kcache; systemctl --user restart plasma-plasmashell`
- Measure SVG element bounds as KSvg sees them: build a tiny QSvgRenderer::boundsOnElement tool (no Python Qt bindings installed)

## Pitfalls
- Plasma 6 tray icons come only from the icon theme (`KDE::icon`); `icons/*.svgz` in a Plasma style are ignored.
- Monochrome icons use the `ColorScheme-Text` stylesheet class so Plasma recolors them; Clay `#D97757` is a literal accent for warnings/news only.
- index.theme Context must be a known one (Status, Actions, Applications…); an unknown Context such as `Applets` makes KIconLoader skip the dir.
- Applets request both `name` and `name-symbolic`; the generator writes both (symlinks). Menu categories (`applications-*`) get only `-symbolic`, so colorful ones elsewhere stay Breeze.
- Task manager prefixes: `south-`/plain, `north-`, `west-`, `east-`; hover looks up `<state>-hover` (`launcher-hover`, `focus-hover`…) before `hover`.
- install.sh replaces listed paths wholesale: list single files for shared dirs (syntax themes), never the dir.

## Status
- Done: v0.9 palette and icon set, Plasma Login Manager, kitty/fastfetch, tray and action icons, KDE app tiles, Plasma tasks/button/lineedit, cursors, Kate themes.
- Gaps (fall back to Breeze): tray gaps (fall back to Breeze): peripheral batteries (mouse, headset…), RTL variants; mobile generation (LTE…) and power-profile badges are aliased to the plain glyph.
