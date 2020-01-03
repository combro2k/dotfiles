function fish_greeting
  set -q SUDO_USER; and return
  set -q TMUX_STATE; and return

  if set -q TMUX; and test "$TMUX_PANE" != '%1'
    return
  end

  type -fq neofetch; and set -q TMUX; and neofetch --off; or neofetch
  type -fq fortune; and fortune -s

  echo ""
  uname -snrmio
  uptime

  return
end
