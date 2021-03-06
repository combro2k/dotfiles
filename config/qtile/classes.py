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
        logger.warning(f'Starting {cmd}')

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
        """ Fix ~ references in commands """
        app = expanduser(app)

        """ Go to specified group if it exists. Otherwise, run the specified app.
        When used in conjunction with dgroups to auto-assign apps to specific
        groups, this can be used as a way to go to an app if it is already
        running. """
        @lazy.function
        def f(qtile):
            if group in qtile.groups_map:
                logger.error(group)
                qtile.groups_map[group].cmd_toscreen()
            else:
                logger.error('SPAWN {0}'.format(app))
                qtile.cmd_spawn(app)

        return f

    def window_to_prev_group():
        @lazy.function
        def f(qtile):
            if qtile.current_window is not None:
                newgroup = qtile.current_group.get_previous_group()

                qtile.current_window.togroup(newgroup.name)
                newgroup.cmd_toscreen()

        return f

    def window_to_next_group():
        @lazy.function
        def f(qtile):
            if qtile.current_window is not None:
                newgroup = qtile.current_group.get_next_group()

                qtile.current_window.togroup(newgroup.name)
                newgroup.cmd_toscreen()

        return f

    def window_to_group(newgroup):
        @lazy.function
        def f(qtile):
            if qtile.current_window is not None:
                qtile.current_window.togroup(newgroup)
                qtile.groups_map[newgroup].cmd_toscreen()

        return f

    def windows_to_prev_group():
        @lazy.function
        def f(qtile):
            if qtile.current_group.windows is not None:
                newgroup = qtile.current_group.get_previous_group()

                for w in qtile.current_group.windows.copy():
                    w.togroup(newgroup.name)

                newgroup.cmd_toscreen()

        return f

    def windows_to_next_group():
        @lazy.function
        def f(qtile):
           if qtile.current_group.windows is not None:
                newgroup = qtile.current_group.get_next_group()

                for w in qtile.current_group.windows.copy():
                    w.togroup(newgroup.name)

                newgroup.cmd_toscreen()

        return f

    def windows_to_group(newgroup):
        @lazy.function
        def f(qtile):
            if qtile.current_group.windows is not None:
                for w in qtile.current_group.windows.copy():
                    w.togroup(newgroup)

                qtile.groups_map[newgroup].cmd_toscreen()

        return f

    def context_menu():
        @lazy.function
        def f(qtile):
            qtile.cmd_spawn([expanduser('~/.local/bin/qtile-contextmenu')])

        return f

    def window_maximize():
        @lazy.function
        def f(qtile):
            if qtile.current_layout.name == 'max':
                return

            qtile.current_window.toggle_maximize()

        return f

    def create_video(mode=False):
        @lazy.function
        def f(qtile):
            def check_running():
                r = run(['pgrep', '-fla', 'byzanz-record'])
                logger.error(r)

                return False if r.returncode == 1 else True

            def thread_run(*cmd):
                r = run(cmd)
                logger.error(r)

                return True

            targetdir = expanduser('~/Pictures/Screenshots/')

            if not isdir(targetdir):
                try:
                    makedirs(targetdir)
                except OSError:
                    if not isdir(targetdir):
                        raise

            hostname = platform.node()
            cmd = ['byzanz-record', '-c', '--duration=3600']
            opts = []

            if mode == 'window':
                qinfo = qtile.current_window.cmd_info()

                opts.extend([
                    '-x', str(qinfo['x']),
                    '-y', str(qinfo['y']),
                    '-w', str(qinfo['width'] + 2),
                    '-h', str(qinfo['height'] + 2),
                ])
                target = f'{targetdir}/{hostname}_window_{str(int(time() * 100))}.gif'
            else:
                target = f'{targetdir}/{hostname}_full_{str(int(time() * 100))}.gif'

            cmd.extend(opts)
            cmd.append(target)

            logger.error(opts)
            logger.error(cmd)

            if not check_running():
                Thread(target=thread_run, args=(cmd)).start()
            else:
                r = run(['pkill', 'byzanz-record'])
                logger.error(r)

        return f

    def create_screenshot(mode=False, clipboard=True):
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
                _id = qtile.current_window.cmd_info()['id']
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

    def toggle_minimize_group():
        @lazy.function
        def f(qtile):
            state = not qtile.current_window.minimized
            if qtile.current_group.windows is not None:
                for w in qtile.current_group.windows:
                    w.minimized = state
        return f

    def minimize_group():
        @lazy.function
        def f(qtile):
            for w in qtile.current_group.windows:
                w.minimized = True

        return f

    def unminimize_group():
        @lazy.function
        def f(qtile):
            for w in qtile.current_group.windows:
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

    def move_window_to_left():
        @lazy.function
        def f(qtile):
            currentLayout = qtile.currentLayout
            if qtile.current_window is not None:
                if currentLayout.name == 'plasma':
                    currentLayout.cmd_move_left()
                elif currentLayout.name == 'bsp':
                    currentLayout.cmd_shuffle_left()
                elif currentLayout.name == 'stack':
                    currentLayout.cmd_shuffle_left()

        return f

    def move_window_to_right():
        @lazy.function
        def f(qtile):
            pass

        return f

    def move_window_to_up():
        @lazy.function
        def f(qtile):
            pass

        return f

    def move_window_to_down():
        @lazy.function
        def f(qtile):
            pass

        return f

    def get_num_screen():
        num = 1

        try:
            r = run(['sh', '-c', '/usr/bin/xrandr --listactivemonitors | head -n1 | tr -dc \'0-9\''], stdout=PIPE, universal_newlines=True)

            num = r.stdout.strip()

        except Exception as e:
            logger.error(e)

        return num

    def get_screen_size():
        try:
            r = run(['sh', '-c', '/usr/bin/xrandr | awk \'/\*/ {print $1}\''], stdout=PIPE, universal_newlines=True)

            s = r.stdout.lstrip().split('x', 2)
            w = s[0]
            h = s[1]

            return {
                'width': int(w),
                'height': int(h),
            }
        except Exception as e:
            logger.error(e)

        return {
            'width': 0,
            'height': 0,
        }

    def get_type_screen():
        det = 'SD'

        dim = Helpers.get_screen_size()

        if dim['height'] >= 720:
            det = 'HD'

        if dim['height'] >= 900:
            det = 'HD+'

        if dim['height'] >= 1050:
            det = 'WSXGA+'

        if dim['height'] >= 1080:
            det = 'FHD'

        if dim['height'] >= 1971:
            det = '4K VMware'

        if dim['height'] >= 2160:
            det = '4K UHD'

        logger.error('Detected ~ resolution: %s' % det)

        return det
