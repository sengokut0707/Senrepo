#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0) && pwd)

rm -vr ~/.config/waybar/
mkdir -p ~/.config/waybar/
cp -vr $SCRIPT_DIR/waybar/* ~/.config/waybar
