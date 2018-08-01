function fish_title
  if set -q HOSTNAME
    set -l HOSTNAME (hostname)
  end

  if [ "$_" = 'fish' ]
    echo "$USER@$HOSTNAME: $PWD"
  else
    echo "$USER@$HOSTNAME: $argv"
  end
end

