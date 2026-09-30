# Clay KDE Theme

Clay — тёплая минималистичная тема для KDE Plasma 6 с отдельными Light/Dark вариантами.

Текущая версия: **0.9**

## Состав

- Global Theme: `Clay`, `Clay Dark`
- Color Schemes: `ClayLight`, `ClayDark`
- Plasma Style: `clay`, `clay-dark`
- Icon overlay: `clay-icons` с fallback на Breeze
- Wallpapers: `Clay Field`, `Clay Field Dark`
- Splash: Light/Dark
- Login Screen: Plasma Login Manager (см. ниже)
- Lock Screen: штатный Plasma locker + Clay colors/icons/wallpaper (в Light тёмный текст на светлых обоях)
- Logout/Shutdown screen: Clay Light/Dark
- KWin Alt+Tab: `Clay Grid`
- Klassy preset/configuration
- Clay launcher mark
- Clay Dolphin icon
- Clay folders and system icon overrides (включая XDG-папки: Desktop, Pictures, Public и т.д.)
- Typography: Inter, если установлен `inter-font`

## Визуальная система

Палитра построена на публичных цветах Anthropic: тёплый бумажный Ivory, Slate-чернила, тёплые нейтральные серые и Clay как скупой акцент.

Light:

- View / Window: Ivory `#FAF9F5` / `#F0EEE6`
- Text: Slate `#141413`, muted `#5E5D59`
- Accent (focus, controls, links): Clay `#D97757` / deep `#C6613F`
- Selection: warm neutral `#E3DACC`

Dark:

- View / Window: `#1F1E1D` / `#262624`
- Text: `#F0EEE6`, muted `#B0AEA5`
- Accent: Clay `#D97757`
- Selection: `#4A3F3A`

Иконки: папки из Manilla `#EBDBBC` на Kraft `#D4A27F` с Clay-глифами; файлы — Ivory-листы с цветным глифом по категории (Sky, Olive, Fig, Kraft, Clay); предметы в тёплом сером; системные приложения — бумажные карточки.

Акцент используется точечно: focus, active controls, glyphs, launcher, OSD. Большие поверхности и selection намеренно нейтральные.

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

Рекомендуется шрифт Inter:

```bash
sudo pacman -S inter-font
```

Если Inter установлен, `apply-*.sh` выставляет его как системный шрифт (моноширинный не трогается). Без него тема работает на текущих шрифтах.

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

## Экран входа (Plasma Login Manager)

Plasma Login Manager не использует QML-темы, как SDDM: экран входа устроен как экран блокировки и берёт цвета, шрифт и обои из настроек, а стиль Plasma и иконки — только из глобально установленных тем. Clay для него ставится отдельно:

```bash
sudo ./install-login.sh
```

Скрипт кладёт стиль Plasma и иконки Clay в `/usr/local/share` (не пересекается с pacman). Затем в «Параметры системы → Экран входа»:

1. «Настроить внешний вид…» → обои Clay Field (или Clay Field Dark) → «Применить».
2. «Применить настройки Plasma…» → «Применить» — переносит цвета, шрифт Inter, курсор и раскладки.

Оба шага просят пароль администратора. После переключения Light/Dark шаг 2 нужно повторить. Удаление: `sudo ./install-login.sh --remove`.

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

### Overview

Overview остаётся штатным KWin. Он наследует Clay colors/highlight, но ширина рамки выбранного окна в Plasma 6.7 жёстко задана внутри приватного KWin `WindowHeapDelegate.qml` как 6 px. Clay не патчит системные файлы, потому что обновление KWin такой патч перезапишет.

### Panel layout

Global Theme не пересоздаёт панель и не удаляет пользовательские виджеты. На исходной системе Clay используется с floating bottom panel 42 px, но пакет не навязывает этот layout другим пользователям.

## Архитектура

`clay-dark` наследует большую часть SVG от `clay`, поэтому Light/Dark не являются двумя независимыми форками Breeze.

`clay-icons` — overlay-theme с `Inherits=breeze`; собственные файлы есть только для наиболее заметных системных иконок. Полноцветные иконки (папки, файлы, корзина, накопители, карточки приложений) генерируются `tools/gen_icons.py` — правьте генератор, а не SVG. Для файлов генератор берёт список имён из установленного Breeze и раскладывает их по категориям симлинками. Символьные иконки действий (`actions/`) нарисованы вручную.

`Clay Grid` основан на штатном KWin Thumbnail Grid и не меняет логику Alt+Tab, только размер и визуальное выделение.

## Лицензирование

Проект содержит компоненты с разными исходными лицензиями:

- Clay-authored assets используют лицензии, указанные в соответствующих metadata.
- `Clay Grid` производен от KWin Thumbnail Grid; исходные SPDX/GPL-заголовки сохранены.
- Logout QML производен от Breeze Look-and-Feel; исходные SPDX-заголовки сохранены.

См. `LICENSES.md`.
