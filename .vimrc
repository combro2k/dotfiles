filetype plugin indent on
filetype plugin on
syntax on

set laststatus=2

call plug#begin('~/.vim/plugged')

Plug 'powerline/powerline', { 'rtp': 'powerline/bindings/vim' }
Plug 'pearofducks/ansible-vim'
Plug 'kovetskiy/sxhkd-vim'
Plug 'nsf/gocode', { 'rtp': 'vim', 'do': '~/.vim/plugged/gocode/vim/symlink.sh' }

call plug#end()

colorscheme desert
