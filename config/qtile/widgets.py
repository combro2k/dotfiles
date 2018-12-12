from libqtile.widget import base, WindowName, TaskList
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
        self.add_defaults(MenuWidget.defaults)
    
    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        self.text = '\uf314'
    
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
        self.text = '\uf2be'
    
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

    def update(self, *args):
        if self.for_current_screen:
            w = self.qtile.currentScreen.group.currentWindow
        else:
            w = self.bar.screen.group.currentWindow
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

class TaskListNew(TaskList):
    defaults = [
        (
            'txt_minimized',
            '\uFAAF ',
            'Text representation of the minimized window state. '
            'e.g., "_ " or "\U0001F5D5 "'
        ),
        (
            'txt_maximized',
            '\uFAAE ',
            'Text representation of the maximized window state. '
            'e.g., "[] " or "\U0001F5D6 "'
        ),
        (
            'txt_floating',
            'V ',
            'Text representation of the floating window state. '
            'e.g., "V " or "\U0001F5D7 "'
        ),
    ]

    def __init__(self, **config):
        TaskList.__init__(self, **config)
        self.add_defaults(TaskListNew.defaults)

    def button_press(self, x, y, button):
        window = None
        current_win = self.bar.screen.group.currentWindow           
        if button == 1 or button == 2 or button == 3:
            window = self.get_clicked(x, y)

        if window and window is not current_win:
            window.group.focus(window, False)

        if button == 2 and window is not None:
            window.toggle_minimize()
        if button == 3:
            self.qtile.cmd_spawn([expanduser('~/.config/qtile/contextmenu.py')])

