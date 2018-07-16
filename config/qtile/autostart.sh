#!/usr/bin/env sh

export TERMINAL='/usr/bin/urxvt'

test -x /usr/lib/polkit-gnome-authentication-agent-1 && /usr/lib/polkit-gnome-authentication-agent-1 &
test -x /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 && /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
test -x /usr/bin/nitrogen && /usr/bin/nitrogen --restore
test -x /usr/bin/feh && /usr/bin/feh --bg-scale --randomize ~/.config/bspwm/backgrounds/ -Z

sleep 1

test -x /usr/bin/compton && /usr/bin/compton &
test -x /usr/bin/kalu && /usr/bin/kalu &
test -x /usr/bin/nm-applet && /usr/bin/nm-applet &
test -x /usr/bin/package-update-indicator && /usr/bin/package-update-indicator &
test -x /usr/bin/clipit && /usr/bin/clipit &
test -x /usr/bin/conky && /usr/bin/conky -c ~/.config/conky/conky.conf &
test -x /usr/bin/conky && /usr/bin/conky -c ~/.config/conky/conky-shortcuts.conf &
test -x /usr/bin/xautolock && /usr/bin/xautolock -time 10 -locker 'xlock -mode blank' &
test -x /usr/bin/tilda && /usr/bin/tilda -h &
