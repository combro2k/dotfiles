from libqtile.widget import base, WindowName, TaskList
from libqtile import bar
from os.path import expanduser
from libqtile.log_utils import logger
from classes import Helpers
from subprocess import run

from extensions import RofiMenu

#from extensions import RofiMenu

class MenuWidget(base._TextBox):
    defaults = [
        (
            'program',
            '~/.local/bin/qtile-contextmenu',
            'Location of the program to run on click'
            'e.g. ~/.local/bin/qtile-contextmenu'
        ),
        (
            'icon',
            '\uf314',
            'Icon to use',
            'e.g. "\uf314 "'
        ),
    ]

    def __init__(self, width=bar.CALCULATED, **config):
        base._TextBox.__init__(self, "", width, **config)
        self.add_defaults(MenuWidget.defaults)

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        self.text = self.icon

    def button_press(self, x, y, button):
        if button == 1:
            self.qtile.cmd_spawn([expanduser(self.program)])

class ActionMenuWidget(base._TextBox):
    defaults = [
        (
            'program',
            '~/.local/bin/qtile-actionmenu',
            'Location of the program to run on click'
            'e.g. ~/.local/bin/qtile-actionmenu'
        ),
        (
            'icon',
            '\uf2be',
            'Icon to use',
            'e.g. "\uf2be "'
        ),
    ]

    def __init__(self, width=bar.CALCULATED, **config):
        base._TextBox.__init__(self, "", width, **config)
        self.add_defaults(ActionMenuWidget.defaults)

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        self.text = self.icon

    def button_press(self, x, y, button):
        if button == 1:
            self.qtile.cmd_spawn([expanduser(self.program)])

class WindowNameNew(WindowName):

    _windowcd = None

    def __init__(self, width=bar.STRETCH, **config):
        WindowName.__init__(self, width=width, **config)
        self.add_defaults(WindowName.defaults)

    @property
    def windowcd(self):
        if self._windowcd is None:
            windowcd = RofiMenu(modi='windowcd')
            windowcd._configure(self.qtile)
            self._windowcd = windowcd

        return self._windowcd

    def update(self, *args):
        if self.for_current_screen:
            w = self.qtile.current_screen.group.current_window
        else:
            w = self.bar.screen.group.current_window
        state = ''
        if self.show_state and w is not None:
            if w.maximized:
                state = '\uf2d0 '
            elif w.minimized:
                state = '\uf2d1 '
            elif w.floating:
                state = '\uf2d2 '
        self.text = "%s%s" % (state, w.name if w and w.name else " ")
        self.bar.draw()

    def button_press(self, x, y, button):
        if self.for_current_screen:
            w = self.qtile.current_screen.group.current_window
        else:
            w = self.bar.screen.group.current_window
        if button == 1 and not w is None:
            w.toggle_maximize()
        if button == 2 and not w is None:
            w.toggle_minimize()
        if button == 3:
            # Dirty hack :-(
            self.qtile.cmd_run_extension(self.windowcd)

