#!/usr/bin/env bash

cat > ~/.vimrc_background <<EOF
if !exists('g:colors_name') || g:colors_name != 'base16-${BASE16_THEME}'
  colorscheme base16-${BASE16_THEME}
endif
EOF
