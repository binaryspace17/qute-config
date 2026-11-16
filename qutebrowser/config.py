# pylint: disable=C0111

c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103


# =============================================================================
# Noctalia Theming
# =============================================================================

config.load_autoconfig(True)
config.source('noctalia/colors.py')
config.new_instance_open_target = 'tab-silent'


# =============================================================================
# General Browser Behavior
# Session persistence and built-in PDF handling
# =============================================================================

c.auto_save.session = True  # Save tabs on quit/restart
c.content.pdfjs = False  # Use pdf.js for PDF rendering


# =============================================================================
# Tab Appearance, Layout, and Visibility
# =============================================================================

c.tabs.title.format = "{audio}{current_title}"

c.tabs.padding = {
    'top': 5,
    'bottom': 5,
    'left': 9,
    'right': 9,
}

c.tabs.indicator.width = 0  # 0 = no tab indicators
c.tabs.width = '10%'
c.tabs.position = 'top'
c.tabs.title.alignment = 'left'
c.tabs.show = 'multiple'


# =============================================================================
# Scrolling & Completion
# =============================================================================

c.scrolling.smooth = True
c.completion.shrink = True  # Shrink completion menu to fit content


# =============================================================================
# Fonts
# Default UI and webpage font configuration
# =============================================================================

c.fonts.default_family = []
c.fonts.default_size = '10pt'
c.fonts.web.size.default = 16
c.fonts.web.size.default_fixed = 13

c.fonts.web.family.fixed = 'monospace'
c.fonts.web.family.sans_serif = 'monospace'
c.fonts.web.family.serif = 'monospace'
c.fonts.web.family.standard = 'monospace'


# =============================================================================
# Window Title
# =============================================================================

c.window.title_format = '{perc}{current_title}'


# =============================================================================
# Statusbar
# =============================================================================

c.statusbar.show = 'in-mode'


# =============================================================================
# Search & Completion
# Search engine and completion menu configuration
# =============================================================================
c.bindings.default = {}   
# ---------- Navigation ----------
config.bind('<Ctrl-l>', 'cmd-set-text -s :open')          # Focus address bar
config.bind('<F6>', 'cmd-set-text -s :open')
config.bind('<Alt-d>', 'cmd-set-text -s :open')
config.bind('<Ctrl-Shift-v>', 'open -- {clipboard}')       # Paste & go

config.bind('<Alt-Left>', 'back')
config.bind('<Alt-Right>', 'forward')
config.bind('<F5>', 'reload')
config.bind('<Ctrl-r>', 'reload')
config.bind('<Ctrl-Shift-r>', 'reload -f')                 # Hard reload

# ---------- Tabs ----------
config.bind('<Ctrl-t>', 'cmd-set-text -s :open -t')        # New tab
config.bind('<Ctrl-w>', 'tab-close')
config.bind('<Ctrl-Shift-t>', 'undo')                      # Reopen closed tab
config.bind('<Ctrl-Tab>', 'tab-next')
config.bind('<Ctrl-Shift-Tab>', 'tab-prev')
config.bind('<Ctrl-PgDown>', 'tab-next')
config.bind('<Ctrl-PgUp>', 'tab-prev')
config.bind('<Ctrl-Shift-PgDown>', 'tab-move +')
config.bind('<Ctrl-Shift-PgUp>', 'tab-move -')

for i in range(1, 9):
    config.bind(f'<Ctrl-{i}>', f'tab-focus {i}')
config.bind('<Ctrl-9>', 'tab-focus -1')                    # Last tab

config.bind('<Ctrl-n>', 'open -w')                         # New window
config.bind('<Ctrl-Shift-n>', 'open -p')                   # Private window

# ---------- Find in page ----------
config.bind('<Ctrl-f>', 'cmd-set-text /')
config.bind('<F3>', 'search-next')
config.bind('<Ctrl-g>', 'search-next')
config.bind('<Shift-F3>', 'search-prev')
config.bind('<Ctrl-Shift-g>', 'search-prev')

