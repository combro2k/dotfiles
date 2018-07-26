#from libqtile.config import Key
#from libqtile.command import lazy
from libqtile.config import Group, Match, ScratchPad, DropDown

from font_images import *

#from keys import keys, mod

groups = [Group(i) for i in "1234567890"]

groups.extend([
    Group(
        name='Firefox',
        matches=[Match(wm_class=["Firefox"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label=f'{www_ico}',
    ),
    Group(
        name='VisualCode',
        matches=[Match(wm_class=["Code"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label=f'{edit_ico}',
    ),
    Group(
        name='Skype',
        matches=[Match(wm_class=["Skype"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label=f'{skype_ico}',
    ),
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "urxvt-256color", 
            opacity=0.9,
            on_focus_lost_hide=True,
            x=0.1,
            y=0.1,
            width=0.8,
            height=0.70
        ),

    ]),
])
