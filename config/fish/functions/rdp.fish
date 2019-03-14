function rdp --description 'RDP wrapper'
  if not type -qf xfreerdp
    echo "XFreeRDP is not installed!"

    return 1
  end

  if not set -q argv
    echo "Please provide servername"

    return 0
  end

  xfreerdp /v:$argv /u:Administrator /f +clipboard
end

