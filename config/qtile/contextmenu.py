#! /usr/bin/env python3

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Gtk, Gdk

from libqtile.command import Client

class ContextMenuApp(Gtk.Application):
    
    # _qtile = None

    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.qtile.actionmenu")
        # self.connect('notify::application-id', self.show_popup)
        self.menu = None
        self.window = None
        self._tile = None

        # self.connect('destroy', self.do_destroy)

    def show_popup(self, event):
        print(args)
        print(kwargs)

    def do_quit(self, event):
        print('event')
        self.window.destroy()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        self.window = Gtk.ApplicationWindow(application=self)
        self.menu = Gtk.Menu()
        self.menu.connect('delete-event', self.do_quit)

        self.add_menu_item(self.do_quit, "Quit")
        # self.menu.connect('destroy', self.do_quit)

        # self.window = Gtk.ApplicationWindow(application=self)
        self.window.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.window.set_position(Gtk.WindowPosition.CENTER)

        # self.window.set_wmclass('Qtile-ActionMenu', 'qtile-actionmenu')

    def do_activate(self):
        Gtk.Application.do_activate(self)

        # self.menu.present()

        # # self.window.show()
        self.menu.popup(
            parent_menu_shell=None,
            parent_menu_item=None,
            func=None,
            data=None,
            button=0,
            activate_time=Gdk.CURRENT_TIME
        )

        
        # self.window.add(self.menu)

    def do_destroy(self):
        pass

    def add_menu_item(self, command, title):
        aMenuitem = Gtk.MenuItem()
        aMenuitem.set_label(title)
        aMenuitem.connect("activate", command)

        self.menu.append(aMenuitem)

        self.menu.show_all()

        # self.window.destroy()

    @property
    def qtile(self):
        if self._qtile is None:
            self._qtile = Client()

        return self._qtile

if __name__ == '__main__':
    app = ContextMenuApp()
    app.run(sys.argv)