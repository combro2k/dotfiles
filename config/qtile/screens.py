from libqtile.config import Screen
from libqtile import bar, widget

from widgets import MenuWidget, ActionMenuWidget, WindowNameNew, TaskListNew

from classes import Helpers

get_type_screen = Helpers.get_type_screen
type_screen = get_type_screen()

widget_defaults = dict(
    font='SauceCodePro Nerd Font Mono',
    fontsize=12 if type_screen != '4K UHD' else 18,
    background='585858',
    markup=True,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
                MenuWidget(
                    background='3badea',
                    fontsize=36 if type_screen != '4K UHD' else 60,
                    padding=10,
                ),
                widget.CurrentLayout(
                    foreground='ffffff',
                    background='585858',
                    fontsize=13 if type_screen != '4K UHD' else 18,
                    padding=10,
                ),
                widget.GroupBox(
                    padding=0 if type_screen != '4K UHD' else 3,
                    fontsize=15 if type_screen != '4K UHD' else 24,
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
                    padding=0 if type_screen != '4K UHD' else 4,
                    background='585858',
                    border='3badea',
                    fontsize=16 if type_screen != '4K UHD' else 24,
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
                widget.Volume(
                     background='585858',
                     padding=10,
                ),
                widget.BatteryIcon(
                    background='585858',
                ),
                widget.Clock(
                    background='585858',
                    fontsize=16 if type_screen != '4K UHD' else 26,
                    format='%I:%M %p',
                    padding=10,
                ),
                ActionMenuWidget(
                    background='3badea',
                    fontsize=32 if type_screen != '4K UHD' else 50,
                    padding=10,
                ),
            ],
            size=27 if type_screen != '4K UHD' else 44,
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
