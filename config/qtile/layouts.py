from libqtile import layout

layouts = [

    layout.Bsp(
        name='bsp',
        lower_right=True,
        fair=True
    ),

    layout.MonadWide(
        name='xmonadw',
    ),

    layout.Max(
        name='max'
    ),

    layout.TreeTab(
        name='tree'
    ),

]
