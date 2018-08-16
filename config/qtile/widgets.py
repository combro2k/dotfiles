from libqtile.widget import base, WindowName
from libqtile import bar
from os.path import expanduser
from libqtile.log_utils import logger
from classes import Helpers
from subprocess import run

from extensions import RofiMenu

#from extensions import RofiMenu

class MenuWidget(base._TextBox):
    defaults = []

    def __init__(self, width=bar.CALCULATED, **config):
        base._TextBox.__init__(self, "", width, **config)
        self.add_defaults(ActionMenuWidget.defaults)
    
    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        self.text = '\uf0c9'
    
    def button_press(self, x, y, button):
        if button == 1:
            self.qtile.cmd_spawn([expanduser('~/.config/qtile/contextmenu.py')])

class ActionMenuWidget(base._TextBox):
    defaults = []

    def __init__(self, width=bar.CALCULATED, **config):
        base._TextBox.__init__(self, "", width, **config)
        self.add_defaults(ActionMenuWidget.defaults)
    
    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        self.text = '\uf013'
    
    def button_press(self, x, y, button):
        if button == 1:
            self.qtile.cmd_spawn([expanduser('~/.config/qtile/actionmenu.py')])

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

    def button_press(self, x, y, button):
        if self.for_current_screen:
            w = self.qtile.currentScreen.group.currentWindow
        else:
            w = self.bar.screen.group.currentWindow           
        if button == 1 and not w is None:
            w.toggle_maximize()
        if button == 2 and not w is None:
            w.toggle_minimize()
        if button == 3:
            # Dirty hack :-(
            self.qtile.cmd_run_extension(self.windowcd)
