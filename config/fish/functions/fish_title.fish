function fish_title
  if [ "$_" = 'fish' ]
    echo "$USER@$HOSTNAME: $PWD"
  else
    echo "$USER@$HOSTNAME: $argv"
  end
end

