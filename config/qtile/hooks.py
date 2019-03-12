from os import environ
from subprocess import Popen, run, PIPE

from libqtile import hook
from libqtile.log_utils import logger
from libqtile.command import lazy
from libqtile.manager import Qtile
from libqtile.window import Window

from classes import AutoStart
from extensions import Wallpaper

@hook.subscribe.startup_complete
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

@hook.subscribe.startup
def autostart():
    AutoStart()

    # set wallpaper :-)
    wallpaper = Wallpaper()
    wallpaper.run()

@hook.subscribe.startup_complete
def auto_screens():
    r = run(['sh', '-c', 'xrandr --listactivemonitors | head -n1'], stdout=PIPE, universal_newlines=True)
    logger.error(f'Found {r.stdout} displays')
    run(['pkill', '-SIGHUP', 'conky'])

@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
    if qtile.ready:
        try:
            return qtile.cmd_restart()
        except Exception as e:
            logger.error(e)

@hook.subscribe.addgroup
def group_created(qtile, group):
    if not qtile.ready:
        return False

    if  ((group == 'WWW') or (group == 'Editors') or (group == 'Skype') or (group == 'GIMP') or (group == 'Builder') or (group == 'TeamViewer') or (group == 'WeeChat') or (group == 'E-Mail') or (group == 'RDP')):
        qtile.groupMap[group].cmd_toscreen()

@hook.subscribe.client_new
def specific_instance_rules(window): # type: Window
    qtile = window.qtile
    if window.match(wmclass='zenity') or window.match(wmclass='qtile-actionmenu'):
        wmtype = qtile.conn.atoms["_NET_WM_WINDOW_TYPE_DOCK"]
        state = list(window.window.get_property('_NET_WM_WINDOW_TYPE', 'ATOM', unpack=int))
        if not wmtype in state:
            state.append(wmtype)
        window.window.set_property('_NET_WM_WINDOW_TYPE', state)
        window.above = True
    if window.match(wmclass='skype'):
        window.cmd_set_size_floating(w=1512,h=800, curx=0, cury=0)
