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

    rofi_dict = {}
    for text_file in text_files:
        text_list = get_text_list(text_file)
        rofi_dict.update(get_rofi_dict(text_list))
    title_list = list(rofi_dict.keys())
    title = subprocess.run(get_rofi_cmd(title_list), shell=True, capture_output=True, text=True).stdout
    if not title:
        print('Null')
        exit()
    elif rofi_dict.get(title.rstrip('\n')):
        cmd = rofi_dict.get(title.rstrip('\n'))
    else:
        cmd = ""
        ## キーワード検索
        #target = '+'.join(title.rstrip('\n').split(' '))
        #cmd = "xdg-open 'http://google.com/search?q=" + target + "' 1>/dev/null 2>/dev/null" 
        #print(cmd)
    proc = subprocess.run(cmd, shell=True)


def get_text_list(text_file):
    with open(text_file) as f:
        text_list = [s.strip() for s in f.readlines()]
        text_list = [s for s in text_list if not s.startswith('#')]
        text_list = [s for s in text_list if not s == '']
    return text_list


def get_rofi_dict(text_list):
    rofi_dict = {}
    for text in text_list:
        title, cmd = text.split(',')
        title, cmd = [s.strip() for s in [title, cmd]]
        title = name_repair(title)
        if cmd.startswith('http'):
            cmd = 'xdg-open ' + cmd
        rofi_dict[title] = cmd
    return rofi_dict


def get_rofi_cmd(title_list):
    ttl = '"\n"'.join(title_list)
    rofi_cmd = f'echo {ttl}| wofi -dmenu -p bookmark -disable-history -s ~/.config/wofi/*.css'
    return rofi_cmd



def name_repair(name):
    ## タイトルに使えない文字の排除
    for i in '\\' , '\"' , '\'' , '/' , ':' , '*' , '?' , '<' , '>' , '|' , '[' , ']' , ' ':
        name = name.replace(i,'_')
    while '__' in name:
        name = name.replace('__','_')
    return name
    

main()
