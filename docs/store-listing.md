# KDE Store listing

Publish at store.kde.org (Pling), logged in as the author. Archives are built by
`./build-release.sh` into `dist/store/`; screenshots go next to them in
`dist/previews/` (not in git: they are taken from a live session, see "Screenshots").

## Order

The Global Themes declare `X-KPackage-Dependencies` (`kns://<knsrc>/api.kde-look.org/<id>`,
ids in `store/ids.json`, written by `tools/store_deps.py`), so installing Clay or Clay Dark
pulls in the Plasma style, icons, cursors, wallpaper and Alt+Tab switcher; Clay also pulls in
Clay Dark (one way: KPackage rejects cyclic dependencies). Upload Clay Dark before Clay. Verified on Plasma
6.7.5: all five install in ~10 s.

- One failed dependency aborts the whole Global Theme install, and KPackage waits at most
  30 s per dependency (`QProcess::waitForFinished`). Slow access to the store's file CDN
  (`*.digitaloceanspaces.com`, throttled in some networks) breaks it.
- The store API serves a new item or a new file only after a delay (hours). Upload or change
  the components first, wait until `https://api.kde-look.org/ocs/v1/content/data/<id>` shows
  `<downloadname1>` with the new file, and only then upload Global Themes that point at them.
- Every dependency item must hold exactly one file: `knshandler` installs one link, and
  `wallpaper.knsrc` (`Uncompress=subdir-archive`) unpacks an archive with several packages
  into an extra subdir, where `Image=Clay` is not found. Hence two wallpaper items.

## Items

| Archive | Store category (as shown in the form; ids from `api.kde-look.org/ocs/v1/content/categories`) | License | Dependencies of the item |
|---|---|---|---|
| `org.artt.clay.desktop-<v>.tar.gz` | Global Themes (Plasma 6), id 722 | LGPL-2.1-or-later | Clay Plasma style, icons, cursors, Clay Field, Clay Grid, Clay Dark (Global Theme) |
| `org.artt.claydark.desktop-<v>.tar.gz` | Global Themes (Plasma 6), id 722 | LGPL-2.1-or-later | Clay Dark Plasma style, icons, cursors, Clay Field Dark, Clay Grid |
| `clay-plasma-style-<v>.tar.gz`, `clay-dark-plasma-style-<v>.tar.gz` | Plasma Themes, id 104 | LGPL-2.1-or-later | none |
| `clay-color-schemes-<v>.tar.gz` | Plasma Color Schemes, id 112 | LGPL-2.1-or-later | none |
| `clay-icons-<v>.tar.gz` | Full Icon Themes, id 132 | LGPL-2.1-or-later | Breeze icons (inherited) |
| `clay-cursors-<v>.tar.gz` | Cursors, id 107 | LGPL-2.1-or-later | none |
| `clay-field-<v>.tar.gz`, `clay-field-dark-<v>.tar.gz` (separate items) | Wallpapers KDE Plasma, id 299 | CC0-1.0 | none |
| `clay-grid-<v>.tar.gz` | Kwin Switching Layouts, id 721 (not 211, the Plasma 5 one) | GPL-2.0-or-later | none |

Not in the store (no category): Kate/KWrite syntax themes, kitty, fastfetch, the
Plasma Login Manager theme. They stay on GitHub and are installed by `install.sh`.

## Description (English, for every item; trim per item)

**Clay: a warm paper-toned Plasma 6 theme, light and dark.**

Ivory and slate surfaces, one restrained terracotta accent used only for focus and active
controls. One consistent visual language from the panel to the file manager:

- Color schemes ClayLight / ClayDark, Plasma styles with a pill task manager, rounded buttons
  and fields, wallpapers, splash, lock and logout screens
- Icon theme on top of Breeze: paper folders, file-type sheets, ~90 line action icons, a full
  system-tray set (network, battery, volume, media, Bluetooth, brightness…), System Settings
  modules, Dolphin emblems, KDE app tiles
- Cursors in the same palette (Wayland SVG and X11 bitmaps)
- Alt+Tab grid switcher
- Kate/KWrite syntax themes and kitty themes (GitHub)

**Requires:** KDE Plasma 6.7+ (tested on 6.7.5, Wayland). Uses the stock Breeze widget style and
window decoration, nothing else to install. The Inter font is optional.

**Apply:** System Settings → Appearance → Global Theme → Clay or Clay Dark. The Plasma style, icons,
cursors, wallpaper and Alt+Tab switcher are installed with it. For the full setup
(Inter, the Kate theme, kitty) use the scripts at
https://github.com/arttvad9r/clay-kde-theme

Independent community theme, not affiliated with KDE. Built from Breeze components (LGPL).

## Screenshots

Take them in a clean session (no personal windows, file names, device names in view).
`dist/previews/` has Light/Dark System Settings and Kate captures; add the desktop with
the panel and the launcher menu. Needs 1–3 images per item; the icon and cursor items can use
sheets rendered from `payload/icons`.

## Test install on a clean user

Install into a throwaway profile with its own session bus, so the dependencies are fetched from
the store and nothing touches your own `~/.local/share`:

```bash
t=$(mktemp -d); mkdir -m700 $t/rt
env -i PATH=/usr/bin HOME=$t XDG_DATA_HOME=$t/data XDG_CONFIG_HOME=$t/config XDG_CACHE_HOME=$t/cache \
  XDG_RUNTIME_DIR=$t/rt QT_QPA_PLATFORM=offscreen dbus-run-session -- \
  kpackagetool6 -t Plasma/LookAndFeel -i dist/store/org.artt.clay.desktop-<v>.tar.gz
ls $t/data/plasma/desktoptheme $t/data/icons $t/data/wallpapers $t/data/kwin/tabbox $t/.icons
```
