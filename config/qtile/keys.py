from libqtile.config import Key, Drag, Click, ScratchPad
from libqtile.command import lazy
from classes import Helpers
from groups import groups

mod = "mod4"
alt = "mod1"

app_or_group = Helpers.app_or_group
zenity_question = Helpers.zenity_question

rofi_drun = Helpers.rofi_drun
rofi_windowcd = Helpers.rofi_windowcd

window_to_group = Helpers.window_to_group
window_to_prev_group = Helpers.window_to_prev_group
window_to_next_group = Helpers.window_to_next_group
window_maximize = Helpers.window_maximize

create_screenshot = Helpers.create_screenshot

context_menu = Helpers.context_menu

minimize_group = Helpers.minimize_group
unminimize_group = Helpers.unminimize_group

keys = [
    Key([], "Print", create_screenshot()),
    Key([alt], "Print", create_screenshot(mode='window')),
    Key(["control"], "Print", create_screenshot(mode='select')),

    Key(["shift"], "Print", create_screenshot(clipboard=True)),
    Key([alt, "shift"], "Print", create_screenshot(mode='window', clipboard=True)),
    Key(["control", "shift"], "Print", create_screenshot(mode='select', clipboard=True)),

    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    Key([mod], "d", minimize_group()),
    Key([mod, "shift"], "d", unminimize_group()),

    Key([mod], "m", lazy.window.toggle_maximize()),
    Key([mod, "shift"], "m", lazy.window.toggle_minimize()),

    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    Key(["control"], "Tab", lazy.group.next_window()),
    Key(["control", "shift"], "Tab", lazy.group.prev_window()),

    Key([mod, "shift"], "space", lazy.layout.toggle_split().when('bsp')),

    Key([mod], "Return", lazy.spawn('urxvtc-256color')),
    Key([mod], "Tab", lazy.next_layout()),
    Key([alt], "F4", lazy.window.kill()),

    Key([mod], "Left", lazy.layout.flip_left().when('bsp')),
    Key([mod], "Right", lazy.layout.flip_right().when('bsp')),
    Key([mod], "Up", lazy.layout.flip_up().when('bsp')),
    Key([mod], "Down", lazy.layout.flip_down().when('bsp')),

    Key([mod, "shift"], "Left", window_to_prev_group()),
    Key([mod, "shift"], "Right", window_to_next_group()),

    Key([mod, "shift"], "q", zenity_question(text="Logoff?", command="qtile-cmd -o cmd -f shutdown")),
    Key([mod, "control"], "q", zenity_question(text="Shutdown?", command="systemctl poweroff")),
    Key([mod, "control"], "r", zenity_question(text="Reboot?", command="systemctl reboot")),
    Key([mod], "space", rofi_drun()),
    Key([alt], "Tab", rofi_windowcd()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('term')),

    Key([mod, "shift"], "F1", app_or_group('Firefox', 'firefox')),
    Key([mod, "shift"], "F2", app_or_group('VisualCode', 'code')),
    Key([mod, "shift"], "F3", app_or_group('Anbox', 'anbox.appmgr')),
    Key([mod, "shift"], "F4", app_or_group('GIMP', 'gimp')),
    Key([mod, "shift"], "F5", app_or_group('Skype', 'skypeforlinux')),
]

for i in groups:
    if i.persist == True and not isinstance(i, ScratchPad):
        keys.extend([
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen()),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, window_to_group(i.name)),
        ])

# Drag floating layouts.
mouse = [
    Drag([mod, alt], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod, alt], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod, alt], "Button2", lazy.window.bring_to_front()),
    Click([alt], "Button3", context_menu()),
]
