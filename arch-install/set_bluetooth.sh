#!/usr/bin/env bash

sudo pacman -S bluez bluez-utils blueberry

sudo systemctl enable bluetooth.service
sudo systemctl start bluetooth.service
