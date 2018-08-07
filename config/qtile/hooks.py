from libqtile import hook
from libqtile.log_utils import logger
from libqtile.command import lazy
from classes import AutoStart, Wallpaper
from os import environ

from subprocess import run, PIPE

#import gi
#gi.require_version('Gdk', '3.0')
#from gi.repository import Gdk

@hook.subscribe.startup
def dbus_register():
    id = environ.get('DESKTOP_AUTOSTART_ID')
    if not id:
        return

    Popen(['dbus-send',
        '--session',
        '--print-reply',
        '--dest=org.gnome.SessionManager',
        '/org/gnome/SessionManager',
        'org.gnome.SessionManager.RegisterClient',
        'string:qtile',
        'string:' + id])


@hook.subscribe.startup_once
def autostart():
    AutoStart()

    pass

@hook.subscribe.addgroup
def group_created(qtile, group):
    if group == 'Firefox':
        if qtile.ready:
            qtile.groupMap[group].cmd_toscreen()

    if group == 'VisualCode':
        if qtile.ready:
            qtile.groupMap[group].cmd_toscreen()

    if group == 'Skype':
        if qtile.ready:
            qtile.groupMap[group].cmd_toscreen()

    if group == 'GIMP':
        if qtile.ready:
            qtile.groupMap[group].cmd_toscreen()

    if group == 'Builder':
        if qtile.ready:
            qtile.groupMap[group].cmd_toscreen()

@hook.subscribe.client_new
def specific_instance_rules(window):
    if window.match(wmclass='zenity'):
        above = window.qtile.conn.atoms["_NET_WM_STATE_ABOVE"]
        state = list(window.window.get_property('_NET_WM_STATE', 'ATOM', unpack=int))
        if not above in state:
            state.append(above)
        window.window.set_property('_NET_WM_STATE', state)

    if window.match(wmclass='pinentry-gtk-2'):
        logger.error(window)

    if window.match(wmclass='conky-sysinfo') or window.match(wmclass='conky-shortcuts'):
        window.static(0)

    if window.match(wmclass='qtile-actionmenu') or window.match(wmclass='qtile-contextmenu'):
        window.static(0)

    if window.match(wmclass='anbox'):
        window.floating = True

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    popup = window.window.get_wm_type() == 'popup'
    transient = window.window.get_wm_transient_for()
    if (dialog or transient) or popup:
        window.floating = True

@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
    if qtile.ready:
        try:
            return qtile.cmd_restart()
        except Exception as e:
            logger.error(e)

@hook.subscribe.startup_complete
def auto_screens():
    try:
        import re

        r = run(['xrandr', '--listactivemonitors'], stdout=PIPE)

#        logger.error(r.find(b'Monitors: '))

        logger.error(r)

    except Exception as e:
        logger.error(e)

@hook.subscribe.client_focus
def dim_inactive_urxvtc(window):
    if window.match(wmclass='urxvtc-256color'):
        qtile = window.qtile

        try:
            index = qtile.groups.index(qtile.currentGroup)
            group = qtile.groups[index]
            window.opacity = 1.0

            for w in group.windows:
                if w.match(wmclass='urxvtc-256color') and w.has_focus is False:
                    w.opacity = 0.70

        except Exception as e:
            logger.error(e)
