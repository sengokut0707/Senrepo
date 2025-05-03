#!/usr/bin/env bash

DIR="/sys/class/backlight/acpi_video0"
if [ -e $DIR ]; then
    AMT=2
else
    DIR="/sys/class/backlight/intel_backlight"
    AMT=2000
fi

CURR=`cat $DIR/brightness`
if [ $CURR -gt $AMT ]; then
    echo `expr -$AMT + $CURR` > $DIR/brightness
fi
