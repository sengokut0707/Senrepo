#!/usr/bin/env bash

DIR="/sys/class/backlight/acpi_video0"
if [ -e $DIR ]; then
    AMT=2
else
    DIR="/sys/class/backlight/intel_backlight"
    AMT=2000
fi
MAX=`cat $DIR/max_brightness`
CURR=`cat $DIR/brightness`
MAX=`expr -$AMT + $MAX`
if [ $CURR -lt $MAX ]; then
    echo `expr $CURR + $AMT` > $DIR/brightness
fi
