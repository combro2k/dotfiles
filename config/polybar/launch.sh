#!/usr/bin/env sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch an bar at each display
export -a MONITOR
for MONITOR in $(bspc query -M --names); do
  polybar default > /dev/null 2> /dev/null &
done

echo "Bars launched..."
