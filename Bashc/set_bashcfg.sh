#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0) && pwd)

rm -vr ~/.bash_cfg
mkdir -p ~/.bash_cfg
cp -vr $SCRIPT_DIR/* ~/.bash_cfg/

if ! grep "bash_cfg/bash_cfg.bash" ~/.bashrc; then
    echo "source ~/.bash_cfg/bash_cfg.bash" >> ~/.bashrc
fi

echo "source ~/.bashrc" > ~/.bash_profile

mkdir -p ~/.config/fish/
cp -v $SCRIPT_DIR/fish_cfg.fish ~/.config/fish/config.fish
