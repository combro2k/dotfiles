function cheat-fzf -d "Cheat fzf wrapper"
  if not type -q cheat
    echo "Cheat is not installed, please install cheat from https://github.com/cheat/cheat"

    return 0
  end
  eval (cheat -l | tail -n +2 | fzf | awk -v vars="$argv" '{ print "cheat " $1 " -t " $3, vars }')
end
