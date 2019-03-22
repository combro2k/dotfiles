function rdp --description 'RDP wrapper'
  if not type -qf xfreerdp
    echo "XFreeRDP is not installed!"

    return 1
  end

  set -l screen_size (/usr/bin/xrandr | awk '/*/ {print $1}')

  set -l width (echo $screen_size | cut -d 'x' -f1)
  set -l height (echo $screen_size | cut -d 'x' -f2)
  set -l maxheight (expr $height - 29)

  if not set -q argv
    echo "Please provide servername"

    return 0
  end

  xfreerdp /v:$argv /u:Administrator /w:$width /h:$maxheight +clipboard
end

