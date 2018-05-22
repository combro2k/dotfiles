# set paths

if status --is-interactive
  test -d ~/bin; and if not contains ~/bin $PATH; echo "Append ~/bin to PATH"; set -U fish_user_paths ~/bin $fish_user_paths; end
  test -d ~/.local/bin/; and if not contains ~/.local/bin $PATH; echo "Append ~/.local/bin to PATH"; set -U fish_user_paths ~/.local/bin $fish_user_paths; end
  test -d ~/go/bin; and if not contains ~/go/bin $PATH; echo "Append ~/go/bin to PATH"; set -U fish_user_paths ~/go/bin $fish_user_paths; end
  test -d ~/.cargo/bin/; and if not contains ~/.cargo/bin/ $PATH; echo "Append ~/.cargo/bin to PATH"; set -U fish_user_paths ~/.cargo/bin/ $fish_user_paths; end
end
