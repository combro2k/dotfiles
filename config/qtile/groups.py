from libqtile.config import Key
from libqtile.command import lazy

from libqtile.config import Key, Group, Match

from keys import keys, mod

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

groups.append(
    Group(
        name='Firefox',
        matches=[Match(wm_class=["Firefox"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label='Firefox',
    ))

groups.append(
    Group(
        name='VisualCode',
        matches=[Match(wm_class=["Code"])],
        exclusive=True,
        persist=False,
        layout='max',
        init=False,
        label='VisualCode',
    ))