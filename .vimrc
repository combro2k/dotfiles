filetype plugin indent on
filetype plugin on
syntax on

set laststatus=2

call plug#begin('~/.vim/plugged')

Plug 'powerline/powerline', { 'rtp': 'powerline/bindings/vim' }
Plug 'pearofducks/ansible-vim'
Plug 'kovetskiy/sxhkd-vim'
Plug 'nsf/gocode', { 'rtp': 'vim', 'do': '~/.vim/plugged/gocode/vim/symlink.sh' }
Plug 'mikewest/vim-markdown'

call plug#end()

function! s:tig_status()
  cd `git rev-parse --show-toplevel % | head -n 1`
  !tig status
endfunction

map <C-G> :TigStatus<CR><CR>
command! TigStatus call s:tig_status()

autocmd BufNewFile,BufReadPost *.md set filetype=markdown

colorscheme delek
