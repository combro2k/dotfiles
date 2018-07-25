from libqtile.config import Key, Drag, Click, ScratchPad
from libqtile.command import lazy
from classes import Helpers
from groups import groups

mod = "mod4"
alt = "mod1"

zenity_question = Helpers.zenity_question
rofi_drun = Helpers.rofi_drun
window_to_group = Helpers.window_to_group

window_to_prev_group = Helpers.window_to_prev_group
window_to_next_group = Helpers.window_to_next_group

keys = [
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),
    Key(["control"], "Tab", lazy.layout.next()),
    Key([mod, "shift"], "space", lazy.layout.rotate()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn('urxvtc-256color')),
    Key([mod], "Tab", lazy.next_layout()),
    Key([alt], "F4", lazy.window.kill()),
    Key([mod, "shift"], "Left", window_to_prev_group()),
    Key([mod, "shift"], "Right", window_to_next_group()),
    Key([mod, "shift"], "q", zenity_question(text="Logoff?", command="qtile-cmd -o cmd -f shutdown")),
    Key([mod, "control"], "q", zenity_question(text="Shutdown?", command="systemctl poweroff")),
    Key([mod, "control"], "r", zenity_question(text="Reboot?", command="systemctl reboot")),
    Key([mod], "space", rofi_drun()),
    Key([mod], "r", lazy.spawncmd()),
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('term')),
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
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
