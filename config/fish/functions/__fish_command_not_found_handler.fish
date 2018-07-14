if test -x /usr/bin/command-not-found
  function __fish_command_not_found_handler --on-event fish_command_not_found
    /usr/bin/command-not-found $argv[1]
  end
end
