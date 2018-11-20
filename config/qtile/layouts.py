from libqtile import layout

try:
    from plasma import Plasma
except:
    pass

layouts = []

try:
    layouts.extend([
        Plasma(
            border_normal='#333333',
            border_focus='#00e891',
            border_normal_fixed='#006863',
            border_focus_fixed='#00e8dc',
            border_width=1,
            border_width_single=0,
            margin=0
        ),
    ])
except:
    pass


layouts.extend([
    layout.Bsp(                                                                                                                                                                                              
        name='bsp'                                                                                                                                                                                           
    ),

    layout.Max(
        name='max'
    ),  

    layout.TreeTab(
        name='tree',
        panel_width=150,
        previous_on_rm=True,
        fontsize=16,
        # sections=['Shell']
    ),
])
