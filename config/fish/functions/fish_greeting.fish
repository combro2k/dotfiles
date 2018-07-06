function fish_greeting
  if test -z $SUDO_USER
    if not set -q TMUX
      /usr/bin/neofetch
    else if [ "$TMUX_PANE" = '%1' ]
      /usr/bin/neofetch --off
    end

    test -x /usr/bin/fortune; and /usr/bin/fortune -s
    test -x /usr/games/fortune; and /usr/games/fortune -s
    echo ""
    uname -snrmio
    uptime
  end
end
