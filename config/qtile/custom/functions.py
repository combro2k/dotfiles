# Global Functions

import subprocess
import os

from libqtile.log_utils import logger
from zenipy import question


def cmd_reboot(text):
    def cmd(qtile):
        result = _cmd_zenity_question(text)
        logger.error('Dit is het: %s', result)

    return cmd

#        if _cmd_zenity_question():
#            logger.error('Restarting')
#
#        logger.error('test')
#
#        return False

def _cmd_zenity_question(title='Question', text='Are you sure?'):
    result = os.system("zenity --question --text='%s'" % text)

    if result == 256:
        return False

    return True

def main(self):
    logger.error('Functions initialized...')

    pass

if __name__ == "__main__":
    main()
