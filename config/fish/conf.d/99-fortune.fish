if status --is-interactive
  if test -z $SUDO_USER; and test -f /usr/bin/fortune
    function fish_greeting
      /usr/bin/fortune -s
    end
  else if test -z $SUDO_USER; and test -f /usr/games/fortune
    function fish_greeting
      /usr/games/fortune -s
    end
  end
end
