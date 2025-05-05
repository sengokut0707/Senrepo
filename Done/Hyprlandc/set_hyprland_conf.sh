#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0) && pwd)

rm -vr ~/.config/hypr/
mkdir -p ~/.config/hypr/
cp -vr $SCRIPT_DIR/* ~/.config/hypr/
