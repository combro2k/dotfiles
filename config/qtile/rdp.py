#!/usr/bin/env python3

import sys, gi, socket, os

gi.require_version('Gtk', '3.0')

from gi.repository import Gio, Gtk, Gdk
from libqtile.command import Client
from subprocess import Popen
from os.path import expanduser

class RDPWindow(Gtk.ApplicationWindow):

    _history_file = expanduser('~/.rdp_history')
    qtile = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'application' in kwargs:
            self.application = kwargs['application']
            self.qtile = self.application.qtile

        self.set_role('qtile-rdp')
        self.set_type_hint(Gdk.WindowTypeHint.TOOLBAR)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_accept_focus(True)
        self.stick()
        self.resize(600, 150)

        self.set_border_width(20)
        self.set_mnemonics_visible(True)

        self.connect('key-press-event', self._key_press_event)

    def _key_press_event(self, widget, event):
        if isinstance(widget, RDPWindow) and Gdk.keyval_name(event.keyval) == 'Escape':
            self.destroy()

        if isinstance(widget, Gtk.Entry) and Gdk.keyval_name(event.keyval) == 'Return':
            self.cmd_connect(widget)

        return False

#    def _history_update(self, widget, event):
#        print(widget, widget.prop.popup_shown)

    def present(self):
        qscreen = self.qtile.screen
        qinfo = qscreen.info()
        qbar = qscreen.bar['top'].info()

        self.width = qinfo['width']
        self.height = qinfo['height'] - qbar['size']

        host_entries = Gtk.ListStore(str)
        for i in self.history:
            if i not in host_entries:
                host_entries.append([i])

        completion = Gtk.EntryCompletion(
            model=host_entries,
        )
        completion.set_text_column(0)

        self.host = Gtk.ComboBox(
            visible=True,
            has_entry=True,
            model=host_entries,
            entry_text_column=0,
        )

        self.host.get_child().set_completion(completion)
        self.host.get_child().set_placeholder_text('Hostname')

        self.username = Gtk.Entry(
            visible=True,
            placeholder_text='Administrator',
        )
        self.password = Gtk.Entry(
            visible=True,
            placeholder_text='Password',
            visibility=False,
        )
        self.btn_connect = Gtk.Button(
            visible=True,
            label='_Connect',
            use_underline=True,
        )
        self.fullscreen = Gtk.CheckButton(
            visible=True,
            label='_Fullscreen',
            use_underline=True,
        )
        self.password_reveal = Gtk.CheckButton(
            visible=True,
            label='_Reveal',
            use_underline=True,
        )

        self.btn_connect.connect("clicked", self.cmd_connect)
        self.host.connect('key-press-event', self._key_press_event)
#        self.host.connect('popup', self._history_update)
        self.username.connect('key-press-event', self._key_press_event)
        self.password.connect('key-press-event', self._key_press_event)
        self.password_reveal.connect("clicked", self.cmd_password_reveal)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        hbox0 = Gtk.Box(spacing=10, visible=True)
        hbox1 = Gtk.Box(spacing=10, visible=True)
        hbox2 = Gtk.Box(spacing=10, visible=True)
        hbox3 = Gtk.Box(spacing=10, visible=True)
        hbox4 = Gtk.Box(spacing=10, visible=True)

        hbox0.pack_start(Gtk.Label(
            visible=True,
            label='_Hostname:',
            mnemonic_widget=self.host,
            use_underline=True,
            xalign=0,
        ), True, True, 0)

        hbox1.pack_start(self.host, True, True, 0)

        hbox2.pack_start(Gtk.Label(
            visible=True,
            label='_Username:',
            mnemonic_widget=self.username,
            use_underline=True,
            xalign=0,
        ), True, True, 0)
        hbox2.pack_start(Gtk.Label(
            label='_Password:',
            mnemonic_widget=self.password,
            use_underline=True,
            visible=True,
            xalign=0,
        ), True, True, 0)

        hbox3.pack_start(self.username, True, True, 0)
        hbox3.pack_start(self.password, True, True, 0)
        hbox3.pack_start(self.password_reveal, True, True, 0)

        hbox4.pack_start(self.fullscreen, True, True, 0)

        vbox.pack_start(hbox0, True, True, 0)
        vbox.pack_start(hbox1, True, True, 0)
        vbox.pack_start(hbox2, True, True, 0)
        vbox.pack_start(hbox3, True, True, 0)
        vbox.pack_start(hbox4, True, True, 0)

        vbox.pack_start(self.btn_connect, True, True, 0)

        vbox.show()

        self.add(vbox)

        self.host.grab_focus()

        super().present()

        self.set_focus(self.host)

    def cmd_connect(self, button):
        try:
            host = self.host.get_child().get_text()

            socket.gethostbyname(host)

            self.add_history(host) 

            username = self.username.get_text() or 'Administrator'
            password = self.password.get_text()

            if not (host and username and password):
                return False

            if self.fullscreen.get_active():
                cmd = f'/usr/bin/xfreerdp /cert-ignore /v:%s /f /u:%s /p:%s /drive:home,%s +clipboard' % (
                        host,
                        username,
                        password,
                        expanduser('~'),
                )
            else:
                cmd = f'/usr/bin/xfreerdp /cert-ignore /v:%s /w:%s /h:%s /u:%s /p:%s /drive:home,%s +clipboard' % (
                        host,
                        self.width,
                        self.height,
                        username,
                        password,
                        expanduser('~'),
                )

            self.hide()

            try:
                print(cmd)
                Popen(['sh', '-c', cmd], shell=False)

                self.destroy()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

    def cmd_password_reveal(self, button):
        self.password.set_visibility(button.get_active())

    @property
    def history(self):
        history = []

        if not os.path.exists(self._history_file):
            return history

        with open(self._history_file, 'r') as f:
            for l in sorted(f.read().splitlines()):
                if l not in history:
                    history.append(l)

        return history

    def add_history(self, value):
        history = self.history

        if not value in history:
            history.append(value)
            history = sorted(history)

            with open(self._history_file, 'w') as f:
                for l in history:
                    f.write('%s\n' % (l))

            #f.write('%s\n' % (value))

class RDP(Gtk.Application):
    _qtile = None

    def __init__(self, qtile=None):
        Gtk.Application.__init__(self,
            application_id="org.qtile.rdp",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
        )

        if qtile is not None:
            self._qtile = qtile

        self.window = None

    def do_activate(self):
        window = RDPWindow(application=self, title="Qtile RDP")
        window.present()

    @property
    def qtile(self):
        if self._qtile is None:
            self._qtile = Client()

        return self._qtile

if __name__ == '__main__':
    app = RDP()
    app.run(sys.argv)
