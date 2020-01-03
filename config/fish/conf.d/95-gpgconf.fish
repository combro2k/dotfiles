if type -fq gpgconf
  test -z "$SSH_AUTH_SOCK"; and set -x SSH_AUTH_SOCK (gpgconf --list-dirs agent-ssh-socket)
end

