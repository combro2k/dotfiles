from libqtile.config import Screen
from libqtile import bar, widget

screens = [
    Screen(
        top=bar.Bar([
                widget.GroupBox(padding=2, fontsize=14),
                widget.Prompt(),
                widget.WindowName(),
                widget.Clock(format='⏰ %Y-%m-%d %a %I:%M %p'),
                widget.Systray(),
            ],
            size=24,
            background='#1d1f21',
            opacity=0.60
        ),
    ),
]