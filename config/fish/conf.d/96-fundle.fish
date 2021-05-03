if status --is-interactive
  if not functions -q fundle
    eval (curl -sfL https://git.io/fundle-install)
  end

  # Fish git prompt
  set fish_prompt_pwd_dir_length 0
  set -g theme_nerd_fonts yes
  #  set -g theme_color_scheme base16-dark

  # Use FZF new keybindings
  set -x FZF_LEGACY_KEYBINDINGS 0

  # list plugin dependencies
  fundle plugin 'smh/base16-shell-fish'
  fundle plugin 'jorgebucaran/fish-getopts'
#  fundle plugin 'fishpkg/fish-await'
  fundle plugin 'decors/fish-colored-man'
  fundle plugin 'tuvistavie/fish-completion-helpers'
  fundle plugin 'tuvistavie/oh-my-fish-core'
  fundle plugin 'tuvistavie/fish-completion-helpers'
  fundle plugin 'tuvistavie/fish-asdf'
  fundle plugin 'oh-my-fish/plugin-vcs'
  fundle plugin 'oh-my-fish/plugin-bang-bang'
  fundle plugin 'oh-my-fish/plugin-license'
  fundle plugin 'oh-my-fish/plugin-sudope'
  fundle plugin 'combro2k/fish-fzf'
  fundle plugin 'edc/bass'
  fundle plugin 'combro2k/theme-combro2k'

  fundle init
end
