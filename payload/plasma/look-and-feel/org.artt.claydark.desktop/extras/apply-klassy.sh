#!/bin/sh
set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
preset="$here/Clay.klpw"
cfg="$HOME/.config/klassy/klassyrc"
store="$HOME/.config/klassy/windecopresetsrc"

if ! grep -q '^\[Windeco Preset Clay\]$' "$store" 2>/dev/null; then
    klassy-settings --import-preset "$preset"
fi
klassy-settings --load-windeco-preset Clay

setv() {
    kwriteconfig6 --file "$cfg" --group "$1" --key "$2" "$3"
}

setv Style AnimationsDuration 140
setv Style AnimationsEnabled true
setv Style ButtonGradient false
setv Style FrameCornerRadius FCR_Custom
setv Style FrameCustomCornerRadius 7.0
setv Style MenuItemDrawStrongFocus false
setv Style MenuOpacity 100
setv Style ScrollBarAddLineButtons 0
setv Style ScrollBarAutoHideArrows true
setv Style ScrollBarSeparator false
setv Style ScrollBarSliderPadding 5
setv Style ScrollBarSliderThicknessMouseNotOverPercent 70
setv Style ScrollBarSliderThicknessMouseOver 7
setv Style ScrollBarSubLineButtons 0
setv Style SliderDrawTickMarks false
setv Style TabBarDrawCenteredTabs false
setv Style ToolBarDrawItemSeparator false
setv Style ViewDrawTreeBranchLines false
lookandfeel_id=$(basename "$(dirname "$here")")
setv Global LookAndFeelSet "$lookandfeel_id"

if command -v qdbus6 >/dev/null 2>&1 && qdbus6 org.kde.KWin >/dev/null 2>&1; then
    qdbus6 org.kde.KWin /KWin reconfigure >/dev/null 2>&1 || true
fi
