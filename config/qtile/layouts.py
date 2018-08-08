from libqtile import layout

layouts = [
    layout.Bsp(
        name='bsp',
        lower_right=True,
        fair=True
    ),

    # layout.MonadWide(
    #     name='xmonadw',
    # ),

    layout.Max(
        name='max'
    ),

    layout.TreeTab(
        name='tree',
        panel_width=100,
        previous_on_rm=True,
        fontsize=16,
        sections=['Shell']
    ),
]
