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

echo "Built:"
echo "  $archive"
echo "  $archive.sha256"
