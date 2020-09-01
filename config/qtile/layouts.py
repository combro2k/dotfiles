from libqtile import layout

from libqtile.log_utils import logger

try:
    from plasma import Plasma
except Exception as e:
    logger.error(e)
    pass

layouts = []

try:
    layouts.extend([
        Plasma(
            name='plasma',
            border_normal='#333333',
            border_focus='#3badea',
            border_normal_fixed='#006863',
            border_focus_fixed='#3badea',
            border_width=1,
            border_width_single=1,
            margin=0,
        ),
    ])
except Exception as e:
    logger.error(e)
    pass


layouts.extend([
    layout.Bsp(
        name='bsp',
        border_normal='#333333',
        border_focus='#3badea',
        border_normal_fixed='#006863',
        border_focus_fixed='#3badea',
        border_width=1,
        border_width_single=1,
        margin=0,
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
