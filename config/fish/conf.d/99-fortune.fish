if status --is-login
  if test -z $SUDO_USER; and test -f /usr/bin/fortune
    /usr/bin/fortune -s
  end
end
