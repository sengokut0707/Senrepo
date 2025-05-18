#!/usr/bin/env python3
import os, pathlib, shutil
import argparse




homedir_path = pathlib.Path(os.path.expanduser("~"))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-j','--ja_to_en',nargs='+')
    parser.add_argument('-p','--homedir')
    return parser.parse_args()



def main():
    args = get_args()
    dirs_list = args.ja_to_en
    homedir = args.homedir

    if dirs_list:
        print("=== homedir_ja_to_en ===")
        homedir_ja_to_en(dirs_list)
    elif homedir:
        print("=== write_user_dirs ===")
        write_user_dirs(homedir)



def homedir_ja_to_en(dirs_list):
    ja_en_dict = {
        'デスクトップ':'Desktop',
        'ダウンロード':'Downloads',
        'テンプレート':'Templates',
        '公開':'Public',
        'ドキュメント':'Documents',
        '音楽':'Music',
        '画像':'Pictures',
        'ビデオ':'Videos'
    }

    for _dir in dirs_list:
        dir_path = pathlib.Path(_dir).resolve()
        parent = dir_path.parent
        dirname = dir_path.name

        en_name = ja_en_dict.get(dirname)
        if en_name:
            shutil.move(dir_path, parent/en_name)
            print(f"move {dirname} >> {en_name}")



def write_user_dirs(homedir):
    homedir = pathlib.Path(homedir).resolve()
    text_list = [
        f'# This file is written by xdg-user-dirs-update',
        f'# If you want to change or add directories, just edit the line youre',
        f'# interested in. All local changes will be retained on the next run.',
        f'# Format is XDG_xxx_DIR="$HOME/.HomeDirs/yyy", where yyy is a shell-escaped',
        f'# homedir-relative path, or XDG_xxx_DIR="/yyy", where /yyy is an',
        f'# absolute path. No other format is supported.',
        f'# ',
        f'XDG_DESKTOP_DIR="{homedir}/Desktop"',
        f'XDG_DOWNLOAD_DIR="{homedir}/Downloads"',
        f'XDG_TEMPLATES_DIR="{homedir}/Templates"',
        f'XDG_PUBLICSHARE_DIR="{homedir}/Public"',
        f'XDG_DOCUMENTS_DIR="{homedir}/Documents"',
        f'XDG_MUSIC_DIR="{homedir}/Music"',
        f'XDG_PICTURES_DIR="{homedir}/Pictures"',
        f'XDG_VIDEOS_DIR="{homedir}/Videos"',
    ]

    user_dirs_text = '\n'.join(text_list)

    user_dirs_file = pathlib.Path.home()/'.config/user-dirs.dirs'
    with open(user_dirs_file, 'w') as f:
        f.write(user_dirs_text)
    print("write user-dirs.dirs")



if __name__ == '__main__':
    main()

