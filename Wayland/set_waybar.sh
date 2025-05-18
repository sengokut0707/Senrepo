#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
config_dir="$HOME/.config/waybar"

mkdir -p $config_dir
rsync -avzuh --delete ${SCRIPT_DIR}/waybar/* $config_dir

echo 'otf-font-awesome please install'
