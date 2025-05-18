#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0) && pwd)

cp -v $SCRIPT_DIR/ssh_config ~/.ssh/config
