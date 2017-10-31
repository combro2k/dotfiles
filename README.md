# dotfiles

## VMWARE config

/etc/lightdm.conf

	[Seat:*]
	...
	display-setup-script=/usr/bin/vmware-user-suid-wrapper
	....


## VIM plugins

	curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
		https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
