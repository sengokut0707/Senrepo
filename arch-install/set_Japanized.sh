#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

sudo pacman -S noto-fonts-cjk
sudo pacman -S fcitx-im fcitx-mozc
sudo pacman -S fcitx-configtool
#cat $SCRIPT_DIR/xprofile > ~/.xprofile
echo ""
echo "please set xprofile and fcitx-configtool setting mozc"
