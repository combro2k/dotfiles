function fpass -d "Fuzzy-find a Lastpass entry and copy the password"
  if not test -x /usr/bin/lpass
    echo "Install lastpass CLI"

    return
  end

  if not type -q fzf
    echo "FZF is not found!"

    return
  end

  if not lpass status -q
    if not set -q LP_EMAIL
      read LP_EMAIL -P 'What is the email? ' 
    end

    env LPASS_AGENT_TIMEOUT=28800 lpass login $LP_EMAIL
  end

  if not lpass status -q
    return
  end

  if not test -z "$argv"
    set id $argv 
  else
    set id (lpass ls --sync=now | fzf | string replace -r -a '.+\[id: (\d+)\]' '$1')
  end

  if not test -z "$id"
    ~/bin/lastpass.py "$id"
  end
end
