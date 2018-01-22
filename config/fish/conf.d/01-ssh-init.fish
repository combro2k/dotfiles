# Use tmux when it's installed and is an SSH connection                                                                                                               
if type -qf tmux
  if status --is-login
    if test -z "$TMUX"; and test "$SSH_CONNECTION" != ""; and test -z "$NOTMUX"; and test ! -f $HOME/.notmux
      tmuxp load -y default

      exec true
    end
  end
end
