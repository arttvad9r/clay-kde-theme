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
  "icons/clay-cursors"
  "org.kde.syntax-highlighting/themes/clay-light.theme"
  "org.kde.syntax-highlighting/themes/clay-dark.theme"
  "kwin/tabbox/clay_grid"
  "aurorae/themes/Clay"
  "aurorae/themes/ClayDark"
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

# Replace each component as a whole (it was backed up above), so files
# dropped from the payload don't linger in an upgraded install.
for rel in "${targets[@]}"; do
  rm -rf "${data_home:?}/$rel"
  mkdir -p "$data_home/$(dirname "$rel")"
  cp -a "$payload/$rel" "$data_home/$rel"
done

# kitty follows the Plasma light/dark preference through these auto themes.
if command -v kitty >/dev/null 2>&1; then
  kitty_dir="${XDG_CONFIG_HOME:-$HOME/.config}/kitty"
  mkdir -p "$kitty_dir"
  for pair in light:clay-light dark:clay-dark no-preference:clay-light; do
    dst="$kitty_dir/${pair%%:*}-theme.auto.conf"
    if [ -e "$dst" ] && ! grep -q 'clay-kde-theme' "$dst"; then
      mkdir -p "$backup/kitty"
      cp -a "$dst" "$backup/kitty/"
      backed_up=true
    fi
    cp "$here/extras/kitty/${pair#*:}.conf" "$dst"
  done
fi

# Firefox draws its own window controls (Breeze theme: solid circle, pink close); restyle them in the default profile.
ff_root=""
for d in "${XDG_CONFIG_HOME:-$HOME/.config}/mozilla/firefox" "$HOME/.mozilla/firefox"; do
  [ -f "$d/profiles.ini" ] && { ff_root="$d"; break; }
done
if [ -n "$ff_root" ]; then
  ff_path="$(awk -F= '/^\[Install/{i=1} i&&/^Default=/{print $2; exit}' "$ff_root/profiles.ini")"
  [ -n "$ff_path" ] || ff_path="$(awk -F= '/^\[Profile/{p=""} /^Path=/{p=$2} /^Default=1/{print p; exit}' "$ff_root/profiles.ini")"
  ff_profile="$ff_root/$ff_path"
  if [ -n "$ff_path" ] && [ -d "$ff_profile" ]; then
    mkdir -p "$ff_profile/chrome"
    dst="$ff_profile/chrome/userChrome.css"
    if [ -e "$dst" ] && ! grep -q 'Clay:' "$dst"; then
      mkdir -p "$backup/firefox"
      cp -a "$dst" "$backup/firefox/"
      backed_up=true
    fi
    cp "$here/extras/firefox/userChrome.css" "$dst"
    pref='user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true); // clay-kde-theme'
    grep -qF 'clay-kde-theme' "$ff_profile/user.js" 2>/dev/null || printf '%s\n' "$pref" >> "$ff_profile/user.js"
    echo "Firefox: window controls styled in $ff_profile (restart Firefox)."
  fi
fi

if command -v kbuildsycoca6 >/dev/null 2>&1; then
  kbuildsycoca6 --noincremental >/dev/null 2>&1 || true
fi

echo "Clay $(tr -d "[:space:]" < "$here/VERSION") installed into: $data_home"
if "$backed_up"; then
  echo "Existing Clay files were backed up to: $backup"
else
  rmdir "$backup" 2>/dev/null || true
fi
echo "Apply with:"
echo "  $here/apply-light.sh"
echo "  $here/apply-dark.sh"
