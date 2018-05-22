if status --is-interactive
  if test -z $SUDO_USER; and test -f /usr/bin/neofetch
    /usr/bin/neofetch
  end
end
