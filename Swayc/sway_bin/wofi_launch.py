#!/usr/bin/env python3

import subprocess
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--text_files',default=[],nargs='*')
    return parser.parse_args()


def main():
    args = get_args()
    text_files = args.text_files

    wofi_dict = {}
    for text_file in text_files:
        text_list = get_text_list(text_file)
        wofi_dict.update(get_wofi_dict(text_list))
    title_list = list(wofi_dict.keys())
    user_input = subprocess.run(get_wofi_cmd(title_list), shell=True, capture_output=True, text=True).stdout
    if not user_input:
        print('Null')
        exit()
    elif wofi_dict.get(user_input.rstrip('\n')):
        cmd = wofi_dict.get(user_input.rstrip('\n'))
    else:
        cmd = ""
        for title in title_list:
            if user_input.rstrip('\n') in title:
                cmd = wofi_dict.get(title.rstrip('\n'))
                break
    proc = subprocess.run(cmd, shell=True)


def get_text_list(text_file):
    with open(text_file) as f:
        text_list = [s.strip() for s in f.readlines()]
        text_list = [s for s in text_list if not s.startswith('#')]
        text_list = [s for s in text_list if not s == '']
    return text_list


def get_wofi_dict(text_list):
    wofi_dict = {}
    for text in text_list:
        title, cmd = text.split(',')
        title, cmd = [s.strip() for s in [title, cmd]]
        title = name_repair(title)
        if cmd.startswith('http'):
            cmd = 'xdg-open ' + cmd
        wofi_dict[title] = cmd
    return wofi_dict


def get_wofi_cmd(title_list):
    ttl = '"\n"'.join(title_list)
    wofi_cmd = f'echo {ttl}| wofi -dmenu -p bookmark -disable-history -s ~/.config/wofi/*.css'
    return wofi_cmd



def name_repair(name):
    ## タイトルに使えない文字の排除
    for i in '\\' , '\"' , '\'' , '/' , ':' , '*' , '?' , '<' , '>' , '|' , '[' , ']' , ' ':
        name = name.replace(i,'_')
    while '__' in name:
        name = name.replace('__','_')
    return name
    

main()
