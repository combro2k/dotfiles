if status --is-interactive
  if not functions -q fundle
    eval (curl -sfL https://git.io/fundle-install)
  end

  # Fish git prompt
  set fish_prompt_pwd_dir_length 0
  set -g theme_nerd_fonts yes
  set -g theme_color_scheme base16-dark

  # Use FZF new keybindings
  set -x FZF_LEGACY_KEYBINDINGS 0

  # list plugin dependencies
  fundle plugin 'fishpkg/fish-await'
  fundle plugin 'decors/fish-colored-man'
  fundle plugin 'tuvistavie/fish-completion-helpers'
  fundle plugin 'tuvistavie/oh-my-fish-core'
  fundle plugin 'tuvistavie/fish-completion-helpers'
  fundle plugin 'oh-my-fish/plugin-vcs'
  fundle plugin 'oh-my-fish/plugin-bang-bang'
  fundle plugin 'oh-my-fish/plugin-license'
  fundle plugin 'oh-my-fish/plugin-sudope'
  fundle plugin 'maman/plugin-gvm'
  fundle plugin 'jethrokuan/fzf'
  fundle plugin 'edc/bass'
  fundle plugin 'smh/base16-shell-fish'
  fundle plugin 'combro2k/theme-cmorrell-twilight'

  fundle init

  if functions -q base16
    base16 twilight
  end
end
