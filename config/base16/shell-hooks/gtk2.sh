#!/usr/bin/env bash

gtk2_source_dir=$HOME/.config/base16-gtk2/schemes
gtk2_theme=$gtk2_source_dir/base16-$BASE16_THEME.gtkrc

if [ -f $gtk2_theme ]; then
  ln -fs $gtk2_theme $HOME/.gtkrc

  echo -e "\e[93mUpdated \e[31m.gtkrc\e[0m"
fi
