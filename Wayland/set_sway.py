#!/usr/bin/env python3
import os
import re
import pathlib
import subprocess

def main():
    # ディレクトリ・ファイルのパスを設定
    script_dir = pathlib.Path(__file__).resolve().parent
    homedir = pathlib.Path.home()
    config_dir = homedir / '.config/sway/'

    i3_cmd = f"rsync -avzuh --delete {script_dir}/ {config_dir}"
    i3_proc = subprocess.run(i3_cmd, shell=True)

if __name__ == "__main__":
    main()
