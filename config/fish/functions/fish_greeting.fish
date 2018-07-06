function fish_greeting
  set -q SUDO_USER; and return

  if set -q TMUX; and test "$TMUX_PANE" != '%1'
    return
  end

  set -q TMUX; and /usr/bin/neofetch --off; or /usr/bin/neofetch
  type -q fortune; and fortune -s

  echo ""
  uname -snrmio
  uptime

  return
end
