#!/usr/bin/env python3

import pprint
import argparse
import collections
import copy
import datetime
import natsort
import os
import pathlib
import re
import shutil
import subprocess
import tempfile


def get_args():
    parser = argparse.ArgumentParser('テキストエディタを使用してファイルの名前変更')
    parser.add_argument('argv', nargs='*' ,help="名前を変更するディレクトリ、ファイル。--restoreのとき、timestamp指定")
    parser.add_argument('-d', '--date', action='store_true', help="日付順")
    parser.add_argument('-e', '--editor', default='vim', help="テキストエディタ")
    parser.add_argument('-r', '--restore', action='store_true')
    parser.add_argument('-f', '--force', action='store_true')
    parser.add_argument('--dirname', action='store_true')
    parser.add_argument('-t', '--text_file')
    return parser.parse_args()



def main():
    args = get_args()
    argv_list = args.argv
    date_flag = args.date
    editor = args.editor
    restore = args.restore
    force = args.force
    dirname = args.dirname
    text_file = args.text_file

    homedir = pathlib.Path.home()
    log_csvfile = homedir/'.vrename-log.csv'
    
    if restore:
        timestamp = ''
        if restore and argv_list:
            timestamp = argv_list[0]
        before_path_list, after_name_list = get_restore_proc(log_csvfile, timestamp)
    elif dirname:
        if len(argv_list) == 0:
            argv_list = os.listdir('./')
        elif argv_list[0] == './':
            argv_list = os.listdir('./')
        before_path_list = [pathlib.Path(f).resolve() for f in sorted(argv_list)]


        _parent_list_list = []
        _parent_list = []
        for i in range(len(before_path_list)):
            p = before_path_list[i]
            _parent_list.append(p)
            if i+1 < len(before_path_list):
                nextp = before_path_list[i+1]
                if p.parent.name == nextp.parent.name:
                    continue
            if _parent_list:
                _parent_list_list.append(_parent_list)
                _parent_list = []

        after_name_list = []
        for _parent_list in _parent_list_list:
            index = 0
            for p in _parent_list:
                index += 1
                num_str = str(index).zfill(len(str(len(_parent_list))))
                _name = f"{p.parent.name}_{num_str}{p.suffix}"
                after_name_list.append(_name)
    elif text_file:
        if len(argv_list) == 0:
            argv_list = os.listdir('./')
        elif argv_list[0] == './':
            argv_list = os.listdir('./')

        argv_path_list = [pathlib.Path(f) for f in argv_list]

        before_path_list = get_before_path_list(argv_path_list, mode='dir')

        with open(text_file) as f:
            text_l = [s.strip() for s in f.readlines()]
        after_name_list = text_l
    else:
        if len(argv_list) == 0:
            argv_list = os.listdir('./')
        elif argv_list[0] == './':
            argv_list = os.listdir('./')

        if date_flag:
            mode = 'date'
        else:
            mode = 'dir'

        argv_path_list = [pathlib.Path(f) for f in argv_list]

        before_path_list = get_before_path_list(argv_path_list, mode)
        after_name_list = get_after_name_list(before_path_list, editor)

    rename_proc(before_path_list, after_name_list, log_csvfile, force)
    print("finish!")



def rename_proc(before_path_list, after_name_list, log_csvfile, force):
    ## after_name_listが少ない場合、length_error回避のため空白で埋める
    if len(before_path_list) > len(after_name_list):
        delta = len(before_path_list) - len(after_name_list)
        for i in range(delta):
            after_name_list.append([''])

    ## after_name_listの重複に'_'を追記し解決する
    while [k for k, v in collections.Counter(after_name_list).items() if v > 1]:
        dup_name = [k for k, v in collections.Counter(after_name_list).items() if v > 1][0]
        _list = []
        _str = ''
        for name in after_name_list:
            if name == dup_name:
                basename, ext = os.path.splitext(name)
                name = f"{basename}{_str}{ext}"
                _str += '_'
            _list.append(name)
        after_name_list = _list


    ## get before & after list
    parent_list = [p.parent for p in before_path_list]
    result_list = []
    _before_l = []
    _after_l = []
    for i in range(len(before_path_list)):
        ## 以下の条件の時、renameしない
        if before_path_list[i].name == after_name_list[i]:
            continue
        elif after_name_list[i].strip() == '':
            continue
        else:
            _before_l.append(before_path_list[i])
            _after_l.append(pathlib.Path(f"{parent_list[i]}/{after_name_list[i]}"))
    result_text = '\n'.join([f"\"{b.name}\" >> \"{a.name}\"" for b,a in zip(_before_l,_after_l)])
    before_path_list = _before_l
    after_path_list = _after_l

    if len(before_path_list) == 0:
        print("実行しませんでした。")
        exit()

    if force:
        choice = 'yes'
    else:
        print(result_text)
        choice = input("\n以上の内容で実行してよろしいでしょうか？ [y/N]: ").lower()

    if choice in ['y', 'ye', 'yes']:

        ## rename proc
        inter_ll = []
        for i in range(len(before_path_list)):
            _before = before_path_list[i]
            _after = after_path_list[i]

            # _afterがbeforelistにある時、中間体を経由する
            if _after in before_path_list:
                inter = _after.with_stem(f"_{_after.stem}")
                while inter.exists():
                    inter = inter.with_stem(f"_{inter.stem}")
                inter_ll.append([copy.copy(inter),copy.copy(_after)])
                _after = copy.copy(inter)

            if _after.exists():
                print('error! file is existed!')
                continue

            shutil.move(_before, _after)
            print(f'\r"{_before.name}" >> "{_after.name}"',end='')
        if inter_ll:
            print("\n\n## inter to after")
            for inter_l in inter_ll:
                _before, _after = inter_l
                shutil.move(_before, _after)
                print(f'\r"{_before.name}" >> "{_after.name}"',end='')
        print()
        logcsv_proc(before_path_list, after_path_list, log_csvfile)

    else:
        print("実行しませんでした。")
        exit()
    



