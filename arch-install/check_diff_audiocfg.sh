#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
diff $SCRIPT_DIR/analog-output-speaker.conf /usr/share/pulseaudio/alsa-mixer/paths/analog-output-speaker.conf
