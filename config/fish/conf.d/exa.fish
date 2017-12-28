function ls --description 'List contents of directory'
  if type -qf exa
    eval exa $argv
  else
    eval /usr/bin/ls --color=auto $argv
  end
end
