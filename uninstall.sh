#!/usr/bin/env bash
set -euo pipefail

data_home="${XDG_DATA_HOME:-$HOME/.local/share}"

current="$(kreadconfig6 --file kdeglobals --group KDE --key LookAndFeelPackage 2>/dev/null || true)"
if [[ "$current" == "org.artt.clay.desktop" || "$current" == "org.artt.claydark.desktop" ]]; then
  echo "Clay is active; switching to Breeze before removing files."
  if command -v plasma-apply-lookandfeel >/dev/null 2>&1; then
    plasma-apply-lookandfeel -a org.kde.breeze.desktop || true
  fi
  if command -v plasma-apply-colorscheme >/dev/null 2>&1; then
    plasma-apply-colorscheme BreezeLight || true
  fi
  kwriteconfig6 --file kdeglobals --group Icons --key Theme breeze --notify || true
  kwriteconfig6 --file kwinrc --group TabBox --key LayoutName thumbnail_grid || true
  kwriteconfig6 --file ksplashrc --group KSplash --key Theme org.kde.breeze.desktop || true
  # Drop Inter only if it was set by Clay's apply script.
  for spec in General:font General:menuFont General:toolBarFont General:smallestReadableFont WM:activeFont; do
    group="${spec%%:*}" key="${spec#*:}"
    value="$(kreadconfig6 --file kdeglobals --group "$group" --key "$key" 2>/dev/null || true)"
    case "$value" in
      "Inter,"*|"Inter Variable,"*) kwriteconfig6 --file kdeglobals --group "$group" --key "$key" --delete "" || true ;;
    esac
  done
fi

rm -f   "$data_home/color-schemes/ClayLight.colors"   "$data_home/color-schemes/ClayDark.colors"

rm -rf   "$data_home/plasma/desktoptheme/clay"   "$data_home/plasma/desktoptheme/clay-dark"   "$data_home/plasma/look-and-feel/org.artt.clay.desktop"   "$data_home/plasma/look-and-feel/org.artt.claydark.desktop"   "$data_home/wallpapers/Clay"   "$data_home/wallpapers/ClayDark"   "$data_home/icons/clay-icons"   "$data_home/kwin/tabbox/clay_grid"

if command -v kbuildsycoca6 >/dev/null 2>&1; then
  kbuildsycoca6 --noincremental >/dev/null 2>&1 || true
fi
if command -v qdbus6 >/dev/null 2>&1; then
  qdbus6 org.kde.KWin /KWin reconfigure >/dev/null 2>&1 || true
fi
if systemctl --user is-active plasma-plasmashell.service >/dev/null 2>&1; then
  systemctl --user restart plasma-plasmashell.service
fi

echo "Clay files removed from $data_home."
