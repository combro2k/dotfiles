"""
    Combro2k's special config for Qtile
"""

# import classes, defines, layouts, keys, groups, screens, hooks

# from subprocess import Popen

from defines import *
from classes import *
from extensions import *
from layouts import *
from keys import *
from groups import *
from screens import *
from hooks import *

try:
    from typing import List  # noqa: F401
except ImportError:
    pass

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width=2,
    border_normal=Colors.border,
    border_focus=Colors.border_focus,
    float_rules=[
        dict(wmclass="skype"), 
        dict(wmclass="gimp"),
        dict(wmclass="pinentry-gtk-2"),
        dict(wmclass="pinentry-qt"),
        dict(wmclass="pinentry-qt5"),
        dict(wmclass="gcr-prompter"),
        dict(wmclass="zenity"),
        dict(wmclass="qtile-actionmenu"),
        dict(wmclass="YaST2"),
        dict(wmclass="nautilus"),
        dict(wmclass="gnome-calculator"),
    ],
    auto_float_types=[
        "notification",
        "toolbar",
        "splash",
        "dialog",
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"

def main(qtile):
    qtile.ready = True
