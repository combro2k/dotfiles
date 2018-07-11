# Use tmux when it's installed and is an SSH connection                                                                                                               
if type -qf tmux
  if status --is-login
    if not set -q TMUX; and set -q SSH_CONNECTION; and not set -q NOTMUX; and test ! -f $HOME/.notmux
      tmux_wrapper
    end
  end
end
