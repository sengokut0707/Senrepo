#!/usr/bin/env bash

if [ $# == 0 ]; then
    :
elif [ $# == 1 ]; then
    args=$1
else
    args="$@"
fi
git commit -m "$args"
