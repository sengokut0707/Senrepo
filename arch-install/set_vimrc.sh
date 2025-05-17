#!/usr/bin/bash

SCRIPT_DIR=$(cd $(dirname $0) && pwd)

mkdir -p ~/.vim/undo
cat $SCRIPT_DIR/vimrc > ~/.vimrc
