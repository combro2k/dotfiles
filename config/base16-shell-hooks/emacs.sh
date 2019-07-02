#!/usr/bin/env bash

cat > ~/.emacs_theme.el <<EOF
(load-theme 'base16-${BASE16_THEME} t)
EOF

echo -e "\e[93mUpdated \e[31m.emacs_theme.el\e[0m"
