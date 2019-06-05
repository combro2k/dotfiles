function ls --description 'List contents of directory'
  if type -qf exa
    switch "$argv"
      case '-altrn'
        set argv "--all --long --sort modified"
      case '-al'
        set argv "--all --long --sort name"
      case '-alt'
        set argv "--all --long --reverse --sort modified"
    end

    eval exa $argv
  else
    set -l ls (which ls)
    eval $ls --color=auto $argv
  end
end
