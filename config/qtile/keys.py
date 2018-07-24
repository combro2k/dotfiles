from libqtile.config import Key, Drag, Click
from libqtile.command import lazy

from classes import Helpers

mod = "mod4"
ctrl = "control"

keys = [
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),
    Key([mod, ctrl], "k", lazy.layout.shuffle_down()),
    Key([mod, ctrl], "j", lazy.layout.shuffle_up()),
    Key([ctrl], "Tab", lazy.layout.next()),
    Key([mod, "shift"], "space", lazy.layout.rotate()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn('urxvt-256color')),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

#    Key([mod], "t", lazy.run_extension(Zenity(
#        zenity_question=True,
#        zenity_text="Test",
#        zenity_title="test",
#    ))),

    Key([mod], "0", Helpers.zenity_question(text="Logoff?", command="qtile-cmd -o cmd -f shutdown")),
    Key([mod, "control"], "q", Helpers.zenity_question(text="Shutdown?", command="systemctl poweroff")),
    Key([mod, "control"], "r", Helpers.zenity_question(text="Reboot?", command="systemctl reboot")),

    Key([mod], "space", Helpers.rofi_drun()),
    Key([mod], "r", lazy.spawncmd()),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]