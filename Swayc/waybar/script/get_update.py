#!/usr/bin/env python3

import subprocess


def exec_proc(cmd):
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
    return output


def main():
    #pac_update = exec_proc("checkupdates | wc -l")
    yay_update = exec_proc("yay -Qu | wc -l")
    #update = int(pac_update) + int(yay_update)
    update = int(yay_update)

    if update != 0:
        print(f'"full_text":"Update" , "color":"#dddd00"')
    #else:
    #    print('"full_text":"newest"')


main()
