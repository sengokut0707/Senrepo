#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0) && pwd)
config_dir="$HOME/.config/ranger"

rsync -avzuh --delete $SCRIPT_DIR/* $config_dir
echo "please install w3m"
