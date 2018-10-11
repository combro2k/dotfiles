from libqtile.config import Key, Drag, Click, ScratchPad
from libqtile.command import lazy
from classes import Helpers
from groups import groups
from extensions import *

mod = "mod4"
alt = "mod1"

app_or_group = Helpers.app_or_group

window_to_group = Helpers.window_to_group
window_to_prev_group = Helpers.window_to_prev_group
window_to_next_group = Helpers.window_to_next_group

windows_to_group = Helpers.windows_to_group
windows_to_prev_group = Helpers.windows_to_prev_group
windows_to_next_group = Helpers.windows_to_next_group
window_maximize = Helpers.window_maximize

create_screenshot = Helpers.create_screenshot
context_menu = Helpers.context_menu

minimize_group = Helpers.minimize_group
unminimize_group = Helpers.unminimize_group

toggle_follow_mouse_focus = Helpers.toggle_follow_mouse_focus

qtile_shutdown = Helpers.qtile_shutdown

keys = [
    Key([], "Print", create_screenshot()),
    Key([alt], "Print", create_screenshot(mode='window')),
    Key(["control"], "Print", create_screenshot(mode='select')),

    Key(["shift"], "Print", create_screenshot(clipboard=True)),
    Key([alt, "shift"], "Print", create_screenshot(mode='window', clipboard=True)),
    Key(["control", "shift"], "Print", create_screenshot(mode='select', clipboard=True)),

    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    Key([mod], "f", toggle_follow_mouse_focus()),

    Key([mod], "d", minimize_group()),
    Key([mod, "shift"], "d", unminimize_group()),

    Key([mod], "m", lazy.window.toggle_maximize()),
    Key([mod, "shift"], "m", lazy.window.toggle_minimize()),

    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    Key(["control"], "Tab", lazy.group.next_window()),
    Key(["control", "shift"], "Tab", lazy.group.prev_window()),

    Key([mod], "q", lazy.layout.toggle_split().when('bsp')),
    Key([mod], "n", lazy.layout.normalize().when('bsp')),

    Key([mod], "Return", lazy.spawn('urxvtc-256color')),
    Key([mod], "Tab", lazy.next_layout()),
    Key([alt], "F4", lazy.window.kill()),

    Key([mod], "Left", 
        lazy.layout.flip_left().when('bsp'),
        lazy.layout.rotate().when('stack'),
    ),
    Key([mod], "Right", 
        lazy.layout.flip_right().when('bsp'),
        lazy.layout.rotate().when('stack'),
    ),
    Key([mod], "Up", 
        lazy.layout.flip_up().when('bsp'),
        lazy.layout.shuffle_up().when('stack'),
    ),
    Key([mod], "Down", 
        lazy.layout.flip_down().when('bsp'),
        lazy.layout.shuffle_down().when('stack'),
    ),

    Key([mod, "shift"], "Left", window_to_prev_group()),
    Key([mod, "shift"], "Right", window_to_next_group()),

    Key([mod, "control"], "Left", windows_to_prev_group()),
    Key([mod, "control"], "Right", windows_to_next_group()),

    Key([mod, "shift"], "q", lazy.run_extension(Zenity(text="Logoff?", exec=lazy.shutdown()))),
    Key([mod, "control"], "q", lazy.run_extension(Zenity(text="Shutdown?", exec=lazy.spawn(['systemctl', 'poweroff'])))),
    Key([mod, "control"], "r", lazy.run_extension(Zenity(text="Reboot?", exec=lazy.spawn(['systemctl', 'reboot'])))),

    Key([mod], "space", lazy.run_extension(RofiMenu(modi="drun"))),
    Key([alt], "Tab", lazy.run_extension(RofiMenu(modi="windowcd"))),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('term')),

    Key([mod], "F1", app_or_group('Firefox', 'firefox')),
    Key([mod], "F2", app_or_group('Editors', 'urxvtc-256color -name emacs -e emacsclient -t')),
    Key([mod], "F3", app_or_group('E-Mail', 'thunderbird')),
#    Key([mod], "F3", app_or_group('GIMP', 'gimp')),
    Key([mod], "F4", app_or_group('WeeChat', 'urxvtc-256color -name WeeChat -e ssh weechat@vmaurik.nl -p 5000')),
    Key([mod], "F5", app_or_group('TeamViewer', 'teamviewer')),


    Key([], "F11", lazy.run_extension(Wallpaper())),

    Key([], "Menu", context_menu()),
]

for i in groups:
    if i.persist == True and not isinstance(i, ScratchPad):
        keys.extend([
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen()),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, window_to_group(i.name)),

            # mod1 + control + letter of group = switch to & move focused window to group
            Key([mod, "control"], i.name, windows_to_group(i.name)),
        ])

# Drag floating layouts.
mouse = [
    Drag(["control", alt], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag(["control", alt], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click(["control", alt], "Button2", lazy.window.bring_to_front()),
#    Click(["control", alt], "Button4", ),
    Click([alt], "Button3", context_menu()),
]
