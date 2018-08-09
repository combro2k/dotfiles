from libqtile.widget import base, WindowName
from libqtile import bar
from os.path import expanduser
from libqtile.log_utils import logger
from classes import Helpers
from subprocess import run

rofi_windowcd = Helpers.rofi_windowcd

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
            self.qtile.cmd_spawn([expanduser('~/.config/mygtkmenu/mygtkmenui'), '--', expanduser('~/.config/mygtkmenu/QtileMenu')])

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

    def button_press(self, x, y, button):
        if self.for_current_screen:
            w = self.qtile.currentScreen.group.currentWindow
        else:
            w = self.bar.screen.group.currentWindow
        if button == 1:
            w.toggle_maximize()
        if button == 2:
            w.toggle_minimize()
        if button == 3:
            run(['sh', '-c', 'rofi -theme base16-twilight -demnu -show windowcd -modi windowcd'], shell=False)