def get_before_path_list(argv_path_list, mode):
    if mode == 'date':
        argv_path_list.sort(key=os.path.getmtime, reverse=True)
        before_path_list = argv_path_list
    elif mode == 'dir':
        dir_l = natsort.natsorted([f for f in argv_path_list if f.is_dir()])
        file_l = natsort.natsorted([f for f in argv_path_list if f.is_file()])
        before_path_list = dir_l + file_l
    else:
        before_path_list = argv_path_list
        
    return before_path_list



def get_after_name_list(before_path_list, editor):
    ## get name_list
    before_name_list = []
    for _before in before_path_list:
        name = _before.name
        if _before.is_dir():
            name = name + '/'
        before_name_list.append(name)

    ## vim get after_name_list
    with tempfile.TemporaryDirectory() as dname:
        tempdir = pathlib.Path(dname)
        after_text = tempdir/'after_text.txt'

        with open(after_text, 'w') as f:
            f.write('\n'.join([str(f) for f in before_name_list]))

        cmd = f"{editor} {after_text}"
        proc = subprocess.run(cmd, shell=True)

        with open(after_text) as f:
            after_name_list = [s.strip() for s in f.readlines()]
        after_name_list = [pathlib.Path(f).name for f in after_name_list]
        after_name_list = [s.rstrip('/') for s in after_name_list]
        if not after_name_list == []:
            homedir = pathlib.Path.home()
            log_txtfile = homedir/'.vrename-log.txt'
            with open(after_text) as f:
                _txt = f.read()
            with open(log_txtfile,'w') as f:
                f.write(_txt)
            print("saved log-txt")

    return after_name_list



def name_repair(name):
    name = name.replace('[','').replace(']','')
    ## タイトルに使えない文字の排除
    for i in '\\' , '\"' , '\'' , '/' , ':' , '*' , '?' , '<' , '>' , '|' , '[' , ']' , ' ' , '　':
        name = name.replace(i,'_')
    while '__' in name:
        name = name.replace('__','_')
    while '_-_' in name:
        name = name.replace('_-_','-')
    return name



def logcsv_proc(before_path_list, after_path_list, log_csvfile):
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    result_l = []
    for _b,_a in zip(before_path_list, after_path_list):
        _txt = timestamp + ',' + str(_a.resolve().parent)  + ',' + str(_b.name) + ',' + str(_a.name)
        result_l.append(_txt)
    result_txt = '\n'.join(result_l)
    if os.path.exists(f"{log_csvfile}"):
        with open(f"{log_csvfile}") as f:
            _txt = f.read()
    result_txt = result_txt + '\n' + _txt.rstrip()
    with open(f"{log_csvfile}",'w') as f:
        f.write(result_txt)
    print("saved log-csv")



def get_restore_proc(log_csvfile, timestamp):
    with open(log_csvfile) as f:
        text_l = [s.strip() for s in f.readlines()] 
    if not timestamp:
        timestamp = text_l[0].split(',')[0]
    text_l = [s for s in text_l if s.startswith(timestamp)]
    before_path_list, after_name_list = [],[]
    for text in text_l:
        _,_dir,after,before = text.split(',')
        if pathlib.Path(_dir, before).exists():
            before_path_list.append(pathlib.Path(_dir)/before)
            after_name_list.append(after)

    ## before_listが重複していた場合
    while [k for k, v in collections.Counter(before_path_list).items() if v > 1]:
        dup_path = [k for k, v in collections.Counter(before_path_list).items() if v > 1][0]
        dup_index = [i for i, x in enumerate(before_path_list) if x == dup_path][1:]
        for i in dup_index:
            del before_path_list[i]
            del after_name_list[i]

    return before_path_list, after_name_list
        

main()
