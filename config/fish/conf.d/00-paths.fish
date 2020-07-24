# set paths

if status --is-interactive
  # cleanup PATH
  set -g -x PATH

  # setup base path
  set -g -x PATH /usr/local/bin /usr/bin /bin /usr/sbin /sbin

  # specific paths if exists
  test -d ~/bin/; and set -g -x PATH $PATH ~/bin
  test -d ~/.local/bin/; and set -g -x PATH $PATH ~/.local/bin
  test -d ~/go/bin/; and set -g -x PATH $PATH ~/go/bin
  test -d ~/.cargo/bin/; and set -g -x PATH $PATH ~/.cargo/bin
  test -d ~/.linuxbrew/bin/; and set -g -x PATH $PATH ~/.linuxbrew/bin
  test -d ~/.fzf/bin/; and set -g -x PATH $PATH ~/.fzf/bin
  test -d ~/.luarocks/bin/; and set -g -x PATH $PATH ~/.luarocks/bin
  test -d /snap/bin/; and set -g -x PATH $PATH /snap/bin
end
