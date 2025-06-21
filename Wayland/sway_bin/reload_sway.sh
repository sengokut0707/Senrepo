#!/usr/bin/env bash

swaymsg reload || i3-msg restart
pkill waybar ; waybar &
