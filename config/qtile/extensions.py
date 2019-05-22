import six
import shlex
import subprocess
import sys
import time

from libqtile.extension.base import RunCommand, _Extension
from libqtile.log_utils import logger
from libqtile.command import _Call
from libqtile import window, xcbq

from threading import Thread

from os.path import expanduser

class RofiMenu(RunCommand):
    defaults = [
        ("rofi_command", "rofi", "the command to be launched (string or list with arguments)"),
        ("modi", "combi", "the mode you want to show"),
        ("theme", "base16-twilight", "theme"),
        ("font", "SauceCodePro Nerd Font Mono", "Use other font"),
        ("fontsize", 12, "Fontsize"),
        ("dmenu", False, "enable DMenu's replacement mode"),
    ]

    def __init__(self, **config):
        RunCommand.__init__(self, **config)
        self.add_defaults(RofiMenu.defaults)

    def _configure(self, qtile):
        RunCommand._configure(self, qtile)

        rofi_command = self.rofi_command or self.command
        if isinstance(rofi_command, str):
            self.configured_command = shlex.split(rofi_command)
        else:
            # Create a clone of dmenu_command, don't use it directly since
            # it's shared among all the instances of this class
            self.configured_command = list(rofi_command)

        if self.dmenu:
            self.configured_command.append("-dmenu")

        if self.theme:
            self.configured_command.extend(("-theme", self.theme))

        if self.modi:
            self.configured_command.extend(("-modi", self.modi))

        if self.font:
            self.configured_command.extend(("-font", "%s %s" % (self.font, self.fontsize)))

        self.configured_command.append("-show")

    def run(self):
        subprocess.run(self.configured_command, shell=False)

class Zenipy(RunCommand):

    defaults = [
        ("zenipy_command", "~/.config/qtile/zenipy.py", "the command to be launched (string or list with arguments)"),
        ("type", "question", "the type of dialog"),
        ("title", None, "The title of the dialog"),
        ("text", None, "The text of the dialog"),
        ("exec", None, "Run after exit code 0")
    ]

    def __init__(self, **config):
        RunCommand.__init__(self, **config)
        self.add_defaults(Zenipy.defaults)

    def _configure(self, qtile):
        RunCommand._configure(self, qtile)

        zenipy_command = self.zenipy_command or self.command
        if isinstance(zenipy_command, str):
            self.configured_command = shlex.split(expanduser(zenipy_command))
        else:
            # Create a clone of dmenu_command, don't use it directly since
            # it's shared among all the instances of this class
            self.configured_command = list(zenipy_command)

        if self.type == "question":
            self.configured_command.append("--question")

        elif self.type == "warning":
            self.configured_command.append("--warning")

        elif self.type == "notification":
            self.configured_command.append("--notification")
        else:
            raise NotImplementedError()

        if self.text:
            self.configured_command.extend(["--text", self.text])

        if self.title:
            self.configured_command.extend(["--title", self.title])

        self.configured_command = ["sh", "-c", ' '.join(self.configured_command)]

    def run(self):
        def worker():
            try:
                x = subprocess.run(self.configured_command, stdout=subprocess.PIPE, shell=False)
                logger.error(x)
            except Exception as e:
                logger.error(x)

            if x.returncode == 0:
                clb = self.exec

                if clb:
                    if isinstance(clb, _Call) and clb.check(self.qtile):
                        logger.error(clb)

                        obj = self.qtile
                        funcname = 'cmd_' + clb.name
                        args = clb.args

                        for s in clb.selectors:
                            try:
                                obj = obj[s]
                            except KeyError:
                                obj = getattr(obj, s)
                            except AttributeError:
                                log.error("Specified object does not exist " + " ".join(sel))

                                return False
                        try:
                            func = getattr(obj, funcname)
                        except AttributeError:
                            log.error("error: Sorry no function " + funcname)

                            return False

                        func(*args)

                    elif isinstance(clb, list):
                        x = subprocess.run(clb, shell=False)
                    elif isinstance(clb, str):
                        clb = shlex.split(clb)
                        x = subprocess.run(cbl)
        try:
            Thread(target=worker).start()
        except Exception as e:
            logger.error(e)

class Wallpaper(_Extension):

    defaults = [
        ("directory", "~/.config/backgrounds", "the command to be launched (string or list with arguments)"),
    ]

    def __init__(self, **config):
        _Extension.__init__(self, **config)
        self.add_defaults(Wallpaper.defaults)

    def run(self):
        logger.error('Setting wallpaper')
        #x = subprocess.run(['feh', '-r', '-z', '--bg-scale', '-Z', expanduser(self.directory)])
