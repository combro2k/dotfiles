function ls --description 'List contents of directory'
  if type -qf exa
    set -l opts

    getopts $argv | while read -l key value
      switch $key
        case l true
          set opts $opts --long --group
        case t true
          set opts $opts --sort modified
        case r true
          set opts $opts --reverse
        case n true
          continue
        case a true
          set opts $opts --all
#        case '?' true
#          set opts $opts -$key
#        case '?' '*'
#          set opts $opts -$key $value
#        case '*' true
#          set opts $opts --$key
        case '*' '*'
          set opts $opts $key $value
      end
    end

    eval exa $opts
  else
    set -l ls (which ls)
    eval $ls --color=auto $argv
  end
end
