#from libqtile.config import Key
#from libqtile.command import lazy
from libqtile.config import Group, Match, ScratchPad, DropDown

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
        label='Firefox',
    ),
    Group(
        name='VisualCode',
        matches=[Match(wm_class=["Code"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label='VisualCode',
    ),
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "urxvtc-256color", 
            opacity=0.9,
            on_focus_lost_hide=True,
            x=0.1,
            y=0.1,
            width=0.8,
            height=0.70
        ),

    ]),
])
