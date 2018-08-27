function takeover
  if set -q TMUX
    tmux detach -a
  else
    echo "No TMUX loaded"
  end
end

