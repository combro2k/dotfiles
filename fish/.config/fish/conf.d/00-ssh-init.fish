if type -qf tmux
  if test -z "$TMUX"; and test "$SSH_CONNECTION" != ""
    tmux attach-session -t ssh_tmux; or tmux new-session -s ssh_tmux
  end
end
