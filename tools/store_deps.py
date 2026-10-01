#!/usr/bin/env python3
"""Add X-KPackage-Dependencies to a Global Theme's metadata.json.

Usage: store_deps.py <ids.json> <lnf id> <metadata.json>
ids.json maps store items to KDE Store content ids; items without an id
(0 or missing) are skipped, so the build works before anything is uploaded.
"""
import json
import sys
from pathlib import Path

# lnf id -> [(ids.json key, knsrc file)]
DEPS = {
    "org.artt.clay.desktop": [("plasma-style", "plasma-themes.knsrc"), ("icons", "icons.knsrc"),
                              ("cursors", "xcursor.knsrc"), ("wallpapers", "wallpaper.knsrc"),
                              ("window-switcher", "kwinswitcher.knsrc")],
    "org.artt.claydark.desktop": [("plasma-style-dark", "plasma-themes.knsrc"), ("icons", "icons.knsrc"),
                                  ("cursors", "xcursor.knsrc"), ("wallpapers", "wallpaper.knsrc"),
                                  ("window-switcher", "kwinswitcher.knsrc")],
}

ids_path, lnf, meta_path = sys.argv[1:4]
ids = json.loads(Path(ids_path).read_text()) if Path(ids_path).exists() else {}
deps = [f"kns://{knsrc}/api.kde-look.org/{ids[key]}" for key, knsrc in DEPS[lnf] if ids.get(key)]
meta = json.loads(Path(meta_path).read_text())
if deps:
    meta["X-KPackage-Dependencies"] = deps
else:
    meta.pop("X-KPackage-Dependencies", None)
Path(meta_path).write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
