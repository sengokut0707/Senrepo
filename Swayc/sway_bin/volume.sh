#!/usr/bin/env bash

volume=`amixer -D pulse sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }'`
mute_stat=`amixer -D pulse sget Master | grep 'Right:' | awk -F'[][]' '{ print $4 }'`

if [ $mute_stat = 'on' ]; then
    echo $volume
else
    echo 'mute'
fi
