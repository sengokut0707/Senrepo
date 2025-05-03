#!/usr/bin/env python3

import os
import subprocess
import random
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='mp3 player')
    parser.add_argument('argv_list',nargs='*',help='dirs指定。files指定も可')
    parser.add_argument('-s','--shuffle',action='store_true')
    parser.add_argument('-n','--newest',type=int, help="名前順で指定した数だけ抽出。")
    parser.add_argument('-r','--single_repeat',action='store_true')
    parser.add_argument('-l','--list_repeat',action='store_true')
    parser.add_argument('-p','--playnumber',type=int,default=1,help='playlistの開始番号')
    parser.add_argument('-v','--volume',type=int,default=70)
    return parser.parse_args()


def main():
    args = get_args()
    shuffle = args.shuffle
    newest = args.newest
    single_repeat = args.single_repeat
    list_repeat = args.single_repeat
    volume = args.volume
    playnumber = int(args.playnumber - 1)
    argv_list = args.argv_list


    file_list = get_file_list(argv_list)
    file_list = [file for file in file_list if not '.stversions' in file]

    option_list = []
    if shuffle:
        option_list.append("--shuffle")
        random.shuffle(file_list)
    if newest:
        dict_list = [{'file':file, 'file_name':os.path.basename(file)} for file in file_list]
        dict_list = sorted(dict_list, key=lambda x: x['file_name'], reverse=True)
        file_list = [_dict.get('file') for _dict in dict_list[:newest]]
    if single_repeat:
        option_list.append("--loop-file")
    if list_repeat:
        option_list.append("--loop-playlist")
    option_list.append(f"--volume={volume}")
    option_list.append(f"--playlist-start={playnumber}")

    play_music(file_list ,option_list)


def play_music(file_list, option_list):
    music_files = ''
    for file in file_list:
        music_files += f"\"{file}\" "

    options = ' '.join(option_list)

    command = f"mpv --no-video {options} {music_files}"

    try:
        proc = subprocess.run(command,shell=True)
    except KeyboardInterrupt:
        pass
    

def get_file_list(argv_list):
    file_list=[]
    for argv in argv_list:
        if os.path.isfile(argv):
            file_list += argv_list
        elif os.path.isdir(argv):
            file_list += find_all_files(argv)
    file_list = [i for i in file_list if '.mp3' in i]
    return file_list


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)
main()
