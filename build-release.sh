#!/usr/bin/env bash
set -euo pipefail

here="$(cd -- "$(dirname -- "$0")" && pwd)"
version="$(tr -d '[:space:]' < "$here/VERSION")"
name="clay-kde-theme-$version"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

mkdir -p "$tmp/$name" "$here/dist"

(
  cd "$here"
  tar     --exclude="./dist"     --exclude="./.git"     -cf - .
) | (
  cd "$tmp/$name"
  tar -xf -
)

archive="$here/dist/$name.tar.gz"
tar -czf "$archive" -C "$tmp" "$name"

(
  cd "$here/dist"
  sha256sum "$name.tar.gz" > "$name.tar.gz.sha256"
)

# KDE Store: one archive per store item, in the layout its knsrc expects
# (see /usr/share/knsrcfiles). Store item ids, once known, go to store/ids.json
# and become X-KPackage-Dependencies of the Global Themes.
store="$here/dist/store"
rm -rf "$store"
mkdir -p "$store"
stage="$tmp/store"
mkdir -p "$stage"
p="$here/payload"
pack() { # pack <archive> <dir> <entries...>
  local out="$1" dir="$2"; shift 2
  tar --owner=0 --group=0 -czf "$store/$out" -C "$dir" "$@"
}

for lnf in org.artt.clay.desktop org.artt.claydark.desktop; do
  cp -a "$p/plasma/look-and-feel/$lnf" "$stage/$lnf"
  scheme=ClayLight; [ "$lnf" = org.artt.claydark.desktop ] && scheme=ClayDark
  # Bundled scheme: colors apply even without the separate color scheme item.
  cp "$p/color-schemes/$scheme.colors" "$stage/$lnf/contents/colors"
  python3 "$here/tools/store_deps.py" "$here/store/ids.json" "$lnf" "$stage/$lnf/metadata.json"
  pack "$lnf-$version.tar.gz" "$stage" "$lnf"
done

# clay-dark falls back to clay; make it standalone for the store.
cp -a "$p/plasma/desktoptheme/clay" "$p/plasma/desktoptheme/clay-dark" "$stage/"
cp -an "$stage/clay/." "$stage/clay-dark/"
cp "$p/plasma/desktoptheme/clay-dark/metadata.json" "$p/plasma/desktoptheme/clay-dark/colors" "$stage/clay-dark/"
sed -i 's/^FallbackTheme=clay$/FallbackTheme=default/' "$stage/clay-dark/plasmarc"
pack "clay-plasma-style-$version.tar.gz" "$stage" clay
pack "clay-dark-plasma-style-$version.tar.gz" "$stage" clay-dark

pack "clay-color-schemes-$version.tar.gz" "$p/color-schemes" ClayLight.colors ClayDark.colors
pack "clay-icons-$version.tar.gz" "$p/icons" clay-icons
pack "clay-cursors-$version.tar.gz" "$p/icons" clay-cursors
# One wallpaper package per archive: wallpaper.knsrc unpacks a multi-package
# archive into an extra subdir, and the Global Theme no longer finds Image=Clay.
pack "clay-field-$version.tar.gz" "$p/wallpapers" Clay
pack "clay-field-dark-$version.tar.gz" "$p/wallpapers" ClayDark
pack "clay-grid-$version.tar.gz" "$p/kwin/tabbox" clay_grid

(
  cd "$store"
  sha256sum ./*.tar.gz > SHA256SUMS
)

echo "Built:"
echo "  $archive"
echo "  $archive.sha256"
echo "  $store/ (KDE Store items)"
