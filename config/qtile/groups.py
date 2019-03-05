#from libqtile.config import Key
#from libqtile.command import lazy
from libqtile.config import Group, Match, ScratchPad, DropDown

from font_images import *

#from keys import keys, mod

groups = [Group(i) for i in "1234567890"]

groups.extend([
    Group(
        name='TeamViewer',
        matches=[Match(wm_instance_class=["TeamViewer"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label=f'TeamViewer',
    ),
 
    Group(
        name='Firefox',
        matches=[Match(wm_instance_class=["Firefox", "Navigator"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label=f'{www_ico}',
    ),
   
    Group(
        name='Editors',
        matches=[Match(wm_instance_class=["code", "Code", "emacs", "Emacs"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label=f'{edit_ico}',
    ),
 
    Group(
        name='Builder',
        matches=[Match(wm_instance_class=["gnome-builder"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label=f'{gnome_ico}',
    ),
   
#    Group(
#        name='Skype',
#        matches=[Match(wm_instance_class=["skype", "Skype"])],
#        exclusive=True,
#        persist=False,
#        layout='max',
#        init=False,
#        label=f'{skype_ico}',
#    ),
 
#    Group(
#        name='WeeChat',
#        matches=[Match(wm_instance_class=["weechat", "WeeChat"])],
#        exclusive=True,
#        persist=False,
#        layout='max',
#        init=False,
#        label=f'{wheechat_ico}',
   
    Group(
        name='GIMP',
        matches=[Match(wm_instance_class=["gimp", "Gimp", "gimp-2.10"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label=f'{gimp_ico}',
    ),

    Group(
        name='E-Mail',
        matches=[Match(wm_instance_class=["thunderbird", "Thunderbird", "Mail"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label=f'{email_ico}',
    ),

    Group(
        name='RDP',
        matches=[Match(wm_instance_class=["xfreerdp"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label=f'{rdp_ico}',
    ),

    # Group(
    #     name='Anbox',
    #     matches=[Match(wm_instance_class=["Anbox", "anbox"])],
    #     exclusive=True,
    #     persist=False,
    #     layout='max',
    #     init=False,
    #     label=f'{android_ico}',
    # ),

    ScratchPad("dropdown", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "urxvt-256color -bg '#1e1e1e' -name scratchpad -sh 100",
            opacity=1,
            warp_pointer=False,
            on_focus_lost_hide=False,
            x=0.05,
            y=0.05,
            width=0.9,
            height=0.85,
        ),

        DropDown("weechat", "urxvt-256color -name weechat -sh 100 -e ssh weechat@vmaurik.nl -p 5000",
            opacity=1,
            warp_pointer=False,
            on_focus_lost_hide=False,
            x=0.025,
            y=0.025,
            width=0.95,
            height=0.90,
        ),
    ]),
])
