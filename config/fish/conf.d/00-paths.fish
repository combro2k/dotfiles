# set paths

if status --is-interactive
  test -d ~/bin; and if not contains ~/bin $PATH; set -U fish_user_paths ~/bin $fish_user_paths; end
  test -d ~/.local/bin/; and if not contains ~/.local/bin $PATH; set -U fish_user_paths ~/.local/bin $fish_user_paths; end
  test -d ~/go/bin; and if not contains ~/go/bin $PATH; set -U fish_user_paths ~/go/bin $fish_user_paths; end
  test -d ~/.cargo/bin/; and if not contains ~/.cargo/bin/ $PATH; set -U fish_user_paths ~/.cargo/bin/ $fish_user_paths; end
  #  test -d /snap/bin/; and if not contains /snap/bin $PATH; set -U fish_user_paths /snap/bin/ $fish_user_paths; end
end
