#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

sudo pacman -S noto-fonts-cjk
sudo pacman -S fcitx5 fcitx5-im fcitx5-mozc fcitx5-configtool fcitx5-gtk
#sudo pacman -S fcitx-im fcitx-mozc
#cat $SCRIPT_DIR/xprofile > ~/.xprofile
echo ""
echo "please set xprofile and fcitx-configtool setting mozc"
