
import os

from logging import getLogger

#from custom.functions import *
from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, extension
from libqtile.log_utils import logger
#from libqtile.extension import base

from subprocess import Popen, call, check_call, PIPE

try:
    from typing import List  # noqa: F401
except ImportError:
    pass

class AutoStart(object):
    def commands(self):
        yield '/usr/bin/compton'
        yield '/usr/bin/xautolock', '-time', '10', '-locker', 'xlock -mode blank'
        yield '/usr/bin/tilda', '-h'
        yield '/usr/bin/nm-applet'
        yield '/usr/bin/package-update-indicator'
        yield '/usr/lib/polkit-gnome-authentication-agent-1'
        yield '/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1'
        yield '/usr/bin/feh', '--bg-scale', '--randomize', os.path.expanduser('~/.config/backgrounds/'), '-Z'
        yield '/usr/bin/clipit'

    def __init__(self):
        self.run()

    def run(self):
        from pprint import pprint
        logger.error('Starting class AutoStart')
        for i in self.commands():
            if i is None:
                continue
            x = os.path.expanduser(i if type(i) is str else list(i)[0])
            if not os.access(x, os.X_OK):
                logger.error('Does not exist or is not executable: %s' % x)
                continue

            c = [x] if type(i) is str else list(i)
            logger.info('Running Popen with: %s' % c)
            Popen(c, shell=False)

#class Zenity(base.RunCommand):
#    defaults = [
#        ("zenity_command", 'dmenu', "the zenity command to be launched"),
#        ("zenity_question", True, "it is an question"),
#        ("zenity_title", None, "it is an question"),
#        ("zenity_text", None, "it is an question"),
#    ]
#
#    def __init__(self, **config):
#        base.RunCommand.__init__(self, **config)
#        self.add_defaults(Zenity.defaults)
#
#    def _configure(self, qtile):
#        base.RunCommand._configure(self, qtile)
#
#        if self.zenity_question:
#            self.configured_command.append("--question")
#
#        if self.zenity_text:
#            self.configure_command.append("--text", str(self.zenity_text))
#
#        if self.zenity_title:
#            self.configure_command.append("--title", str(self.zenity_title))
#
#
#    def run(self, items=None):
#        proc = super(Zenity, self).run()
#
#        return proc

class Colors(object):
    bg = '666666'
    highlight_bg = '888888'
    urgent_bg = 'fe8964'
    text = 'ffffff'
    inactive_text = '333333'
    border = '333333'
    border_focus = urgent_bg
    highlight_text = urgent_bg

def rofi_drun():
    @lazy.function
    def f(qtile):
        Popen(['sh', '-c', 'rofi -theme base16-twilight -demnu -show drun -modi drun'], shell=False)

    return f

def zenity_question(command, title="Question", text="Are you sure?"):
    @lazy.function
    def f(qtile):
        try:
            Popen(['sh', '-c', f'zenity --question --title="{title}" --text="{text}" && {command}'], shell=False)
        except subprocess.CalledProcessError as e:
            logger.error(e)

    return f

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
    Key([mod], "0", zenity_question(text="Logoff?", command="qtile-cmd -o cmd -f shutdown")),
    Key([mod, "control"], "q", zenity_question(text="Shutdown?", command="systemctl poweroff")),
    Key([mod, "control"], "r", zenity_question(text="Reboot?", command="systemctl reboot")),

    Key([mod], "space", rofi_drun()),
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

groups.append(
    Group(
        name='Firefox',
        matches=[Match(wm_class=["Firefox"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label='Firefox',
    ))

layouts = [
    layout.Bsp(),
    layout.Max(),
]

widget_defaults = dict(
    font='Cousine Nerd Font Mono',
    fontsize=16,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
                widget.GroupBox(padding=2, fontsize=14),
                widget.Prompt(),
                widget.WindowName(),
                widget.Clock(format='⏰ %Y-%m-%d %a %I:%M %p'),
                widget.Systray(),
            ],
            size=24,
            background='#1d1f21',
            opacity=0.60
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

@hook.subscribe.startup_once
def autostart_once():
    AutoStart()

@hook.subscribe.addgroup
def firefox_group_created(qtile, group):
    if group == 'Firefox':
        if qtile.ready:
            qtile.groupMap[group].cmd_toscreen() 

@hook.subscribe.client_new
def register_zenity_instance(window):
    if window.match(wmclass='zenity'):
        above = window.qtile.conn.atoms["_NET_WM_STATE_ABOVE"]
        state = list(window.window.get_property('_NET_WM_STATE', 'ATOM', unpack=int))
        if not above in state:
            state.append(above)
        window.window.set_property('_NET_WM_STATE', state)

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    popup = window.window.get_wm_type() == 'popup'
    transient = window.window.get_wm_transient_for()
    if (dialog or transient) or popup:
        window.floating = True

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
