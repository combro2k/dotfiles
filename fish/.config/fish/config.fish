# Global settings
set -g -x SXHKD_SHELL '/usr/bin/sh'
set -g -x TERMINAL '/usr/bin/urxvt'

if status --is-interactive
  if not functions -q fundle
    eval (curl -sfL https://git.io/fundle-install)
  end

  # Fish git prompt
  set fish_prompt_pwd_dir_length 9999
  # set -g theme_nerd_fonts yes
  # set -g theme_color_scheme terminal2-light-black

  # Use FZF new keybindings
  set -U FZF_LEGACY_KEYBINDINGS 0

  # list plugin dependencies
  fundle plugin 'fisherman/await'
  fundle plugin 'fisherman/choices'
  fundle plugin 'tuvistavie/fish-completion-helpers'
  fundle plugin 'fisherman/get'
  fundle plugin 'fisherman/getopts'
  fundle plugin 'fisherman/get_file_age'
  fundle plugin 'fisherman/last_job_id'
  fundle plugin 'fisherman/menu'

  # plugins
  fundle plugin 'tuvistavie/oh-my-fish-core'
  fundle plugin 'tuvistavie/fish-completion-helpers'
  fundle plugin 'oh-my-fish/plugin-vcs'
  fundle plugin 'oh-my-fish/plugin-bang-bang'
  fundle plugin 'oh-my-fish/plugin-license'
  fundle plugin 'oh-my-fish/plugin-sudope'
  fundle plugin 'fisherman/fzf'
  fundle plugin 'fisherman/docker-completion'
  fundle plugin 'edc/bass'

  # theme
  fundle plugin 'oh-my-fish/theme-bira'
  # fundle plugin 'oh-my-fish/theme-bobthefish'
  
  fundle init

  if test -z $SUDO_USER; and test -f /usr/bin/neofetch
    /usr/bin/neofetch
  end

  if test -f /usr/bin/lpass; and not test -z "$LP_EMAIL"
    function fpass -d "Fuzzy-find a Lastpass entry and copy the password"
      if not lpass status -q
        lpass login $LP_EMAIL
      end

      if not lpass status -q
        return 1
      end

      set id (lpass ls | fzf | string replace -r -a '.+\[id: (\d+)\]' '$1')

      if not test -z "$id"
        lpass show "$id"
      end
    end
  end

  function fssh -d "Fuzzy-find ssh host and ssh into it"
    if test -f ~/.ssh/config
      ssh (ag '^host [^*]' ~/.ssh/config | cut -d ' ' -f 2 | fzf)
    else
      echo "There is no config found in ~/.ssh/config"
      return 1
    end
  end

  test -z "$MOSH"; and set -g fish_term24bit 1

  test -z "$SSH_AUTH_SOCK";  and set -x SSH_AUTH_SOCK (gpgconf --list-dirs agent-ssh-socket)

  # set paths
  test -d ~/bin/; and set -U fish_user_paths ~/bin $fish_user_paths
  test -d ~/go/bin/; and set -U fish_user_paths ~/go/bin $fish_user_paths
  test -d ~/.cargo/bin/; and set -U fish_user_paths ~/.cargo/bin/ $fish_user_paths

  function ls --description 'List contents of directory'
    if type -qf exa
      eval exa $argv
    else
      /usr/bin/ls --color=auto $argv
    end
  end

  function emacs --description 'Star emacs'
    if type -qf emacs-nox
      eval /usr/bin/emacs-nox $argv
    else
      /usr/bin/emacs $argv
    end
  end

  function hc --description "Send a COMMAND with optional arguments ARGS to a running herbstluftwm instance."
    /usr/bin/herbstclient $argv
  end
end
# vim:ft=fish
