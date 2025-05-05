#!/usr/bin/env python3

import os, pathlib
import subprocess
import argparse

def get_args():
    parser = argparse.ArgumentParser("switch workspace and run command")
    parser.add_argument('cmd', nargs='*')
    parser.add_argument('-n','--name', required=True, help='workspace name')
    parser.add_argument('--i3wm', action='store_true')
    parser.add_argument('--sway', action='store_true')
    return parser.parse_args()



def main():
    args = get_args()
    cmd = ' '.join(args.cmd)
    name = args.name
    i3wm = args.i3wm
    sway = args.sway

    if sway:
        switch_ws = subprocess.run(f"swaymsg 'workspace {name} ; exec {cmd}'", shell=True)
    else:
        switch_ws = subprocess.run(f"i3-msg workspace {name} && exec {cmd}", shell=True)



main()
