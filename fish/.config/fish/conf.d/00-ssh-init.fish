if type -qf tmux                         
  if status --is-login                   
    if test -z "$TMUX"; and test "$SSH_CONNECTION" != ""                           
      tmux attach-session -t "$USER-tmux"; or tmux new-session -s "$USER-tmux"     
      exec true                          
    end                                  
  end                                    
end
