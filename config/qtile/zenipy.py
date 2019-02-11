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

    DEFAULT_WIDTH = 330
    DEFAULT_HEIGHT = 120

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
        group.add_argument("--info",
            action="store_const",
            const="info",
            dest="type",
            help="Info Dialog"
        )
        group.add_argument("--notification",
            action="store_const",
            const="info",
            dest="type",
            help="Info Dialog"
        )
        group.add_argument("--question", 
            action="store_const",
            const="question",
            dest="type",
            help="Use Question Dialog"
        )
        group.add_argument("--error", 
            action="store_const",
            const="error",
            dest="type",
            help="Use error dialog"
        )
        group.add_argument("--warning", 
            action="store_const",
            const="warning",
            dest="type",
            help="Use warning dialog"
        )

#        group.add_argument("--warning",
#            action="store_const",
#            const="warning",
#            dest="type",
#            help="Use Warning Dialog"
#        )


        parser.add_argument("-t", "--title", 
            help="Title of the dialog",
            default=sys.argv[0],
        )
        parser.add_argument("--text", 
            help="Text to display",
            default=None,
        )
        parser.add_argument("--width", 
            help="Width of dialog",
            type=int,
            metavar='N',
            default=self.DEFAULT_WIDTH,
        )
        parser.add_argument("--height", 
            help="Height of dialog",
            type=int,
            metavar='N',
            default=self.DEFAULT_HEIGHT,
        )

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
            'info': self.info,
            'question': self.question,
            'error': self.error,
            'warning': self.warning,
            None: self.info,
        }

        return switcher.get(self.args.type, lambda: None)()

    def info(self):
        return self.zenipy.message(
            title=self.args.title, 
            text=self.args.text,
            timeout=self.args.timeout,
            width=self.args.width,
            height=self.args.height,
        )

    def error(self):
        return self.zenipy.error(
            title=self.args.title, 
            text=self.args.text,
            timeout=self.args.timeout,
            width=self.args.width,
            height=self.args.height,
       )

    def warning(self):
        return self.zenipy.warning(
            title=self.args.title, 
            text=self.args.text,
            timeout=self.args.timeout,
            width=self.args.width,
            height=self.args.height,
      )


    def question(self):
        return self.zenipy.question(
            title=self.args.title, 
            text=self.args.text,
            timeout=self.args.timeout,
            width=self.args.width,
            height=self.args.height,
       )

if __name__ == '__main__':
    app = Application()
    sys.exit(0) if app.exitcode else sys.exit(1)
