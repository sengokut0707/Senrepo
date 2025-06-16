#!/usr/bin/bash

SCRIPT_DIR=$(cd $(dirname $0) && pwd)

mkdir -p ~/.config/nvim
cat $SCRIPT_DIR/vimrc > ~/.config/nvim/init.vim
