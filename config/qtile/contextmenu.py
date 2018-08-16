#! /usr/bin/env python3

import sys
import gi
import time
import subprocess
import shlex
import os.path

import xdg.Menu
import xdg.DesktopEntry

gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Gtk, Gdk

from libqtile.command import Client

class ContextMenuApp(Gtk.Application):
    
    _qtile = None
    _menu = None
    _quit = False
    _submenu = []

    @property
    def qtile(self):
        if self._qtile is None:
            self._qtile = Client()

        return self._qtile

    @property
    def menu(self):
        if self._menu is None:
            menu = Gtk.Menu()
            menu.set_title('ROOT')
            menu.connect('deactivate', self.cmd_destroy)

            self._menu = menu            

        return self._menu

    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.qtile.actionmenu")

    def _configure(self):
        try:
            currentWindow = self.qtile.window.info()
        except:
            currentWindow = None

        self.createXdgMenu(
            menu=xdg.Menu.parse(
                filename=None, 
                debug=False,
            ), 
            submenu=self.addMenu(
                item=self.createMenu(title='Applications'),
                icon='applications-other'
            )
        )
        
        self.addMenuItem(
            item=self.createMenuItemSeparator(),
            parent=self.menu,
        )

        qtileMenu = self.addMenu(
            item=self.createMenu(title='_Qtile'),
            icon='qtile',
            parent=self.menu
        )

        if currentWindow:
            qtileWindowMenu = self.addMenu(
                item=self.createMenu(title='_Window'),
                parent=qtileMenu,
                icon='preferences-system-windows',
            )

            self.addMenuItem(
                item=self.createMenuItem(
                    title='Toggle _Maximize', 
                    callback=self.cmd_qtile,
                    icon='window-maximize-symbolic',
                    key='window',
                    command='toggle_maximize',
                ),
                parent=qtileWindowMenu
            )

            self.addMenuItem(
                item=self.createMenuItem(
                    title='Toggle _Minimize', 
                    callback=self.cmd_qtile,
                    icon='window-minimize-symbolic',
                    key='window',
                    command='toggle_minimize',
                ),
                parent=qtileWindowMenu
            )

            self.addMenuItem(
                item=self.createMenuItem(
                    title='Toggle _Float', 
                    callback=self.cmd_qtile,
                    key='window',
                    command='toggle_floating',
                ),
                parent=qtileWindowMenu
            )

        qtileCommandsMenu = self.addMenu(
            item=self.createMenu(
                title='_Commands',
            ),
            icon='system-run',
            parent=qtileMenu,
        )

        self.addMenuItem(
            item=self.createMenuItem(
                title='_Restart',
                callback=self.cmd_qtile,
                command='restart',
            ),
            parent=qtileCommandsMenu
        )

        self.addMenuItem(
            item=self.createMenuItem(
                title='_Quit',
                callback=self.cmd_qtile,
                command='shutdown',
            ),
            parent=qtileCommandsMenu
        )

        self.addMenuItem(
            item=self.createMenuItemSeparator(),
            parent=self.menu,
        )

        systemMenu = self.addMenu(
            item=self.createMenu(title='_System'),
            icon='system',
            parent=self.menu
        )

        self.addMenuItem(
            item=self.createMenuItem(
                title='_Logout',
                callback=self.cmd_qtile,
                icon='system-log-out',
                command='shutdown',
            ),
            parent=systemMenu
        )

        self.addMenuItem(
            item=self.createMenuItem(
                title='_Restart',
                callback=self.cmd_execute,
                icon='view-refresh',
                command='systemctl reboot',
            ),
            parent=systemMenu
        )

        self.addMenuItem(
            item=self.createMenuItem(
                title='_Shutdown',
                callback=self.cmd_execute,
                icon='system-shutdown-symbolic',
                command='systemctl poweroff',
            ),
            parent=systemMenu
        )


        self.addMenuItem(
            item=self.createMenuItemSeparator(),
            parent=self.menu,
        )

        self.addMenuItem(
            item=self.createMenuItem(
                title='_Close',
                callback=self.cmd_destroy,
            ),
            parent=self.menu
        )

    def createXdgMenu(self, menu, submenu=None):
        groups = []
        entries = []

        for entry in menu.getEntries():
            if isinstance(entry, xdg.Menu.Menu):
                groupsTuple = {
                    'title': entry.getName(),
                }

                if groupsTuple not in groups:
                    newSubmenu = self.createMenu(title=entry.getName())

                    self.addMenu(
                        item=newSubmenu,
                        icon=entry.getIcon(),
                        parent=submenu
                    )

                    entries.extend(
                        self.createXdgMenu(
                            menu=entry, 
                            submenu=newSubmenu,
                        )
                    )

                    groups.append(groupsTuple)

            elif (isinstance(entry, xdg.Menu.MenuEntry)):
                cmd = None
                entryTuple = {
                    'title': entry.DesktopEntry.getName(),
                    'command': entry.DesktopEntry.getExec(),
                    'icon': entry.DesktopEntry.getIcon(),
                }

                if entryTuple not in entries:
                    cmd = entry.DesktopEntry.getExec() \
                        .replace('%U', '', 1) \
                        .replace('%u', '', 1) \
                        .replace('%F', '', 1)

                    item = self.createMenuItem(
                        title=entry.DesktopEntry.getName(),
                        callback=self.cmd_execute,
                        command=cmd,
                        icon=entry.DesktopEntry.getIcon(),
                    )

                    self.addMenuItem(
                        item=item,
                        parent=submenu
                    )

                    entries.append(entryTuple)

        return entries

    def getThemeIcon(self, icon, size=24):           
        icon = Gio.ThemedIcon(name=icon)
        img = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)

        return img

    def createMenu(self, title='', icon=None):
        item = Gtk.Menu()
        item.set_title(title)

        return item # type: gi.overrides.Gtk.Menu

    def createMenuItem(self, title='', callback=None, icon=None, **kwargs):
        if icon:
            item = Gtk.ImageMenuItem.new_with_mnemonic(title)
            item.set_image(self.getThemeIcon(icon))
        else:
            item = Gtk.MenuItem.new_with_mnemonic(title)

        if callback:
            if len(kwargs) > 0:
                item.connect("activate", callback, kwargs)
            else:
                item.connect("activate", callback)

        return item # type: gi.overrides.Gtk.MenuItem

    def createMenuItemSeparator(self, title=''):
        item = Gtk.SeparatorMenuItem()
        item.set_label(title)

        return item

    def addMenuItem(self, item, parent=None):
        if parent is None:
            parent = self.menu

        parent.append(item)

    def addMenu(self, item, icon=None, parent=None):
        if parent is None: 
            parent = self.menu # type: gi.overrides.Gtk.Menu

        menuItem = self.createMenuItem(
            title=item.get_title(),
            icon=icon,
        )

        menuItem.set_submenu(item)

        parent.append(menuItem)

        return item

    def popup(self):
        self.menu.show_all()

        self.menu.popup(
            parent_menu_shell=None,
            parent_menu_item=None,
            func=None,
            data=None,
            button=0,
            activate_time=Gdk.CURRENT_TIME
        )       

    def do_activate(self):
        self._configure()
        self.popup()

        Gtk.main()   

    def cmd_qtile(self, item, kwargs=None):
        if kwargs:
            command = kwargs.get('command', 'commands')
            key = kwargs.get('key', None)
            args = kwargs.get('args', None)
        else:
            command = 'commands'
            key = None
            args = None
        
        if key is not None:
            mod = getattr(self.qtile, key)
        else:
            mod = self.qtile

        try:
            if args is not None:
                ret = getattr(mod, command)(args)
            else:
                ret = getattr(mod, command)()

            if ret is not None:
                print(ret)
        except Exception as e:
            print(e)

    def cmd_execute(self, item, kwargs=None):
        if kwargs:
            command = kwargs.get('command', None)
            shell = kwargs.get('shell', False)
        else:
            command = None
            shell = False

        if command is not None:
            if type(command) is str:
                command = shlex.split(command)  

            command[0] = os.path.expanduser(command[0])
            try:
                subprocess.Popen(command, shell=shell)
            except Exception as e:
                print(e)

        else:
            print('Nothing to run!')

    def cmd_destroy(self, item):
        Gtk.main_quit()

if __name__ == '__main__':
    app = ContextMenuApp()
    app.run(sys.argv)
