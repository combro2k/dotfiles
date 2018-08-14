#! /usr/bin/env python3

import sys
import gi
import time

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
            menu.connect('deactivate', self.cmd_destroy)

            self._menu = menu            

        return self._menu

    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.qtile.actionmenu")
        
    def do_activate(self):
        self.add_menu_item(
            command=self.cmd_qtile_maximize,
            title="_Unmaximize Window" if self.qtile.window.info()['maximized'] else "_Maximize Window",
            submenu='_Qtile'
        )

        self.add_menu_item(
            command=self.cmd_qtile,
            command_args='debug',
            title="_Debug",
            submenu='_Qtile'
        )

        self.add_menu_item(
            command=self.cmd_qtile_restart,
            title="_Reload",
            submenu='_Qtile'
        )

        self.add_menu_item(
            command=self.cmd_qtile_shutdown,
            title="_Quit",
            submenu='_Qtile'
        )

        self.add_menu_item(
            command=self.cmd_destroy,
            title="Quit"
        )

        # self.window.hide()
        self.menu.popup(
            parent_menu_shell=None,
            parent_menu_item=None,
            func=None,
            data=None,
            button=0,
            activate_time=Gdk.CURRENT_TIME
        )

        Gtk.main()

    def add_submenu_item(self, title):
        aMenuitem = Gtk.MenuItem.new_with_mnemonic(title)
        aMenuitem.set_submenu(Gtk.Menu())

        self.menu.append(aMenuitem)

        return aMenuitem

    def get_submenu_item(self, title):
        for m in self.menu:
            if m.get_label() == title and not m.get_submenu() is None:
                s = m.get_submenu()

                return s
        
        m = self.add_submenu_item(title)
        s = m.get_submenu()

        return s

    def add_menu_item(self, command=None, command_args=None, title='', submenu=None):
        aMenuitem = Gtk.MenuItem.new_with_mnemonic(title)

        if not command is None:
            if not command_args is None:
                aMenuitem.connect("activate", command, command_args)
            else:
                aMenuitem.connect("activate", command)

        if not submenu is None:
            s = self.get_submenu_item(submenu) # type: Gtk.MenuItem
            s.append(aMenuitem)
        else:
            self.menu.append(aMenuitem)

        self.menu.show_all()

    def get_menu_item(self, menu):
        for m in self.menu.get_children():
            if m.get_label() == menu:
                return m
        
        return None

    def cmd_qtile(self, item, *args, **kwargs):
#        with self.qtile:
#            args()
        print(args, kwargs)

    def cmd_destroy(self, item):
        Gtk.main_quit()

    def cmd_qtile_restart(self, item):
        try:
            self.qtile.restart()
        except Exception:
            pass

    def cmd_qtile_shutdown(self, item):
        try:
            self.qtile.shutdown()
        except Exception:
            pass

    def cmd_qtile_debug(self, item):
        print(self.qtile.commands())

    def cmd_qtile_maximize(self, item):
        try:
            self.qtile.window.toggle_maximize()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = ContextMenuApp()
    app.run(sys.argv)
