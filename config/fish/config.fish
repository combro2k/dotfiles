# Global settings
set -g -x SXHKD_SHELL '/usr/bin/sh'
set -g -x TERMINAL '/usr/bin/urxvt'

# Use tmux when it's installed and is an SSH connection
if type -qf tmux
  if status --is-login
    if test -z "$TMUX"; and test "$SSH_CONNECTION" != ""; and test -z "$NOTMUX"
      tmux attach-session -t "$USER-tmux"; or tmux new-session -s "$USER-tmux"
      exec true
    end
  end
end