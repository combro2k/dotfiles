if status --is-interactive
  if test -z $SUDO_USER; and test -f /usr/bin/fortune
    function fish_greeting
      /usr/bin/fortune -s
    end
  end
end
