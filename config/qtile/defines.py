def autostart():
    from os.path import expanduser

    yield '/usr/bin/vmware-user-suid-wrapper'
    yield '/usr/bin/ibus-daemon', '--xim'
    yield '/usr/bin/conky', '-c', expanduser('~/.config/conky/conky.conf')
    yield '/usr/bin/xautolock', '-time', '10', '-locker', 'slock'
    yield '/usr/bin/emacs-nox', '--daemon'
    yield '/usr/bin/nm-applet'
    yield '/usr/bin/package-update-indicator'
    yield '/usr/lib/polkit-gnome-authentication-agent-1'
    yield '/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1'
    yield '/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1'
#    yield '/usr/bin/clipit'
    yield '/usr/lib/gpaste/gpaste-daemon'
    yield '/usr/lib/x86_64-linux-gnu/gpaste/gpaste-daemon'
    yield '/usr/bin/blueman-applet'
    yield '/usr/lib64/libexec/kdeconnectd'
    yield '/usr/bin/kdeconnect-indicator'
    yield '/usr/bin/urxvtd', '-o', '-q', '-m'
    yield '/usr/bin/compton', '-b'
    yield '/usr/bin/simplescreenrecorder', '--start-hidden'
    yield '/usr/bin/xsetroot', '-name', 'Qtile', '-bg', '#323637', '-fg', '#323637', '-solid', '#323637'
    yield '/usr/bin/copyq'
    yield '/usr/bin/nitrogen', '--restore'
