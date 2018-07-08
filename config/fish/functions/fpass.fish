function fpass -d "Fuzzy-find a Lastpass entry and copy the password"
  if not test -x /usr/bin/lpass
    echo "Install lastpass CLI"

    return
  end

  if not set -q LP_EMAIL
    echo "LP_EMAIL is not set"

    return
  end

  if not type -q fzf
    echo "FZF is not found!"

    return
  end

  if not lpass status -q
    lpass login $LP_EMAIL
  end

  if not lpass status -q
    return
  end

  set id (lpass ls | fzf | string replace -r -a '.+\[id: (\d+)\]' '$1')

  if not test -z "$id"
    lpass show "$id"
  end
end
