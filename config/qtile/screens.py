from libqtile.config import Screen
from libqtile import bar, widget

from widgets import widget_defaults

screens = [
    Screen(
        top=bar.Bar([
                widget.GroupBox(
                    disable_drag=True,
                    **widget_defaults
                ),
                widget.Prompt(**widget_defaults),
                widget.WindowName(**widget_defaults),
                widget.Clock(format='⏰ %Y-%m-%d %a %I:%M %p', **widget_defaults),
                widget.Systray(**widget_defaults),
            ],
            size=24,
            background='#1d1f21',
            opacity=0.60
        ),
    ),
]
