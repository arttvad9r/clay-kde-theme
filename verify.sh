#!/usr/bin/env bash
set -euo pipefail

data_home="${XDG_DATA_HOME:-$HOME/.local/share}"
errors=0

check_file() {
  if [ -e "$1" ]; then
    printf "OK   %s\n" "$1"
  else
    printf "MISS %s\n" "$1"
    errors=$((errors + 1))
  fi
}

check_file "$data_home/color-schemes/ClayLight.colors"
check_file "$data_home/color-schemes/ClayDark.colors"
check_file "$data_home/plasma/desktoptheme/clay/metadata.json"
check_file "$data_home/plasma/desktoptheme/clay-dark/metadata.json"
check_file "$data_home/plasma/look-and-feel/org.artt.clay.desktop/metadata.json"
check_file "$data_home/plasma/look-and-feel/org.artt.claydark.desktop/metadata.json"
check_file "$data_home/icons/clay-icons/index.theme"
check_file "$data_home/icons/clay-cursors/index.theme"
check_file "$data_home/org.kde.syntax-highlighting/themes/clay-light.theme"
check_file "$data_home/kwin/tabbox/clay_grid/metadata.json"
check_file "$data_home/wallpapers/Clay/metadata.json"
check_file "$data_home/wallpapers/ClayDark/metadata.json"

for f in "$data_home/plasma/desktoptheme/clay"/widgets/*.svgz          "$data_home/plasma/desktoptheme/clay"/dialogs/*.svgz          "$data_home/plasma/desktoptheme/clay-dark"/widgets/*.svgz; do
  [ -e "$f" ] || continue
  if gzip -t "$f" 2>/dev/null; then
    printf "SVGZ %s\n" "$f"
  else
    printf "BAD  %s\n" "$f"
    errors=$((errors + 1))
  fi
done

echo
echo "Active state:"
printf "  Global:  "; kreadconfig6 --file kdeglobals --group KDE --key LookAndFeelPackage || true
printf "  Icons:   "; kreadconfig6 --file kdeglobals --group Icons --key Theme || true
printf "  TabBox:  "; kreadconfig6 --file kwinrc --group TabBox --key LayoutName || true
printf "  Splash:  "; kreadconfig6 --file ksplashrc --group KSplash --key Theme || true

if (( errors > 0 )); then
  echo "$errors verification error(s)." >&2
  exit 1
fi
echo "Clay verification passed."
