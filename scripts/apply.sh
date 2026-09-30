#!/usr/bin/env bash
set -euo pipefail

variant="${1:-light}"
data_home="${XDG_DATA_HOME:-$HOME/.local/share}"
config_home="${XDG_CONFIG_HOME:-$HOME/.config}"

case "$variant" in
  light)
    lnf="org.artt.clay.desktop"
    scheme="ClayLight"
    plasma_theme="clay"
    wallpaper="Clay"
    ;;
  dark)
    lnf="org.artt.claydark.desktop"
    scheme="ClayDark"
    plasma_theme="clay-dark"
    wallpaper="ClayDark"
    ;;
  *)
    echo "Usage: $0 light|dark" >&2
    exit 2
    ;;
esac

required=(
  plasma-apply-lookandfeel
  plasma-apply-colorscheme
  plasma-apply-wallpaperimage
  kwriteconfig6
  kbuildsycoca6
  klassy-settings
)
for cmd in "${required[@]}"; do
  command -v "$cmd" >/dev/null 2>&1 || {
    echo "Missing required command: $cmd" >&2
    exit 3
  }
done

test -d "$data_home/plasma/look-and-feel/$lnf" || {
  echo "Clay is not installed in $data_home. Run ./install.sh first." >&2
  exit 4
}

# A custom KDE AccentColor rewrites Colors:Selection. Clay intentionally
# separates a vivid focus accent from a quiet selection surface.
kwriteconfig6 --file kdeglobals --group General --key AccentColor --delete "" || true
kwriteconfig6 --file kdeglobals --group General --key LastUsedCustomAccentColor --delete "" || true
kwriteconfig6 --file kdeglobals --group General --key accentColorFromWallpaper false

plasma-apply-lookandfeel -a "$lnf"
plasma-apply-colorscheme "$scheme"

kwriteconfig6 --file kdeglobals --group KDE --key widgetStyle Klassy
kwriteconfig6 --file kdeglobals --group Icons --key Theme clay-icons --notify
kwriteconfig6 --file kwinrc --group org.kde.kdecoration2 --key library org.kde.klassy
kwriteconfig6 --file kwinrc --group org.kde.kdecoration2 --key theme Klassy
kwriteconfig6 --file kwinrc --group TabBox --key LayoutName clay_grid

kwriteconfig6 --file ksplashrc --group KSplash --key Engine KSplashQML
kwriteconfig6 --file ksplashrc --group KSplash --key Theme "$lnf"

"$data_home/plasma/look-and-feel/$lnf/extras/apply-klassy.sh"

plasma-apply-wallpaperimage   "$data_home/wallpapers/$wallpaper/contents/images/3840x2160.png"

kbuildsycoca6 --noincremental >/dev/null 2>&1 || true

if command -v qdbus6 >/dev/null 2>&1; then
  qdbus6 org.kde.KWin /KWin reconfigure >/dev/null 2>&1 || true
fi

if systemctl --user is-active plasma-plasmashell.service >/dev/null 2>&1; then
  systemctl --user restart plasma-plasmashell.service
fi

echo "Applied Clay $variant."
echo "Global Theme: $lnf"
echo "Color Scheme: $scheme"
echo "Plasma Style: $plasma_theme"
echo "Icons: clay-icons"
echo "Window switcher: clay_grid"
