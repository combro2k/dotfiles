function tmux_wrapper --description "Load TMUX wrapper"
  set -g TMUX_STATE attached

  tmuxp load -y default

  if test -f ~/.no-logout
    rm ~/.no-logout

    set -g TMUX_STATE detached

    return 0
  end

  exec true
end 
