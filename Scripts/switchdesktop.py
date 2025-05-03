#!/usr/bin/env python3

import os, pathlib
import subprocess
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--desktop',required=True)
    return parser.parse_args()

def main():
    args = get_args()
    desktop_env = args.desktop

    cmd = f"sudo sed -i 's/^autologin-session=.*$/autologin-session={desktop_env}/' /etc/lightdm/lightdm.conf"

    proc = subprocess.run(cmd, shell=True)

    print("comp! please reboot")

if __name__ == '__main__':
    main()

