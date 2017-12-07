# dotfiles

## Stow

  Configs can be symlinked via GNU stow

## VMWARE config

/etc/lightdm.conf or /etc/xdg/lightdm/lightdm.conf.d/vmware.conf

	[Seat:*]
	...
	display-setup-script=/usr/bin/vmware-user-suid-wrapper
	....


## VIM plugins

	curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
		https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

## Polybar

	git clone --recursive https://github.com/jaagr/polybar
	mkdir polybar/build
	cd polybar/build
	cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
	make
	sudo make install

## Dunst

I use dunst for notifications, in order to work with it you need to install dunst:

  sudo pacman -S dunst
  
  sudo zypper install dunst

## Nerd Font

	git clone https://github.com/ryanoasis/nerd-fonts.git
	cd nerd-font
	./install.sh

## FZF

	__fzf_install
