from libqtile.config import Screen
from libqtile import bar, widget

from classes import MenuWidget, ActionMenuWidget

widget_defaults = dict(
    font='Cousine Nerd Font Mono',
    fontsize=14,
    padding=2,
    background='001c3d',
    markup=True
)

screens = [
    Screen(
        top=bar.Bar([
                widget.Spacer(
                    length=4
                ),
                MenuWidget(
                    background='3badea',
                    fontsize=24,
                    padding=4
                ),
                widget.Spacer(
                    length=5
                ),
                widget.CurrentLayout(
                    background='000000',
                    foreground='ffffff',
                    padding=3
                ),
                widget.GroupBox(
                    padding=1,
                    fontsize=19,
                    highlight_method='block',
                    spacing=0,
                    use_mouse_wheel=False,
                    disable_drag=True,
                    active='ffffff',
                    this_current_screen_border='3badea',
                    other_current_screen_border='ffffff',
                    urgent_alert_method='block',
                    inactive='8e8e8e'
                ),
                widget.Spacer(
                    length=5
                ),
                # widget.Prompt(**widget_defaults),
                widget.WindowName(
                    # background='3badea',
                    padding=10
                ),
                widget.Spacer(
                    length=5
                ),
                widget.Systray(
                    padding=2    
                ),
                widget.Spacer(
                    length=5
                ),
                widget.BatteryIcon(

                ),
                widget.Spacer(
                    length=5
                ),
                widget.Clock(
                    format='%I:%M %p'
                ),
                widget.Spacer(
                    length=5
                ),
                ActionMenuWidget(
                    fontsize=24
                ),
                widget.Spacer(
                    length=10
                ),
            ],
            size=30,
            background='#1d1f21',
            opacity=0.888888880
        ),
    ),
]
