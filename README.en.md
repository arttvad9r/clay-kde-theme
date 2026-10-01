# Clay KDE Theme

A warm, paper-toned theme for KDE Plasma 6 with Light and Dark variants. Ivory and slate
surfaces, one restrained terracotta accent. The Russian [README.md](README.md) is the full
documentation; this is the short version.

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

`./uninstall.sh` switches back to Breeze and removes the files. Pieces are also published
separately on the KDE Store (see `docs/store-listing.md`).

## Licensing

LGPL-2.1-or-later for Clay's own work; some parts derive from Breeze and KWin, wallpapers are
CC0-1.0. Details in [LICENSES.md](LICENSES.md). Not affiliated with KDE.
