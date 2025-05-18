#!/usr/bin/env python3

import os,sys,glob
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('dirs',default='[.]',nargs='*')
    parser.add_argument('-n','--name')
    parser.add_argument('-t','--text',action='store_true')
    parser.add_argument('-f','--file',action='store_true')
    parser.add_argument('-d','--dir',action='store_true')
    return parser.parse_args()

def main():
    args = get_args()
    dirs = args.dirs
    name = args.name
    flag_dic = {}
    flag_dic['text'] = args.text
    flag_dic['file'] = args.file
    flag_dic['dir'] = args.dir
    find_list = find_proc(dirs, name, flag_dic)
    for find in find_list:
        print(find)
    
    
def find_proc(dirs, name, flag_dic):
    find_list = []
    for dirname in dirs:
        if name == None:
            find_list += glob.glob(f"{dirname}/**", recursive=True)
        else:
            find_list += glob.glob(f"{dirname}/**/*{name}*", recursive=True)
        if f"{dirname}/" in find_list:
            find_list.remove(f"{dirname}/")
    if flag_dic.get('text'):
        find_list = [f for f in find_list if os.path.isfile(f)]
        find_list = [f for f in find_list if is_text_file(f)]
    elif flag_dic.get('file'):
        find_list = [f for f in find_list if os.path.isfile(f)]
    elif flag_dic.get('dir'):
        find_list = [d for d in find_list if os.path.isdir(d)]
    return sorted(find_list)


def is_text_file(file):
    def is_binary_string(Bytes):
        textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
        result = bool(Bytes.translate(None, textchars))
        return result
    result = is_binary_string(open(file, 'rb').read(1024))
    if result:
        return False
    else:
        return True

        

main()
