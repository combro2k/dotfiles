#! /usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio
from subprocess import Popen

from gi.repository.GdkPixbuf import Pixbuf

from libqtile.command import Client

class ActionMenu(Gtk.Window):

    _qtile = None

    """
        Magic init handler
    """
    def __init__(self):
        Gtk.Window.__init__(self, title="ActionMenu")
        self._configure()
        self.render()

    @property
    def qtile(self):
        if self._qtile is None:
            self._qtile = Client()

        return self._qtile

    """
        Set up the window
    """
    def _configure(self):
        self.set_type_hint(Gdk.WindowTypeHint.DIALOG)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(10)
        
        self.stick()
        self.set_urgency_hint(True)
        self.set_keep_above(True)
        self.set_mnemonics_visible(True)
        self.set_focus_visible(True)

        self.set_wmclass('Qtile-ActionMenu', 'qtile-actionmenu')
        self.resize(300, 60)
        self.connect('key-press-event', self._key_press_event)

    def render(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        vbox.pack_start(self.create_button('_Logout', 'system-log-out', self.logout), False, False, 0)
        vbox.pack_start(self.create_button('_Restart', 'view-refresh-symbolic', self.restart), False, False, 0)
        vbox.pack_start(self.create_button('_Shutdown', 'system-shutdown-symbolic', self.shutdown), False, False, 0)
        vbox.pack_start(self.create_button('_Cancel', 'gtk-cancel', self.cancel), False, False, 0)
        
        self.add(vbox)

    """
        GTK3 Create buton helper
    """
    def create_button(self, label=None, icon=None, callback=None):
        btn = Gtk.Button.new_with_mnemonic(label=label)

        if icon is not None:
            try:
                btn.set_image(self._get_theme_icon(icon))
                btn.set_always_show_image(True)
            except Exception as v:
                print(v)

        if callback is not None:
            btn.connect("clicked", callback)

        return btn

    """
        GTK3 Icon Theme Helper
    """
    def _get_theme_icon(self, icon, size=24):           
        icon = Gio.ThemedIcon(name=icon)
        img = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)

        return img

    """
        Key Press event handler
    """
    def _key_press_event(self, widget, event):
        if Gdk.keyval_name(event.keyval) == 'Escape':
            self.destroy()

    """
        Button callbacks
    """
    def cancel(self, button):
        self.destroy()

    def logout(self, button):
        try:
            self.qtile.shutdown()
        except Exception as v:
            print(v)

        self.destroy()

    def restart(self, button):
        Popen(['sh', '-c', f'sleep 2 && /usr/bin/systemctl reboot'], shell=False)
        self.destroy()

    def shutdown(self, button):
        Popen(['sh', '-c', f'sleep 2 && /usr/bin/systemctl poweroff'], shell=False)
        self.destroy()
        
win = ActionMenu()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
