function __fpass_completion
  lpass ls -m | string replace -r -a '(.+) \[id: (\d+)\]' '$1' | string match -rv '/$'
end

complete -x -c fpass -f -a '(__fpass_completion)'
