# Base16 Shell
if status --is-interactive
  set BASE16_SHELL_HOOKS "$HOME/.config/base16-shell-hooks/"
  set BASE16_SHELL "$HOME/.config/base16-shell/"
  source "$BASE16_SHELL/profile_helper.fish"
end
