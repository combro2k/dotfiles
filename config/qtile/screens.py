from libqtile.config import Screen
from libqtile import bar, widget

from widgets import MenuWidget, ActionMenuWidget, WindowNameNew

widget_defaults = dict(
    font='SauceCodePro Nerd Font Mono',
    fontsize=14,
    padding=10,
    background='001c3d',
    markup=True
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
                widget.Spacer(
                    length=4
                ),
                MenuWidget(
                    background='3badea',
                    fontsize=28,
                    padding=10
                ),
                widget.CurrentLayout(
                    foreground='ffffff',
                    background='585858',
                    fontsize=12,
                    padding=10
                ),
                widget.GroupBox(
                    padding=1,
                    fontsize=16,
                    highlight_method='block',
                    spacing=0,
                    use_mouse_wheel=False,
                    disable_drag=True,
                    active='ffffff',
                    background='585858',
                    this_current_screen_border='3badea',
                    other_current_screen_border='ffffff',
                    urgent_alert_method='block',
                    inactive='8e8e8e'
                ),
                WindowNameNew(
                    background='3badea',
                    padding=10
                ),
                widget.Systray(
                    background='585858',
                    padding=10
                ),
                widget.BatteryIcon(
                    background='585858',
                ),
                widget.Clock(
                    background='585858',
                    fontsize=18,
                    format='%I:%M %p',
                    padding=20
                ),
                ActionMenuWidget(
                    background='3badea',
                    fontsize=20,
                    padding=10
                ),
            ],
            size=30,
#            background='1d1f21',
            background='585858',
            opacity=0.888888880
        ),
#        bottom=bar.Bar([
#            size=30,
#            background='#1d1f21',
#            opacity=0.888888880
#        ]),
    ),
]
