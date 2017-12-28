# set paths
test -d ~/bin/; and set -U fish_user_paths ~/bin $fish_user_paths
test -d ~/go/bin/; and set -U fish_user_paths ~/go/bin $fish_user_paths
test -d ~/.cargo/bin/; and set -U fish_user_paths ~/.cargo/bin/ $fish_user_paths
