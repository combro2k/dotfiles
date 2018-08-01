from libqtile import hook
from libqtile.log_utils import logger
from classes import AutoStart


@hook.subscribe.startup
def autostart():
    AutoStart()

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


@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    popup = window.window.get_wm_type() == 'popup'
    transient = window.window.get_wm_transient_for()
    if (dialog or transient) or popup:
        window.floating = True
