if status --is-interactive
  function fssh -d "Fuzzy-find ssh host and ssh into it"
    if test -f ~/.ssh/config
      ssh (ag '^host [^*]' ~/.ssh/config | cut -d ' ' -f 2 | fzf)
    else
      echo "There is no config found in ~/.ssh/config"
      return 1
    end
  end
end
