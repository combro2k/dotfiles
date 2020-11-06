function fish_greeting
  set -q SUDO_USER; and return
  set -q TMUX_STATE; and return

  if set -q TMUX; and test "$TMUX_PANE" != '%1'
    return
  end

  if type -fq archey
    archey
    #set -q TMUX; and neofetch --off; or neofetch
  end

  if type -fq fortune
    fortune -s
  end

  echo ""
  uname -snrmio
  uptime

  return
end
