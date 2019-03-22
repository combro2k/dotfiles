def autostart():
    from os.path import expanduser

    yield '/usr/bin/ibus-daemon', '--xim'
    yield '/usr/bin/conky', '-c', expanduser('~/.config/conky/conky.conf')
    yield '/usr/bin/xautolock', '-time', '10', '-locker', 'xlock -mode blank'
    yield '/usr/bin/emacs-nox', '--daemon'
    yield '/usr/bin/nm-applet'
    yield '/usr/bin/package-update-indicator'
    yield '/usr/lib/polkit-gnome-authentication-agent-1'
    yield '/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1'
#    yield '/usr/bin/clipit'
    yield '/usr/lib/gpaste/gpaste-daemon'
    yield '/usr/bin/vmware-user-suid-wrapper'
    yield '/usr/bin/blueman-applet'
    yield '/usr/lib64/libexec/kdeconnectd'
    yield '/usr/bin/kdeconnect-indicator'
    yield '/usr/bin/urxvtd-256color', '-o', '-q', '-m'
