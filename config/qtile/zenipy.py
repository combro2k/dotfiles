#!/usr/bin/env python3

from __future__ import absolute_import

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import argparse, importlib, sys, imp

#from root.zenipy import error, question, message

class Application(object):
    args = {}
    exitcode = 0
    _zenipy = None

    @property
    def zenipy(self):
        if self._zenipy is None:
            try:
                f, pn, dsc = imp.find_module('zenipy', sys.path[1:])
                zp = imp.load_module('zenipy', f, pn, dsc)
                self._zenipy = zp
            except ImportError:
                print("Can't find zenipy module, is it installed?")
                sys.exit(1)
            
        return self._zenipy

    def __init__(self):
        parser = argparse.ArgumentParser()

        group = parser.add_mutually_exclusive_group()
        group.add_argument("-d", "--dialog",
            action="store_const",
            const="dialog",
            dest="type",
            help="Use Dialog"
        )
        group.add_argument("-q", "--question", 
            action="store_const",
            const="question",
            dest="type",
            help="Use Question Dialog"
        )
        group.add_argument("-e", "--error", 
            action="store_const",
            const="error",
            dest="type",
            help="Use Error Dialog"
        )

        parser.add_argument("-t", "--title", help="Title of the dialog")
        parser.add_argument("-m", "--message", help="Message to display")

        parser.add_argument("--timeout", 
            help="Dialog timeout",
            type=int,
            metavar='N',
            default=None
        )

        self.args = parser.parse_args()
        self.exitcode = self.run()

    def run(self):
        switcher = {
            'dialog': self.dialog,
            'question': self.question,
            'error': self.error,
        }

        return switcher.get(self.args.type, lambda: False)()

    def dialog(self):
        return self.zenipy.message(
            title=self.args.title, 
            text=self.args.message,
            timeout=self.args.timeout,
        )

    def error(self):
        return self.zenipy.error(
            title=self.args.title, 
            text=self.args.message,
            timeout=self.args.timeout,
        )

    def question(self):
        return self.zenipy.question(
            title=self.args.title, 
            text=self.args.message,
            timeout=self.args.timeout,
        )

if __name__ == '__main__':
    app = Application()
    sys.exit(0) if app.exitcode else sys.exit(1)
