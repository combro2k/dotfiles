"""
    Combro2k's special config for Qtile
"""

# import classes, defines, layouts, keys, groups, screens, hooks

from subprocess import Popen

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
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
        border_width=2,
        border_normal=Colors.border,
        border_focus=Colors.border_focus,
        float_rules=[
            {'wmclass': 'confirm'},
            {'wmclass': 'dialog'},
            {'wmclass': 'download'},
            {'wmclass': 'error'},
            {'wmclass': 'file_progress'},
            {'wmclass': 'notification'},
            {'wmclass': 'splash'},
            {'wmclass': 'toolbar'},
            {'wmclass': 'confirmreset'},
            {'wmclass': 'makebranch'},
            {'wmclass': 'maketag'},
            {'wname': 'branchdialog'},
            {'wname': 'pinentry'},
            {'wmclass': 'pinentry-gtk-2'},
            {'wmclass': 'ssh-askpass'},
            {'wmclass': 'Tilda'},
            {'wmclass': 'gpk-update-viewer'},
            {'wmclass': 'package-update-indicator-prefs'},
        ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"

def main(qtile):
    qtile.ready = True
    pass
