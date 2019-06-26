function emacs --description 'Start emacs'
  if not type -qf emacs; and not type -qf emacs-nox
    echo "Emacs is not installed, install it first!"

    return 1
  end

  if type -qf emacs-nox
    eval /usr/bin/emacs-nox $argv
  else
    eval /usr/bin/emacs $argv
 end
end
