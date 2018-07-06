if status --is-interactive
  if test -f /usr/bin/neofetch; and not set -q SUDO_USER
    if not set -q TMUX
      /usr/bin/neofetch
    else if [ "$TMUX_PANE" = '%1' ]
      /usr/bin/neofetch --off
    end
  end
end
