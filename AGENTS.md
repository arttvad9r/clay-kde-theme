# Clay KDE Theme

Warm minimal KDE Plasma 6 Light/Dark theme. User-facing docs are in `README.md`.

## Layout and generation
- `payload/` contains installed files. `install.sh` replaces listed components wholesale with backup; never list a shared directory when only one file should be replaced.
- Generated assets must be changed through their generators: `tools/gen_icons.py`, `gen_plasma_widgets.py`, `gen_aurorae.py`, `gen_cursors.py`; do not hand-edit their generated SVGs.
- Kate themes live in `payload/org.kde.syntax-highlighting/themes`; release archives come from `build-release.sh`; store metadata is in `docs/store-listing.md` and `store/ids.json`.

## Commands
- Regenerate with the relevant `python3 tools/gen_*.py`; install via `./install.sh`; apply via `./apply-light.sh` / `./apply-dark.sh`; verify with `./verify.sh`.
- For visual cache refresh: `rm -f ~/.cache/icon-cache.kcache ~/.cache/plasma_theme_clay*.kcache; systemctl --user restart plasma-plasmashell`.
- Check actual icon resolution at the requested size; `kiconfinder6` alone is insufficient for size-specific fallbacks.

## Important pitfalls
- KIconLoader may silently drop name suffixes and fall back to unrelated icons; verify applet icons at real size. Plasma tray icons come from the icon theme, not `icons/*.svgz` in Plasma style.
- Monochrome icons use `ColorScheme-Text`; only intentional warning/news accents use literal Clay accent. `index.theme` Context must be a valid KDE context.
- Splash stage 5 occurs before the desktop is drawn: never fade the whole root there; only fade content. Test with `ksplashqml --test --nofork <lnf dir>` and screenshots.
- Store installs execute no scripts; behavior that depends on `apply.sh` is not part of store-only installation.
- Screenshots of a live desktop must never be committed; store screenshots use a nested throwaway `kwin_wayland --virtual` session.
- GTK symbolic window buttons must be filled shapes. Firefox titlebar styling is handled by `extras/firefox/userChrome.css`; Electron apps draw their own.
- Do not reload kded `gtkconfig` or rerun apply scripts while Claude/Codex or other Electron apps are open; settings reload has crashed Codex.

## Git
- `main` holds released code only; every merge into `main` is a release tagged `vX.Y.Z`.
- `dev` is the integration branch and must always build and pass checks.
- Work in `feat/<name>` / `fix/<name>` from `dev`; several branches may run in parallel. Merge verified work into `dev`, then delete the branch.
- Push, tags and releases only with the owner's explicit permission.

## Status
Released v1.0 base theme exists; current unreleased work and store gaps are tracked by git and `docs/store-listing.md`, not duplicated here.
