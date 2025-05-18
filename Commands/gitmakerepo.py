#!/usr/bin/env python3

import os, pathlib
import argparse
import subprocess

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('dirname')
    return parser.parse_args()

def main():
    args = get_args()
    dirname = args.dirname
    host = "Raspi"
    remote = "/home/Git_dir.git"


    mkrmt_cmd = f'ssh {host} "cd /home/Git_dir.git/ && mkdir {dirname}.git && cd ./{dirname}.git && git --bare init --share"'
    proc = subprocess.run(mkrmt_cmd, shell=True)

    os.makedirs(dirname, exist_ok=True) 
    mkgit_cmd = f"cd {dirname} && git init && git remote add origin {host}:{remote}/{dirname}.git"
    proc = subprocess.run(mkgit_cmd, shell=True)




main()
