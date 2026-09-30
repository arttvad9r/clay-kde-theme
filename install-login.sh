#!/usr/bin/env bash
# Install the Clay Plasma style and icons system-wide so the Plasma Login
# Manager greeter (runs as the 'plasmalogin' user) can use them.
# Colors, fonts and wallpaper are then applied from
# System Settings -> Login Screen; see README.
#
#   sudo ./install-login.sh           install / update
#   sudo ./install-login.sh --remove  remove
set -euo pipefail

here="$(cd -- "$(dirname -- "$0")" && pwd)"
payload="$here/payload"
prefix="/usr/local/share"

targets=(
  "plasma/desktoptheme/clay"
  "plasma/desktoptheme/clay-dark"
  "icons/clay-icons"
)

if [ "$(id -u)" -ne 0 ]; then
  echo "Run with sudo: sudo $0 ${1:-}" >&2
  exit 2
fi

case "${1:-}" in
  "")
    for rel in "${targets[@]}"; do
      rm -rf "${prefix:?}/$rel"
      mkdir -p "$prefix/$(dirname "$rel")"
      cp -R "$payload/$rel" "$prefix/$rel"
      chown -R root:root "$prefix/$rel"
      chmod -R u=rwX,go=rX "$prefix/$rel"
    done
    echo "Clay Plasma style and icons installed into $prefix."
    echo "Now open System Settings -> Login Screen:"
    echo "  1. Configure Appearance... -> pick the Clay wallpaper -> Apply"
    echo "  2. Apply Plasma Settings... -> Apply"
    ;;
  --remove)
    for rel in "${targets[@]}"; do
      rm -rf "${prefix:?}/$rel"
    done
    echo "Clay login screen files removed from $prefix."
    ;;
  *)
    echo "Usage: sudo $0 [--remove]" >&2
    exit 2
    ;;
esac
