from libqtile.config import Screen
from libqtile import bar, widget

widget_defaults = dict(
    font='Cousine Nerd Font Mono',
    fontsize=14,
    padding=0,
)

screens = [
    Screen(
        top=bar.Bar([
                widget.GroupBox(
                    padding=5
                ),
                # widget.Prompt(**widget_defaults),
                widget.WindowName(
                    padding=3
                ),
                widget.Clock(format='⏰ %Y-%m-%d %a %I:%M %p', **widget_defaults),
                widget.Systray(**widget_defaults),
            ],
            size=30,
            background='#1d1f21',
            opacity=0.60
        ),
    ),
]
