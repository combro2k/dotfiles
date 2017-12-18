if status --is-interactive
  if test -f /usr/bin/lpass; and not test -z "$LP_EMAIL"
    function fpass -d "Fuzzy-find a Lastpass entry and copy the password"
      if not lpass status -q
        lpass login $LP_EMAIL
      end

      if not lpass status -q
        return 1
      end

      set id (lpass ls | fzf | string replace -r -a '.+\[id: (\d+)\]' '$1')

      if not test -z "$id"
        lpass show "$id"
      end
    end
  end
end
