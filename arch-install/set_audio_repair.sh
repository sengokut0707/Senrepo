#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

sudo pacman -S pulseaudio
sudo rm -rfv /usr/share/pulseaudio/alsa-mixer/paths/analog-output-speaker.conf
sudo cp -vr $SCRIPT_DIR/analog-output-speaker.conf  /usr/share/pulseaudio/alsa-mixer/paths/analog-output-speaker.conf
