#!/usr/bin/env bash
set -euo pipefail

here="$(cd -- "$(dirname -- "$0")" && pwd)"
payload="$here/payload"
data_home="${XDG_DATA_HOME:-$HOME/.local/share}"

test -d "$payload" || {
  echo "Payload not found: $payload" >&2
  exit 2
}

targets=(
  "color-schemes/ClayLight.colors"
  "color-schemes/ClayDark.colors"
  "plasma/desktoptheme/clay"
  "plasma/desktoptheme/clay-dark"
  "plasma/look-and-feel/org.artt.clay.desktop"
  "plasma/look-and-feel/org.artt.claydark.desktop"
  "wallpapers/Clay"
  "wallpapers/ClayDark"
  "icons/clay-icons"
  "kwin/tabbox/clay_grid"
)

stamp="$(date +%Y%m%d-%H%M%S)"
backup="$data_home/clay-install-backup-$stamp"
backed_up=false

for rel in "${targets[@]}"; do
  src="$data_home/$rel"
  if [ -e "$src" ]; then
    mkdir -p "$backup/$(dirname "$rel")"
    cp -a "$src" "$backup/$rel"
    backed_up=true
  fi
done

mkdir -p "$data_home"
cp -a "$payload/." "$data_home/"

for f in   "$data_home/plasma/look-and-feel/org.artt.clay.desktop/extras/apply-klassy.sh"   "$data_home/plasma/look-and-feel/org.artt.claydark.desktop/extras/apply-klassy.sh"; do
  [ -f "$f" ] && chmod +x "$f"
done

if command -v kbuildsycoca6 >/dev/null 2>&1; then
  kbuildsycoca6 --noincremental >/dev/null 2>&1 || true
fi

echo "Clay 0.8 installed into: $data_home"
if "$backed_up"; then
  echo "Existing Clay files were backed up to: $backup"
else
  rmdir "$backup" 2>/dev/null || true
fi
echo "Apply with:"
echo "  $here/apply-light.sh"
echo "  $here/apply-dark.sh"
