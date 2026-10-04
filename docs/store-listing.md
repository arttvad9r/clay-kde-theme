# KDE Store listing

Publish at store.kde.org (Pling), logged in as the author. Archives are built by
`./build-release.sh` into `dist/store/`; screenshots go next to them in
`dist/previews/` (not in git: they are taken from a live session, see "Screenshots").

## Order

Upload all items in any order. The Global Themes ship without `X-KPackage-Dependencies`
(`store/ids.json` stays all zeros): `kns://` dependencies fail on several Plasma 6 releases
("Could not install dependency"), and one failed dependency aborts the whole Global Theme
install. Without them the Global Theme always installs; components that are not installed
fall back to Breeze. List the component items with links in each Global Theme description.

To turn dependencies on later: put the content ids (the number in the item URL) into
`store/ids.json`, rebuild, re-upload the Global Themes, and test the install on a clean user.

## Items

| Archive | Store category | License | Dependencies of the item |
|---|---|---|---|
| `org.artt.clay.desktop-<v>.tar.gz` | Global Themes (Plasma 6) | LGPL-2.1-or-later | none (Breeze widget style and decoration ship with Plasma) |
| `org.artt.claydark.desktop-<v>.tar.gz` | Global Themes (Plasma 6) | LGPL-2.1-or-later | none |
| `clay-plasma-style-<v>.tar.gz`, `clay-dark-plasma-style-<v>.tar.gz` | Plasma Theme | LGPL-2.1-or-later | none |
| `clay-color-schemes-<v>.tar.gz` | KDE Color Scheme | LGPL-2.1-or-later | none |
| `clay-icons-<v>.tar.gz` | KDE Icon Theme | LGPL-2.1-or-later | Breeze icons (inherited) |
| `clay-cursors-<v>.tar.gz` | X11 Mouse Theme | LGPL-2.1-or-later | none |
| `clay-wallpapers-<v>.tar.gz` | KDE Wallpaper (other) | CC0-1.0 | none |
| `clay-grid-<v>.tar.gz` | Kwin Switching Layouts Plasma 6 | GPL-2.0-or-later | none |

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

**Apply:** System Settings → Appearance → Global Theme → Clay or Clay Dark. Install the Clay
Plasma style, icons, cursors, wallpapers and Alt+Tab switcher first (links below), or Breeze is
used in their place. For the full setup
(Inter, the Kate theme, kitty) use the scripts at
https://github.com/arttvad9r/clay-kde-theme

Independent community theme, not affiliated with KDE. Built from Breeze components (LGPL).

## Screenshots

Take them in a clean session (no personal windows, file names, device names in view).
`dist/previews/` has Light/Dark System Settings and Kate captures; add the desktop with
the panel and the launcher menu. Needs 1–3 images per item; the icon and cursor items can use
sheets rendered from `payload/icons`.

## Test install on a clean user

```bash
XDG_DATA_HOME=$(mktemp -d) kpackagetool6 -t Plasma/LookAndFeel -i dist/store/org.artt.clay.desktop-<v>.tar.gz
```

Then apply it in a throwaway Plasma session or a fresh VM user.
