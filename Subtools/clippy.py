#!/usr/bin/env python3

import sys,os
import pyperclip
import argparse

def get_args():
    parser = argparse.ArgumentParser('テキストやテキストファイルをクリップボードにコピーします。')
    parser.add_argument('argv', nargs='*', help='テキストファイルを指定します。')
    return parser.parse_args()


def main():
    args = get_args()
    argv_list = args.argv

    result_list = []
    for argv in argv_list:
        if os.path.isfile(argv):
            with open(argv) as f:
                text = f.read()
        else:
            text = argv
        result_list.append(text)

    result = '\n'.join(result_list)
    pyperclip.copy(result)
    print("クリップボードにコピーしました。")

if __name__ == '__main__':
    main()


