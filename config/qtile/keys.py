from libqtile.config import Key, Drag, Click, ScratchPad
from libqtile.command import lazy
from classes import Helpers
from groups import groups
from extensions import *
from os.path import expanduser

mod = "mod4"
alt = "mod1"

app_or_group = Helpers.app_or_group
window_to_group = Helpers.window_to_group
window_to_prev_group = Helpers.window_to_prev_group
window_to_next_group = Helpers.window_to_next_group
window_maximize = Helpers.window_maximize
windows_to_group = Helpers.windows_to_group
windows_to_prev_group = Helpers.windows_to_prev_group
windows_to_next_group = Helpers.windows_to_next_group
minimize_group = Helpers.minimize_group
unminimize_group = Helpers.unminimize_group
toggle_minimize_group = Helpers.toggle_minimize_group
create_screenshot = Helpers.create_screenshot
create_video = Helpers.create_video
context_menu = Helpers.context_menu
toggle_follow_mouse_focus = Helpers.toggle_follow_mouse_focus
qtile_shutdown = Helpers.qtile_shutdown

keys = [
    Key([], "Print", create_screenshot(clipboard=False)),
    Key([alt], "Print", create_screenshot(mode='window', clipboard=False)),
    Key(["control"], "Print", create_screenshot(mode='select', clipboard=False)),

#    Key(["shift"], "Print", create_screenshot(clipboard=True)),
#    Key([alt, "shift"], "Print", create_screenshot(mode='window', clipboard=True)),
#    Key(["control", "shift"], "Print", create_screenshot(mode='select', clipboard=True)),

    Key([mod], "Print", create_video()),
    Key([mod,  "shift"], "Print", create_video(mode='window')),

    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    Key([mod], "f", toggle_follow_mouse_focus()),

    Key([mod], "v", lazy.spawn(["/usr/bin/copyq", "toggle"])),

    Key([mod], "d", toggle_minimize_group()),
    # Key([mod, "shift"], "d", unminimize_group()),

    Key([mod], "m", lazy.window.toggle_maximize()),
    Key([mod, "shift"], "m", lazy.window.toggle_minimize()),
    Key([mod], "f", lazy.window.toggle_floating()),

    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    Key(["control"], "Tab", lazy.group.next_window()),
    Key(["control", "shift"], "Tab", lazy.group.prev_window()),

    Key([mod], "q", lazy.layout.toggle_split().when('bsp')),
    Key([mod], "n", 
        lazy.layout.reset_size().when('plasma'),
        lazy.layout.normalize().when('bsp'),
    ),

    Key([mod], "Return",
        lazy.layout.mode_horizontal().when('plasma'),
        lazy.spawn('urxvtc-256color')
    ),
    Key([mod, alt], "Return",
        lazy.layout.mode_vertical().when('plasma'),
        lazy.spawn('urxvtc-256color')
    ),

    Key([mod], "Tab", lazy.next_layout()),
    Key([alt], "F4", lazy.window.kill()),

    Key([mod], "Left", 
        lazy.layout.move_left().when('plasma'),
        lazy.layout.shuffle_left().when('bsp'),
        lazy.layout.rotate().when('stack'),
    ),
    Key([mod], "Right",
        lazy.layout.move_right().when('plasma'),
        lazy.layout.shuffle_right().when('bsp'),
        lazy.layout.rotate().when('stack'),
    ),
    Key([mod], "Up",
        lazy.layout.move_up().when('plasma'),
        lazy.layout.shuffle_up().when('bsp'),
        lazy.layout.shuffle_up().when('stack'),
    ),
    Key([mod], "Down",
        lazy.layout.move_down().when('plasma'),
        lazy.layout.shuffle_down().when('bsp'),
        lazy.layout.shuffle_down().when('stack'),
    ),

    Key([mod, alt], "Left",
        lazy.layout.integrate_left().when('plasma')
    ),
    Key([mod, alt], "Right",
        lazy.layout.integrate_right().when('plasma')
    ),
    Key([mod, alt], "Up",
        lazy.layout.integrate_up().when('plasma')
    ),
    Key([mod, alt], "Down",
        lazy.layout.integrate_down().when('plasma')
    ),

    # Key([alt, "control"], "Left", lazy.layout.grow_left().when('bsp')),
    # Key([alt, "control"], "Right", lazy.layout.grow_right().when('bsp')),
    # Key([alt, "control"], "Up", lazy.layout.grow_up().when('bsp')),
    # Key([alt, "control"], "Down", lazy.layout.grow_down().when('bsp')),

    Key([mod, "shift"], "Left", window_to_prev_group()),
    Key([mod, "shift"], "Right", window_to_next_group()),

    Key([mod, "control"], "Left", windows_to_prev_group()),
    Key([mod, "control"], "Right", windows_to_next_group()),

    Key([mod, "shift"], "q", lazy.run_extension(Zenipy(text="Logoff?", exec=lazy.shutdown()))),
    Key([mod, "control"], "q", lazy.run_extension(Zenipy(text="Shutdown?", exec=lazy.spawn(['systemctl', 'poweroff'])))),
    Key([mod, "control"], "r", lazy.run_extension(Zenipy(text="Reboot?", exec=lazy.spawn(['systemctl', 'reboot'])))),

    Key([mod], "space", lazy.run_extension(RofiMenu(modi="drun"))),
    Key([alt], "Tab", lazy.run_extension(RofiMenu(modi="windowcd"))),
    Key([mod, "shift"], "r", lazy.restart()),

    Key([], 'F10', lazy.group['dropdown'].dropdown_toggle('qutebrowser')),
    Key([], 'F11', lazy.group['dropdown'].dropdown_toggle('weechat')),
    Key([], 'F12', lazy.group['dropdown'].dropdown_toggle('term')),

    Key([mod], "F1", app_or_group('WWW', '~/.local/bin/qutebrowser')),
    Key([mod], "F2", app_or_group('Editors', 'urxvtc-256color -bg "#1e1e1e" -name emacs -e emacsclient -t')),
    Key([mod], "F3", app_or_group('E-Mail', 'thunderbird')),
    Key([mod], "F5", app_or_group('TeamViewer', 'teamviewer')),
    Key([mod], "F6", app_or_group('RPD', '~/.local/bin/xfreerdpui')),
    Key([mod], "F7", lazy.spawn([
        expanduser('~/.local/bin/lastpass-gtk')
    ])),


    Key([mod], "r", app_or_group('RPD', '~/.local/bin/xfreerdpui')),
    Key([mod], "p", lazy.spawn([
        expanduser('~/.local/bin/lastpass-gtk')
    ])),

#    Key([], "F10", lazy.run_extension(Wallpaper())),

    Key([], "Menu", context_menu()),

    # Specific XF86 keys
    Key([], "XF86MyComputer", lazy.spawn(["xdg-open", "."])),
    Key([], "XF86Calculator", lazy.spawn(["gnome-calculator"])),
    Key([], "XF86HomePage", app_or_group('WWW', '~/.local/bin/qutebrowser')),
    Key([], "XF86Mail", app_or_group('E-Mail', 'thunderbird')),
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
    Click([alt], "Button3", context_menu()),
]