# ---------- Scrolling ----------
config.bind('<Down>', 'scroll down')
config.bind('<Up>', 'scroll up')
config.bind('<Left>', 'scroll left')
config.bind('<Right>', 'scroll right')
config.bind('<Space>', 'scroll-page 0 1')
config.bind('<Shift-Space>', 'scroll-page 0 -1')
config.bind('<Home>', 'scroll-to-perc 0')
config.bind('<End>', 'scroll-to-perc 100')

# ---------- Zoom ----------
config.bind('<Ctrl-=>', 'zoom-in')
config.bind('<Ctrl-+>', 'zoom-in')
config.bind('<Ctrl-->', 'zoom-out')
config.bind('<Ctrl-0>', 'zoom')

# ---------- Page / misc ----------
config.bind('<F11>', 'fullscreen')
config.bind('<Ctrl-u>', 'view-source')
config.bind('<F12>', 'devtools')
config.bind('<Ctrl-Shift-i>', 'devtools')
config.bind('<Ctrl-p>', 'print')
config.bind('<Ctrl-Shift-c>', 'yank')                      # Copy page URL

# ---------- Raindrop ----------
config.bind('<Ctrl-b>', 'open -t https://app.raindrop.io/my/0')
config.bind(
    '<Ctrl-d>',
    'open -t https://app.raindrop.io/add?link={url}&title={title}',
)                                                          # "Bookmark this page"

# ---------- Power toggles (Ctrl+Alt) ----------
config.bind('<Ctrl-Alt-d>', 'config-cycle colors.webpage.darkmode.enabled true false')
config.bind('<Ctrl-Alt-b>', 'config-cycle content.blocking.enabled true false')
config.bind('<Ctrl-Alt-t>', 'config-cycle tabs.position top left')
config.bind('<Ctrl-Alt-h>', 'config-cycle tabs.show multiple never')
config.bind('<Ctrl-Alt-s>', 'config-cycle statusbar.show always never')
config.bind('<Ctrl-Alt-p>', 'mode-enter passthrough')      # Let site handle all keys
config.bind('<Ctrl-Alt-w>', 'tab-only')                    # Close other tabs
config.bind('<Ctrl-Alt-c>', 'tab-clone')                   # Duplicate tab
config.bind('<Ctrl-Alt-n>', 'tab-give')                    # Tab -> new window
config.bind('<Ctrl-Alt-f>', 'hint links tab-bg --rapid')   # Rapid-open links in bg tabs
config.bind('<Ctrl-Alt-y>', 'hint links yank')
config.bind('<Ctrl-Alt-r>', 'config-source')               # Reload this config

# ---------- Command line (:) ----------
config.bind('<Return>', 'command-accept', mode='command')
config.bind('<Escape>', 'mode-leave', mode='command')
config.bind('<Tab>', 'completion-item-focus next', mode='command')
config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
config.bind('<Ctrl-n>', 'completion-item-focus next', mode='command')
config.bind('<Ctrl-p>', 'completion-item-focus prev', mode='command')
config.bind('<Up>', 'command-history-prev', mode='command')
config.bind('<Down>', 'command-history-next', mode='command')

# ---------- Prompts / yes-no dialogs ----------
config.bind('<Return>', 'prompt-accept', mode='prompt')
config.bind('<Escape>', 'mode-leave', mode='prompt')
config.bind('y', 'prompt-accept yes', mode='yesno')
config.bind('n', 'prompt-accept no', mode='yesno')
config.bind('<Return>', 'prompt-accept', mode='yesno')
config.bind('<Escape>', 'mode-leave', mode='yesno')

# ---------- Hints ----------
config.bind('<Return>', 'hint-follow', mode='hint')
config.bind('<Escape>', 'mode-leave', mode='hint')

