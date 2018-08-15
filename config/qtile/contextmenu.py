#! /usr/bin/env python3

import sys
import gi
import time
import subprocess
import shlex
import os.path

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
        
    def _configure(self):
        try:
            currentWindow = self.qtile.window.info()
        except:
            currentWindow = None

        self.add_menu_item(
            callback=self.cmd_execute,
            command='urxvtc-256color',
            label="_URXvt",
            submenu='_Run'
        )

        self.add_menu_separator()

        if currentWindow is not None:
            self.add_menu_item(
                callback=self.cmd_qtile,
                command='toggle_maximize',
                key='window',
                label="_Unmaximize Window" if currentWindow['maximized'] else "_Maximize Window",
                menu=self.get_submenu_item('_Qtile'),
                submenu='_Window'
            )

            self.add_menu_separator(
                submenu='_Qtile',
            )

        self.add_menu_item(
            callback=self.cmd_qtile,
            command='debug',
            label="_Debug",
            submenu='_Qtile'
        )

        self.add_menu_item(
            callback=self.cmd_qtile,
            command='restart',
            label="_Reload",
            submenu='_Qtile'
        )

        self.add_menu_item(
            callback=self.cmd_qtile,
            command='shutdown',
            label="_Quit",
            submenu='_Qtile'
        )

    def popup(self):
        self.add_menu_separator()

        self.add_menu_item(
            callback=self.cmd_destroy,
            label="_Cancel"
        )

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

    def add_submenu_item(self, title, menu=None):
        aMenuitem = Gtk.MenuItem.new_with_mnemonic(title)
        aMenuitem.set_submenu(Gtk.Menu())

        menu = self.menu if menu is None else menu
        menu.append(aMenuitem)

        return aMenuitem

    def get_submenu_item(self, title, menu=None):
        menu = self.menu if menu is None else menu

        for m in self.menu:
            if m.get_label() == title and not m.get_submenu() is None:
                s = m.get_submenu()

                return s
        
        m = self.add_submenu_item(title, menu)
        s = m.get_submenu()

        return s

    def add_menu_separator(self, label='', submenu=None):
        aMenuseparator = Gtk.SeparatorMenuItem()
        aMenuseparator.set_label(label)

        if submenu is not None:
            s = self.get_submenu_item(submenu) # type: Gtk.Menu
            s.append(aMenuseparator)
        else:
            self.menu.append(aMenuseparator)

    def add_menu_item(self, callback=None, label='', submenu=None, menu=None, **kwargs):
        aMenuitem = Gtk.MenuItem.new_with_mnemonic(label)

        if callback is not None:
            if len(kwargs) > 0:
                aMenuitem.connect("activate", callback, kwargs)
            else:
                aMenuitem.connect("activate", callback)

        if submenu is not None:
            s = self.get_submenu_item(submenu, menu) # type: Gtk.Menu
            s.append(aMenuitem)
        else:
            self.menu.append(aMenuitem)

    def get_menu_item(self, menu):
        for m in self.menu.get_children():
            if m.get_label() == menu:
                return m
        
        return None

    def cmd_qtile(self, item, kwargs):
        command = kwargs.get('command', 'info')
        key = kwargs.get('key', None)
        args = kwargs.get('args', None)
        
        if key is not None:
            mod = getattr(self.qtile, key)
        else:
            mod = self.qtile

        try:
            if args is not None:
                getattr(mod, command)(args)
            else:
                getattr(mod, command)()
        except Exception as e:
            print(e)

    def cmd_execute(self, item, kwargs):
        command = kwargs.get('command', None)
        shell = kwargs.get('shell', False)
        args = kwargs.get('args', None)

        if command is not None:
            if type(command) is str:
                command = [os.path.expanduser(command)]
            else:
                command[0] = os.path.expanduser(command[0])
            
            if args is not None:
                subprocess.Popen(command + shlex.split(args), shell=shell)
            else:
                subprocess.Popen(command, shell=shell)

    def cmd_destroy(self, item):
        Gtk.main_quit()

if __name__ == '__main__':
    app = ContextMenuApp()
    app.run(sys.argv)
