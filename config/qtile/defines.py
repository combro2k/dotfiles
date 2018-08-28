def autostart():
    from os.path import expanduser

    #yield '/usr/bin/feh', '--bg-scale', '--randomize', expanduser('~/.config/backgrounds/'), '-Z'

    yield '/usr/bin/ibus-daemon', '--xim'
    
    yield '/usr/bin/conky', '-c', expanduser('~/.config/conky/conky.conf')
#    yield '/usr/bin/conky', '-c', expanduser('~/.config/conky/conky-shortcuts.conf')

    yield '/usr/bin/xautolock', '-time', '10', '-locker', 'xlock -mode blank'
    yield '/usr/bin/urxvtd-256color', '-o', '-q'

    # broken?
    yield '/usr/bin/nm-applet'
    yield '/usr/bin/package-update-indicator'

    yield '/usr/lib/polkit-gnome-authentication-agent-1'
    yield '/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1'
#    yield '/usr/bin/gnome-keyring-daemon', '-f', '--start', '--components=ssh'

    yield '/usr/bin/clipit'

    yield '/usr/bin/compton', '--dbus'

    yield '/usr/bin/vmware-user-suid-wrapper'

