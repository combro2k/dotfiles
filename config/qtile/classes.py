
from libqtile.command import lazy

class AutoStart(object):
    commands = []

    def __init__(self, commands):
        self.commands = commands
        self.run()

    def run(self):
        # needed imports for the function
        from libqtile.log_utils import logger
        from subprocess import Popen
        from os import access, X_OK
        from os.path import expanduser

        logger.error('Starting class AutoStart')
        for i in self.commands:
            if i is None:
                continue

            x = expanduser(i if type(i) is str else list(i)[0])

            if not access(x, X_OK):
                logger.error('Does not exist or is not executable: %s' % x)
                continue

            c = [x] if type(i) is str else list(i)

            logger.error('Running Popen with: %s' % c)
            Popen(c, shell=False)

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
    def rofi_drun():
        @lazy.function
        def f(qtile):
            from subprocess import Popen
            Popen(['sh', '-c', 'rofi -theme base16-twilight -demnu -show drun -modi drun'], shell=False)

        return f

    def zenity_question(command, title="Question", text="Are you sure?"):
        @lazy.function
        def f(qtile):
            from subprocess import Popen
            try:
                Popen(['sh', '-c', f'zenity --question --title="{title}" --text="{text}" && {command}'], shell=False)
            except subprocess.CalledProcessError as e:
                logger.error(e)

        return f

    def app_or_group(group, app):
        """ Go to specified group if it exists. Otherwise, run the specified app.
        When used in conjunction with dgroups to auto-assign apps to specific
        groups, this can be used as a way to go to an app if it is already
        running. """
        def f(qtile):
            try:
                qtile.groupMap[group].cmd_toscreen()
            except KeyError:
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