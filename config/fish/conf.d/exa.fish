function ls --description 'List contents of directory'
  if type -qf exa
    eval exa $argv
  else
    set -l ls (which ls)
    eval $ls --color=auto $argv
  end
end
