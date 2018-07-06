function fish_greeting
  if test -z $SUDO_USER
    test -x /usr/bin/fortune; and /usr/bin/fortune -s
    test -x /usr/games/fortune; and /usr/games/fortune -s
    echo ""
    uname -snrmio
    uptime
  end
end
