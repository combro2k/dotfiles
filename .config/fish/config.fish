# Global settings

if status --is-interactive
	if not functions -q fundle; eval (curl -sfL https://git.io/fundle-install); end
end

test -z "$MOSH" 
	and set -g fish_term24bit 1
test -z "$SSH_AUTH_SOCK"
    	and set -x SSH_AUTH_SOCK (gpgconf --list-dirs agent-ssh-socket)

set -g -x SXHKD_SHELL '/usr/bin/sh'

# set paths
test -d ~/go/bin/
	and set -U fish_user_paths ~/go/bin $fish_user_paths

# Fish git prompt
set fish_prompt_pwd_dir_length 9999

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
fundle plugin 'oh-my-fish/theme-bira'

fundle init

# Start Neofetch if installed
#

if status --is-interactive; and test -z $SUDO_USER; and type "/usr/bin/neofetch" > /dev/null
	/usr/bin/neofetch
end

# vim:ft=fish
