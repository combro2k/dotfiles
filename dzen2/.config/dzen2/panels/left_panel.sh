#!/usr/bin/env bash

bspc query -m -D --names > "$PANEL_FIFO" &
