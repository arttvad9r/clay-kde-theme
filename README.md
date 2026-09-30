# Clay KDE Theme

Clay — тёплая минималистичная тема для KDE Plasma 6 с отдельными Light/Dark вариантами.

Текущая версия: **0.8**

## Состав

- Global Theme: `Clay`, `Clay Dark`
- Color Schemes: `ClayLight`, `ClayDark`
- Plasma Style: `clay`, `clay-dark`
- Icon overlay: `clay-icons` с fallback на Breeze
- Wallpapers: `Clay Field`, `Clay Field Dark`
- Splash: Light/Dark
- Lock Screen: штатный Plasma locker + Clay colors/icons/wallpaper
- Logout/Shutdown screen: Clay Light/Dark
- KWin Alt+Tab: `Clay Grid`
- Klassy preset/configuration
- Clay launcher mark
- Clay Dolphin icon
- Clay folders and system icon overrides

## Визуальная система

Light:

- Canvas: `#F2EFE8`
- Text: `#2A2722`
- Identity / focus orange: `#E66F43`
- Quiet selection: `#E8D7CF`

Dark:

- View: `#1F1D1A`
- Window: `#25221F`
- Text: `#E8E1D8`
- Control accent: `#F28B5E`
- Identity folders/icons remain Clay orange.

Акцент используется точечно: focus, active controls, folders, launcher, Dolphin, OSD. Большие surfaces и selection намеренно спокойные.

## Требования

Проверено на:

- KDE Plasma 6.7.5
- KWin 6.7.5 / Wayland
- Klassy 6.7.3

Нужны команды:

- `plasma-apply-lookandfeel`
- `plasma-apply-colorscheme`
- `plasma-apply-wallpaperimage`
- `kwriteconfig6`
- `kbuildsycoca6`
- `klassy-settings`

Klassy является обязательной зависимостью для полного внешнего вида окон и Qt Widgets.

## Установка

```bash
./install.sh
```

Установка только копирует файлы в `${XDG_DATA_HOME:-~/.local/share}` и не переключает текущую тему.

Затем:

```bash
./apply-light.sh
# или
./apply-dark.sh
```

## Проверка

```bash
./verify.sh
```

## Удаление

```bash
./uninstall.sh
```

Если Clay активен во время удаления, скрипт сначала переключит Plasma на Breeze, чтобы не удалять используемые компоненты.

## Что намеренно не входит

### SDDM

Clay не меняет SDDM. Экран входа в систему остаётся системным.

### Overview

Overview остаётся штатным KWin. Он наследует Clay colors/highlight, но ширина рамки выбранного окна в Plasma 6.7 жёстко задана внутри приватного KWin `WindowHeapDelegate.qml` как 6 px. Clay не патчит системные файлы, потому что обновление KWin такой патч перезапишет.

### Panel layout

Global Theme не пересоздаёт панель и не удаляет пользовательские виджеты. На исходной системе Clay используется с floating bottom panel 42 px, но пакет не навязывает этот layout другим пользователям.

## Архитектура

`clay-dark` наследует большую часть SVG от `clay`, поэтому Light/Dark не являются двумя независимыми форками Breeze.

`clay-icons` — overlay-theme с `Inherits=breeze`; собственные файлы есть только для наиболее заметных системных иконок.

`Clay Grid` основан на штатном KWin Thumbnail Grid и не меняет логику Alt+Tab, только размер и визуальное выделение.

## Лицензирование

Проект содержит компоненты с разными исходными лицензиями:

- Clay-authored assets используют лицензии, указанные в соответствующих metadata.
- `Clay Grid` производен от KWin Thumbnail Grid; исходные SPDX/GPL-заголовки сохранены.
- Logout QML производен от Breeze Look-and-Feel; исходные SPDX-заголовки сохранены.

См. `LICENSES.md`.
