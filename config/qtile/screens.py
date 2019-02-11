from libqtile.config import Screen
from libqtile import bar, widget

from widgets import MenuWidget, ActionMenuWidget, WindowNameNew, TaskListNew

from classes import Helpers

get_screen_size = Helpers.get_screen_size
screensize = get_screen_size()

widget_defaults = dict(
    font='SauceCodePro Nerd Font Mono',
    fontsize=12 if screensize['height'] <= 1050 else 16,
    background='585858',
    markup=True,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
                MenuWidget(
                    background='3badea',
                    fontsize=36 if screensize['height'] <= 1050 else 40,
                    padding=10,
                ),
                widget.CurrentLayout(
                    foreground='ffffff',
                    background='585858',
                    fontsize=13 if screensize['height'] <= 1050 else 14,
                    padding=10,
                ),
                widget.GroupBox(
                    padding=0 if screensize['height'] <= 1050 else 5,
                    fontsize=15 if screensize['height'] <= 1050 else 19,
                    highlight_method='block',
                    spacing=0,
                    use_mouse_wheel=False,
                    disable_drag=True,
                    active='ffffff',
                    background='585858',
                    this_current_screen_border='3badea',
                    other_current_screen_border='ffffff',
                    urgent_alert_method='block',
                    inactive='8e8e8e',
                ),
                TaskListNew(
                    spacing=0,
                    padding=0 if screensize['height'] <= 1050 else 5,
                    background='585858',
                    border='3badea',
                    fontsize=16 if screensize['height'] <= 1050 else 19,
                    highlight_method='block',
                    rounded=False,
                    title_width_method='uniform',
                ),
#                WindowNameNew(
#                    background='3badea',
#                    fontsize=14,
#                    padding=10,
#                ),
                widget.Systray(
                    background='585858',
                    padding=10,
                ),
                widget.BatteryIcon(
                    background='585858',
                ),
                widget.Clock(
                    background='585858',
                    fontsize=16 if screensize['height'] <= 1050 else 20,
                    format='%I:%M %p',
                    padding=10,
                ),
                ActionMenuWidget(
                    background='3badea',
                    fontsize=32 if screensize['height'] <= 1050 else 40,
                    padding=10,
                ),
            ],
            size=27 if screensize['height'] <= 1050 else 40,
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
