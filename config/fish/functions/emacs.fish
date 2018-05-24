function emacs --description 'Star emacs'
  if not type -qf emacs; and not type -qf emacs-nox
    echo "Emacs is not installed, install it first!"

    return 1
  end

  if set -q DISPLAY
    eval /usr/bin/emacs $argv
  else if type -qf emacs-nox
    eval /usr/bin/emacs-nox $argv
  else
    eval /usr/bin/emacs $argv
 end
end
