import platform

from subprocess import run, Popen, PIPE
from time import time

from os import devnull, access, X_OK, makedirs, remove
from os.path import expanduser, isdir

from libqtile.command import lazy
from libqtile.log_utils import logger

from threading import Thread, Event

class AutoStart(object):
    commands = []

    def __init__(self):
        self.run()

    def load_commands(self):
        from defines import autostart as load
        self.commands = load()

    def check_running(self, cmd):
        try:
            r = run(['pgrep', '-f', '-l', '-a', ' '.join(cmd)])
            if r.returncode == 1:
                logger.info(f'Process {cmd} is not started!')

                return False
        except Exception as e:
            logger.error(e)

            return False

        return True

    def thread_run(self, *cmd):
        logger.info(f'Starting {cmd}')

        try:
            Popen(cmd, shell=False)
        except Exception as e:
            logger.error(e)

    def run(self):
        self.load_commands()
        for i in self.commands:
            if i is None:
                continue

            x = expanduser(i if type(i) is str else list(i)[0])
            c = [x] if type(i) is str else list(i)

            if not access(x, X_OK):
                logger.error(f'{x} does not exist or is not executable!')
                continue

            if not self.check_running(c):
                logger.info(f'{c} Starting thread...')

                try:
                    Thread(target=self.thread_run, args=(c)).start()
                    # Popen(c, shell=False)
                except Exception as e:
                    logger.error(e)

class Wallpaper(Thread):
    def __init__(self):
        pass

class Colors(object):
    bg = '666666'
    highlight_bg = '888888'
    urgent_bg = 'fe8964'
    text = 'ffffff'
    inactive_text = '333333'
    border = '333333'
    border_focus = urgent_bg
    highlight_text = urgent_bg

class Helpers():
    def app_or_group(group, app):
        """ Go to specified group if it exists. Otherwise, run the specified app.
        When used in conjunction with dgroups to auto-assign apps to specific
        groups, this can be used as a way to go to an app if it is already
        running. """
        @lazy.function
        def f(qtile):
            if group in qtile.groupMap:
                qtile.groupMap[group].cmd_toscreen()
            else:
                if group == 'Editors' and app == 'emacs-nox':
                    qtile.cmd_spawn(app)
                else:
                    qtile.cmd_spawn(app)

        return f

    def window_to_prev_group():
        @lazy.function
        def f(qtile):
            if qtile.currentWindow is not None:
                index = qtile.groups.index(qtile.currentGroup)
                newgroup = qtile.groups[index - 1].name if index > 0 else qtile.groups[len(qtile.groups) - 2].name

                qtile.currentWindow.togroup(newgroup)
                qtile.groupMap[newgroup].cmd_toscreen()

        return f

    def window_to_next_group():
        @lazy.function
        def f(qtile):
            if qtile.currentWindow is not None:
                index = qtile.groups.index(qtile.currentGroup)
                newgroup = qtile.groups[index + 1].name if index < len(qtile.groups) - 2 else qtile.groups[0].name

                qtile.currentWindow.togroup(newgroup)
                qtile.groupMap[newgroup].cmd_toscreen()

        return f

    def window_to_group(newgroup):
        @lazy.function
        def f(qtile):
            if qtile.currentWindow is not None:
                qtile.currentWindow.togroup(newgroup)
                qtile.groupMap[newgroup].cmd_toscreen()

        return f

    def windows_to_prev_group():
        @lazy.function
        def f(qtile):
            if qtile.currentGroup.windows is not None:
                index = qtile.groups.index(qtile.currentGroup)
                newgroup = qtile.groups[index - 1].name if index > 0 else qtile.groups[len(qtile.groups) - 2].name

                windows = qtile.currentGroup.windows.copy()
                for w in windows:
                    w.togroup(newgroup)

                qtile.groupMap[newgroup].cmd_toscreen()

        return f

    def windows_to_next_group():
        @lazy.function
        def f(qtile):
           if qtile.currentGroup.windows is not None:
                index = qtile.groups.index(qtile.currentGroup)
                newgroup = qtile.groups[index + 1].name if index < len(qtile.groups) - 2 else qtile.groups[0].name

                windows = qtile.currentGroup.windows.copy()
                for w in windows:
                    w.togroup(newgroup)

                qtile.groupMap[newgroup].cmd_toscreen()

        return f

    def windows_to_group(newgroup):
        @lazy.function
        def f(qtile):
            if qtile.currentGroup.windows is not None:
                windows = qtile.currentGroup.windows.copy()
                for w in windows:
                    w.togroup(newgroup)

                qtile.groupMap[newgroup].cmd_toscreen()

        return f

    def context_menu():
        @lazy.function
        def f(qtile):
            qtile.cmd_spawn([expanduser('~/.config/qtile/contextmenu.py')])

        return f

    def window_maximize():
        @lazy.function
        def f(qtile):
            if qtile.currentLayout.name == 'max':
                return

            qtile.currentWindow.toggle_maximize()

        return f

    def create_screenshot(mode=False, clipboard=False):
        @lazy.function
        def f(qtile):
            targetdir = expanduser('~/Pictures/Screenshots/')

            if not isdir(targetdir):
                try:
                    makedirs(targetdir)
                except OSError:
                    if not isdir(targetdir):
                        raise

            hostname = platform.node()
            cmd = ['maim']
            opts = []

            if mode == 'window':
                target = f'{targetdir}/{hostname}_window_{str(int(time() * 100))}.png'
                _id = qtile.currentWindow.cmd_info()['id']
                opts.extend(['-i', f'{_id}'])
            elif mode == 'select':
                target = f'{targetdir}/{hostname}_select_{str(int(time() * 100))}.png'
                opts.append('-s')
            else:
                target = f'{targetdir}/{hostname}_full_{str(int(time() * 100))}.png'

            cmd.extend(opts)
            cmd.append(target)

            r = run(cmd)

            if clipboard:
                logger.error('Copying to clipboard!')
                if r.returncode == 0:
                    f = open(target, 'rb')
                    x = run(['xclip', '-selection', 'c', '-t', 'image/png'], input=f.read())
                    remove(target)
                else:
                    logger.error(f'Strange thing happend! {r}')

        return f

    def minimize_group():
        @lazy.function
        def f(qtile):
            for w in qtile.currentGroup.windows:
                w.minimized = True

        return f

    def unminimize_group():
        @lazy.function
        def f(qtile):
            for w in qtile.currentGroup.windows:
                w.minimized = False

        return f

    def toggle_follow_mouse_focus():
        @lazy.function
        def f(qtile):
            qtile.config.follow_mouse_focus = not qtile.config.follow_mouse_focus

        return f

    def qtile_shutdown():
        @lazy.function
        def f(qtile):
            try:
                qtile.shutdown()
            except Exception as e:
                pass

        return f
