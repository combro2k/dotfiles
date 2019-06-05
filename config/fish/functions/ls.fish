function ls --description 'List contents of directory'
  if type -qf exa
    if set -q argv; and [ "$argv" = '-altrn' ]
      set argv "-balgsold"
     end

    eval exa $argv
  else
    set -l ls (which ls)
    eval $ls --color=auto $argv
  end
end
