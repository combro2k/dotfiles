from libqtile.config import Screen
from libqtile import bar, widget

from classes import MenuWidget, ActionMenuWidget

widget_defaults = dict(
    font='Cousine Nerd Font Mono',
    fontsize=14,
    padding=2,
    markup=True
)

screens = [
    Screen(
        top=bar.Bar([
                MenuWidget(
                    fontsize=24
                ),
                
                widget.Spacer(
                    length=5
                ),

                widget.GroupBox(
                    padding=1,
                    fontsize=19,
                    highlight_method='block',
                    spacing=0,
                    use_mouse_wheel=False,
                    disable_drag=True,
                    active='ffffff',
                    this_current_screen_border='82ea3c',
                    other_current_screen_border='ffffff',
                    urgent_alert_method='block',
                    inactive='8e8e8e'
                ),

                widget.Spacer(
                    length=5
                ),

                widget.CurrentLayout(
                    foreground='ff0000',
                    padding=3
                ),

                # widget.Prompt(**widget_defaults),
                widget.WindowName(
                    padding=10
                ),

                widget.Spacer(
                    length=5
                ),

                widget.Clock(format='⏰ %Y-%m-%d %a %I:%M %p', **widget_defaults),

                widget.Systray(
                    padding=2    
                ),

                ActionMenuWidget(
                    fontsize=24
                ),
            ],
            size=30,
            background='#1d1f21',
            opacity=0.888888880
        ),
    ),
]
