# dotfiles

## DotBot

Configs can be symlinked via [dotbot](https://git.io/dotbot), use ./install to use that. 
In order to automaticly install python libs install the python development package:
python3-devel or python3-dev (depending on OS)

## Hints

#### VMWARE config

To be placed in /etc/lightdm.conf or /etc/xdg/lightdm/lightdm.conf.d/vmware.conf

    [Seat:*]
    ...
    display-setup-script=/usr/bin/vmware-user-suid-wrapper
    ....

### Dependencies

#### Polybar (choice)

**Depracated in favor of qtile**

    # Use zypper repository
    [polybar](https://software.opensuse.org/ymp/home:sysek/openSUSE_Tumbleweed/polybar.ymp?base=openSUSE%3AFactory&query=polybar)

    # Compile on OpenSUSE
    sudo zypper install \
        cmake \
        make \
        gcc \
        gcc-c++ \
        cairo-devel \
        xcb-proto-devel \
        xcb-util-wm-devel \
        xcb-util-devel \
        xcb-util-image-devel \
        xcb-util-cursor-devel \
        xcb-util-renderutil-devel \
        xcb-util-keysyms-devel \
        xcb-util-xrm-devel \
        libcurl-devel \
        libiw-devel
        git clone --recursive https://github.com/jaagr/polybar
        mkdir polybar/build
        cd polybar/build
        cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
        make
        sudo make install

#### Lemonbar (suggested)

**Deprecated in favor of qtile**

    # Download patched xft lemonbar
    [Krypt-n lemonbar](https://github.com/krypt-n/bar)

Download xtitle dependency

    [Xtitle](https://cerberus.site4u.nl/profiles/ticket/BNU-71184-425/conversation)
    git clone https://github.com/baskerville/xtitle.git
    cd xtitle
    make PREFIX=/usr
    sudo make PREFIX=/usr install

Compile on OpenSUSE

    sudo zypper install \
        make \
        libXft-devel
    git clone https://github.com/krypt-n/bar
    cd bar
    make PREFIX=/usr
    sudo make PREFIX=/usr install

#### NeoFetch

    # Use zypper repository
    [neofetch](https://software.opensuse.org/ymp/utilities/openSUSE_Factory/neofetch.ymp?base=openSUSE%3AFactory&query=neofetch)

#### Dunst

I use dunst for notifications, in order to work with it you need to install dunst:

    sudo pacman -S dunst

    sudo zypper install dunst

#### Nerd Font

	git clone https://github.com/ryanoasis/nerd-fonts.git
	cd nerd-font
	./install.sh

#### FZF

	__fzf_install

#### Pipsi

    pip install --user pipsi

#### Qtile Plasma

I'm a favor of qtile plasma layout; You can install it by using one of those methods

    # For current user only
    pip install --user --upgrade https://github.com/combro2k/qtile-plasma/archive/master.zip

    # For globally
    sudo pip install --upgrade https://github.com/combro2k/qtile-plasma/archive/master.zip

#### Other useful stuff

	package-update-indicator
	clipit
	nm-applet
	xautolock
	tickr

#
