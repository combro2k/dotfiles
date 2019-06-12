function ls --description 'List contents of directory'
  if type -qf exa
    set -l opts --classify --modified --reverse

    getopts $argv | while read -l key value
      if [ "$key" = "l" ]
        set -a opts --long --group
      else if [ "$key" = "t" ]
        set -a opts --sort modified
      else if [ "$key" = "r" ]
        #set -a opts --reverse
      else if [ "$key" = "n" ]
        # nothing here :-O 
      else if [ "$key" = "a" ]
        set -a opts --all
      end

      if [ "$key" = "_" ] || [ "$value" != true ]
        set -a opts $value
      end
    end

    command exa $opts
  else
    set -l ls (which ls)
    command $ls --color=auto $argv
  end
end
