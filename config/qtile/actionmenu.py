#! /usr/bin/env python3

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Gtk, Gdk

from libqtile.command import Client

from subprocess import Popen

class ActionMenuWindow(Gtk.ApplicationWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'application' in kwargs:
            self.application = kwargs['application']

        self.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_wmclass('Qtile-ActionMenu', 'qtile-actionmenu')
        self.resize(400, 350)

        self.set_border_width(20)
        self.set_mnemonics_visible(True)
        # window.connect('key-press-event', self._key_press_event)

    def present(self):
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.vbox.pack_start(self.create_button('_Logout', 'system-log-out', self.logout), True, True, 0)
        self.vbox.pack_start(self.create_button('_Restart', 'view-refresh-symbolic', self.restart), True, True, 0)
        self.vbox.pack_start(self.create_button('_Shutdown', 'system-shutdown-symbolic', self.shutdown), True, True, 0)
        self.vbox.pack_start(self.create_button('_Cancel', 'gtk-cancel', self.cancel), True, True, 0)
        self.vbox.show()

        self.add(self.vbox)

        super().present()
      
    """
        GTK3 Create buton helper
    """
    def create_button(self, label=None, icon=None, callback=None):
        btn = Gtk.Button.new_with_mnemonic(label=label)
        btn.show()

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
    def _get_theme_icon(self, icon, size=64):
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
            self.application.qtile.shutdown()
        except Exception as v:
            print(v)

        self.destroy()

    def restart(self, button):
        Popen(['sh', '-c', f'sleep 2 && /usr/bin/systemctl reboot'], shell=False)
        self.destroy()

    def shutdown(self, button):
        Popen(['sh', '-c', f'sleep 2 && /usr/bin/systemctl poweroff'], shell=False)
        self.destroy()

class ActionMenu(Gtk.Application):
    
    _qtile = None

    def __init__(self, qtile=None):
        Gtk.Application.__init__(self, application_id="org.qtile.actionmenu", flags=Gio.ApplicationFlags.FLAGS_NONE)

        if qtile is not None:
            self._qtile = qtile

        self.window = None

    def do_activate(self):
        window = ActionMenuWindow(application=self, title="Main Window")
        window.present()

    @property
    def qtile(self):
        if self._qtile is None:
            self._qtile = Client()

        return self._qtile

if __name__ == '__main__':
    app = ActionMenu()
    app.run(sys.argv)
    print('test')
