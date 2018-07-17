# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os


#from custom.functions import *
from subprocess import Popen, PIPE, STDOUT
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.log_utils import logger

from xcffib.xproto import StackMode

try:
    from typing import List  # noqa: F401
except ImportError:
    pass

class Commands(object):
    autostart = { 
            '/usr/bin/compton': None,
            '/usr/bin/xautolock': '-time 10 -locker \'xlock -mode blank\'',
            '/usr/bin/tilda': '-h',
            '/usr/bin/nm-applet': None,
            '/usr/bin/package-update-indicator': None,
            '/usr/lib/polkit-gnome-authentication-agent-1': None,
            '/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1': None,
            '/usr/bin/feh': '--bg-scale --randomize ~/.config/bspwm/backgrounds/ -Z',
            '/usr/bin/clipit': None,
    }

    def __init__():
        pass

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("urxvt-256color")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod], "0", lazy.shutdown()),
    Key([mod, "control"], "q", lazy.spawn([
        "sh",
        "-c",
        "zenity --question --text='Shutdown?' && systemctl poweroff",
    ])),
    Key([mod, "control"], "r", lazy.spawn([
        "sh",
        "-c",
        "zenity --question --text='Reboot?' && systemctl reboot",
    ])),
    Key([mod], "r", lazy.spawncmd()),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.Bsp(),
    layout.Max(),
]

widget_defaults = dict(
    font='Cousine Nerd Font Mono',
    fontsize=16,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.Systray(),
            ],
            26,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'pinentry-gtk-2'}, # Pinentry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'Tilda'}, # tilda fun
    {'wmclass': 'gpk-update-viewer'}, # package-updater-indicator
    {'wmclass': 'package-update-indicator-prefs'}, # package-update-indicator
])
auto_fullscreen = True
focus_on_window_activation = "smart"


@hook.subscribe.client_new
def register_zenity_instance(window):
    if window.match(wmclass='zenity'):
        window.window.configure(stackmode=StackMode.Above)
        window.static(0)

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    for command, args in Commands.autostart.items():
        logger.info('Command to run: %s with arguments: %s' % (command, args))
        if not os.access(command, os.X_OK):
            logger.error('Does not exist or is not executable: %s' % command)
        else:
            if not args is None:
                command = '%s %s' % (command, args)
            
            logger.error('Run with args: %s' % command)

            Popen([command], shell=True, stderr=STDOUT) 

#@hook.subscribe.startup
#def dbus_register():
#    x = os.environ.get('DESKTOP_AUTOSTART_ID', '0')
#    subprocess.call(['dbus-send',
#        '--session',
#        '--print-reply=literal',
#        '--dest=org.gnome.SessionManager',
#        '/org/gnome/SessionManager',
#        'org.gnome.SessionManager.RegisterClient',
#        'string:qtile',
#        'string:' + x])


def main(qtile):
    pass 
