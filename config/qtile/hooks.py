from libqtile import hook

@hook.subscribe.startup_once
def autostart_once():
    # needed imports for the function
    from classes import AutoStart
    from defines import autostart

    AutoStart(autostart())

@hook.subscribe.addgroup
def group_created(qtile, group):
    if group == 'Firefox':
        if qtile.ready:
            qtile.groupMap[group].cmd_toscreen()

    if group == 'VisualCode':
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