# ---------- Insert / passthrough / caret ----------
config.bind('<Escape>', 'mode-leave', mode='insert')
config.bind('<Ctrl-e>', 'edit-text', mode='insert')        # Edit field in your editor
config.bind('<Shift-Escape>', 'mode-leave', mode='passthrough')
config.bind('<Escape>', 'mode-leave', mode='caret')

# =============================================================================
# Dark Mode & Webpage Color Scheme
# Webpage dark mode is disabled by default and can be toggled with `td`
# =============================================================================

c.colors.webpage.darkmode.enabled = False
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'never'
c.colors.webpage.preferred_color_scheme = 'auto'

config.set(
    'colors.webpage.darkmode.enabled',
    False,
    'file://*',
)


# =============================================================================
# Privacy & Content Settings
# WebGL, canvas, geolocation, WebRTC, and cookie behavior
# =============================================================================

config.set('content.webgl', False, '*')
config.set('content.canvas_reading', False)
config.set('content.geolocation', False)

config.set(
    'content.webrtc_ip_handling_policy',
    'default-public-interface-only',
)

config.set(
    'content.cookies.accept',
    'no-3rdparty',
)

config.set(
    'content.cookies.store',
    True,
)


# =============================================================================
# Ad Blocking
# Filter lists and blocking behavior
# =============================================================================

c.content.blocking.enabled = True
c.content.blocking.method = 'both'

c.content.blocking.adblock.lists = [
    'https://easylist.to/easylist/easylist.txt',
    'https://easylist.to/easylist/easyprivacy.txt',
    'https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/ultimate.txt',
    'https://raw.githubusercontent.com/DandelionSprout/adfilt/refs/heads/master/LegitimateURLShortener.txt',
    'https://gitflic.ru/project/magnolia1234/bypass-paywalls-clean-filters/blob/raw?file=bpc-paywall-filter.txt',

    # uBlock Origin's own default lists
    # 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt',       # malware/scam domains
    # 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt',      # uBO's core custom rules
    # 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt',       # extra tracking, complements EasyPrivacy

    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt',  # Site-breakage fixes — read below, this one matters
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt',  # Cookie banners, newsletter popups, social widgets
]


# =============================================================================
# Ad Blocking Whitelist
# =============================================================================

c.content.blocking.whitelist = [
    'https://app.raindrop.io/*',
]


# =============================================================================
# User Agent
# Browser identity presented to websites
# =============================================================================

config.set(
    'content.headers.user_agent',
    'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
)


# =============================================================================
# Custom Stylesheets
# Optional webpage-specific CSS modifications
# =============================================================================

# c.content.user_stylesheets = ["~/.config/qutebrowser/styles/youtube-tweaks.css"]

c.content.user_stylesheets = [
    '~/.config/qutebrowser/styles/hide-scrollbars.css',
]


# =============================================================================
# Media Playback
# Open media directly in mpv
# =============================================================================

config.bind(',m', 'spawn mpv {url}')
config.bind(',M', 'hint links spawn mpv {hint-url}')


# =============================================================================
# Qt / Wayland
# Prevent QtWebEngine from dropping frames under Wayland
# =============================================================================

c.qt.args = [
    'disable-gpu-compositing',
    'enable-gpu-rasterization',
]


# =============================================================================
# External Tools & Startpage
# Editor integration and custom start/new-tab page
# =============================================================================

# Open config-edit in Helix
c.editor.command = [
    'micro',
    '--wait',
    '{file}',
]

# Custom start page / new tab page
c.url.start_pages = 'file:///home/amm/.config/qutebrowser/startpage/index.html'
c.url.default_page = 'file:///home/amm/.config/qutebrowser/startpage/index.html'


# =============================================================================
# Window Transparency
# Real window transparency, for the transparent startpage background to show through
# =============================================================================

# c.window.transparent = True

# c.colors.webpage.bg = 'transparent'
