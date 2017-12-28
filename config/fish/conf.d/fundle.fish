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
  fundle plugin 'oh-my-fish/plugin-rustup'
  fundle plugin 'fisherman/fzf'
  fundle plugin 'fisherman/docker-completion'
  fundle plugin 'edc/bass'

  # theme
  fundle plugin 'oh-my-fish/theme-bira'
  #fundle plugin 'oh-my-fish/theme-bobthefish'

  fundle init
end
