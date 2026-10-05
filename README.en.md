# Clay KDE Theme

![Clay Light and Clay Dark](docs/screenshots/hero.png)

A warm, paper-toned theme for KDE Plasma 6, light and dark. Ivory and slate surfaces, one restrained terracotta accent used only for focus and active controls. One visual language from the panel to the file manager. The Russian [README.md](README.md) is the full documentation; this is the short version.

Version **1.0.1** · Plasma 6.7+

<table>
<tr>
<td><img src="docs/screenshots/light-dolphin.png" alt="Dolphin, light"></td>
<td><img src="docs/screenshots/dark-dolphin.png" alt="Dolphin, dark"></td>
</tr>
<tr>
<td><img src="docs/screenshots/light-settings.png" alt="System Settings"></td>
<td><img src="docs/screenshots/dark-alttab.png" alt="Clay Grid Alt+Tab"></td>
</tr>
<tr>
<td><img src="docs/screenshots/icons-light.png" alt="Icons"></td>
<td><img src="docs/screenshots/cursors.png" alt="Cursors"></td>
</tr>
</table>

## KDE Store

No scripts needed: System Settings → … → Get New…, search for "Clay". Install the components first, then the Global Theme (it does not pull them in: on several Plasma 6 releases dependency downloads break the whole install).

| Component | System Settings page | Store |
|---|---|---|
| Global Theme Clay / Clay Dark | Global Theme | [Clay](https://store.kde.org/p/2377208) · [Clay Dark](https://store.kde.org/p/2377211) |
| Plasma style | Plasma Style | [Clay](https://store.kde.org/p/2377181) · [Clay Dark](https://store.kde.org/p/2377182) |
| Color schemes | Colors | [Clay Color Schemes](https://store.kde.org/p/2377202) |
| Icons | Icons | [Clay Icons](https://store.kde.org/p/2377203) |
| Cursors | Cursors | [Clay Cursors](https://store.kde.org/p/2377205) |
| Wallpapers | Wallpaper | [Clay Field](https://store.kde.org/p/2377206) |
| Alt+Tab | Task Switcher | [Clay Grid](https://store.kde.org/p/2377207) |

Kate/KWrite themes, kitty, fastfetch, Inter and the login screen come only with `install.sh` (below).

## What's inside

Global Themes `Clay` / `Clay Dark`, color schemes, Plasma styles, an icon theme on top of Breeze
(folders, files, ~90 action icons, the system tray, System Settings, Dolphin emblems, KDE apps),
cursors, wallpapers, splash/lock/logout screens, an Alt+Tab grid, Kate/KWrite themes, and
kitty/fastfetch extras. Plasma Login Manager is supported (`install-login.sh`).

## Requirements

KDE Plasma 6.7+ (tested on 6.7.5, Wayland). Widget style and window decoration are the stock
Breeze, nothing else to install. Optional: the Inter font.

## Install

```bash
./install.sh
./apply-light.sh   # or ./apply-dark.sh
./verify.sh
```

`./uninstall.sh` switches back to Breeze and removes the files.

## Licensing

LGPL-2.1-or-later for Clay's own work; some parts derive from Breeze and KWin, wallpapers are
CC0-1.0. Details in [LICENSES.md](LICENSES.md). Not affiliated with KDE.
