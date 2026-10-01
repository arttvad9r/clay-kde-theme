# KDE Store listing

Publish at store.kde.org (Pling), logged in as the author. Archives are built by
`./build-release.sh` into `dist/store/`; screenshots go next to them in
`dist/previews/` (not in git: they are taken from a live session, see "Screenshots").

## Order

1. Upload the leaf items, note each content id (the number in the item URL).
2. Put the ids into `store/ids.json` (`plasma-style`, `plasma-style-dark`, `icons`, `cursors`,
   `wallpapers`, `window-switcher`) and rebuild: both Global Themes then get
   `X-KPackage-Dependencies` (`kns://<knsrc>/api.kde-look.org/<id>`), so installing the Global
   Theme pulls the rest.
3. Upload the two Global Themes last. Test an install on a clean user (below).

## Items

| Archive | Store category | License | Dependencies of the item |
|---|---|---|---|
| `org.artt.clay.desktop-<v>.tar.gz` | Global Themes (Plasma 6) | LGPL-2.1-or-later | Klassy (not installable from the store) |
| `org.artt.claydark.desktop-<v>.tar.gz` | Global Themes (Plasma 6) | LGPL-2.1-or-later | Klassy |
| `clay-plasma-style-<v>.tar.gz`, `clay-dark-plasma-style-<v>.tar.gz` | Plasma Theme | LGPL-2.1-or-later | none |
| `clay-color-schemes-<v>.tar.gz` | KDE Color Scheme | LGPL-2.1-or-later | none |
| `clay-icons-<v>.tar.gz` | KDE Icon Theme | LGPL-2.1-or-later | Breeze icons (inherited) |
| `clay-cursors-<v>.tar.gz` | X11 Mouse Theme | LGPL-2.1-or-later | none |
| `clay-wallpapers-<v>.tar.gz` | KDE Wallpaper (other) | CC0-1.0 | none |
| `clay-grid-<v>.tar.gz` | Kwin Switching Layouts Plasma 6 | GPL-2.0-or-later | none |

Not in the store (no category): Klassy preset, Kate/KWrite syntax themes, kitty, fastfetch, the
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

**Requires:** KDE Plasma 6.7+ (tested on 6.7.5, Wayland) and the Klassy window decoration and
style. Without Klassy windows fall back to the default decoration. The Inter font is optional.

**Apply:** System Settings → Appearance → Global Theme → Clay or Clay Dark. For the full setup
(Klassy preset, Inter, Kate and kitty themes) use the scripts at
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

Then apply it in a throwaway Plasma session or a fresh VM user and check the dependency downloads.
Plasma 6.5+ has reports of `kns://` dependencies failing to install; verify on your uploaded items
before announcing.
