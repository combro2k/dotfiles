function emacs --description 'Star emacs'
  if type -qf emacs-nox
    eval /usr/bin/emacs-nox $argv
  else
    /usr/bin/emacs $argv
  end
end
