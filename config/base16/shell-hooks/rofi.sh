#!/usr/bin/env bash

rofi_config_dir=$HOME/.config/rofi
rofi_config=$rofi_config_dir/config.rasi

if [ ! -d "$rofi_config_dir" ]; then
  mkdir -p $rofi_config_dir
fi

cat > $rofi_config <<EOF
configuration {
  show-icons: true;
  theme: "base16-$BASE16_THEME";
}
EOF

echo -e "\e[93mUpdated \e[31m.config/rofi/config.rasi\e[0m"
