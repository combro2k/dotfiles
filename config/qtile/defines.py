def autostart():
    from os import path

    yield '/usr/bin/compton'
    yield '/usr/bin/xautolock', '-time', '10', '-locker', 'xlock -mode blank'
    yield '/usr/bin/tilda', '-h'
    yield '/usr/bin/nm-applet'
    yield '/usr/bin/package-update-indicator'
    yield '/usr/lib/polkit-gnome-authentication-agent-1'
    yield '/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1'
    yield '/usr/bin/feh', '--bg-scale', '--randomize', path.expanduser('~/.config/backgrounds/'), '-Z'
    yield '/usr/bin/clipit'
