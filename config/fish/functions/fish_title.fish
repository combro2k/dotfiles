function fish_title
  if test -z $HOSTNAME
    echo " (INIT) "
    set -g HOSTNAME (hostname)
  end

  if [ "$_" = 'fish' ]
    echo "$USER@$HOSTNAME: $PWD"
  else
    echo "$USER@$HOSTNAME: $argv"
  end
end

