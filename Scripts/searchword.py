#!/usr/bin/env python3

import os, sys, glob, pathlib
import argparse
import mimetypes


def get_args():
    parser = argparse.ArgumentParser(description='テキストファイルに対して文字列検索をします。行番号と行の中身を返します。')
    parser.add_argument('args_list', nargs='*', default='[.]', help='テキストファイルを指定します。ディレクトリも可')
    parser.add_argument('-R','--recursive_flag',action='store_true',help='再帰的に検索する。')
    parser.add_argument('-w','--word',type=str,required=True,help='キーワードを指定します。')
    parser.add_argument('-r','--replace',type=str,help='キーワードを検索後、全置換します。')
    parser.add_argument('-n','--name_only',action='store_true',help='ファイル名のみ出力します。')
    parser.add_argument('-p','--path_only',action='store_true',help='ファイルパスのみ出力します。')
    parser.add_argument('-i','--inverted',action='store_true',help='検索結果を逆転させます。')
    return parser.parse_args()



def main():
    args = get_args()
    args_list = args.args_list
    recursive_flag = args.recursive_flag
    key_word = args.word
    replace = args.replace
    name_only_flag = args.name_only
    path_only_flag = args.path_only
    inverted_flag = args.inverted

    file_list = get_file_list(args_list, recursive_flag)
    text_file_list = get_text_file_list(file_list)
    result_file_list = get_result_file_list(text_file_list, key_word)

    if inverted_flag:
        result_file_list = sorted(list(set(text_file_list) - set(result_file_list)))

    result_text = get_result_text(result_file_list, key_word, replace, name_only_flag, path_only_flag)
    print(result_text)

    if replace:
        replace_proc(result_file_list, key_word, replace)



def get_file_list(args_list, recursive_flag):
    file_list = []
    for args in args_list:
        if os.path.isfile(args):
            file_list.append(args)
        elif os.path.isdir(args):
            find_list = glob.glob(f"{str(pathlib.Path(args))}/**", recursive=recursive_flag)
            file_list += [f for f in find_list if os.path.isfile(f)]
    return file_list



def get_text_file_list(file_list):
    text_file_list = [f for f in file_list if is_text_file(f)]
    text_file_list = sorted(text_file_list)
    return text_file_list



def get_result_file_list(text_file_list, key_word):
    result_list = []
    for text_file in text_file_list:
        try:
            with open(text_file) as f:
                text = f.read()
            if key_word in text:
                result_list.append(text_file)
        except:
            print(f"error! {text_file}")
    return result_list



def get_result_text(result_file_list, key_word, replace, name_only_flag, path_only_flag):
    result_list = []

    if name_only_flag:
        for result_file in result_file_list:
            result_list.append(os.path.basename(result_file))
        result_text = '\n'.join(result_list)
        return result_text

    if path_only_flag:
        for result_file in result_file_list:
            result_list.append(os.path.abspath(result_file))
        result_text = '\n'.join(result_list)
        return result_text
        
    for result_file in result_file_list:
        result_list.append(f"=== {os.path.basename(pathlib.Path(result_file).resolve().parent)}/" + f"{os.path.basename(result_file)} ===")
        with open(result_file) as f:
            lines_base = f.readlines()
        lines = [i.strip() for i in lines_base]
        i_line_list = [(i+1,line) for i,line in enumerate(lines) if str(key_word) in line]

        for [i,line] in i_line_list:
            result_list.append(f"{i}行 :{line}")
        result_list.append("")

        if replace:
            result_list.append("--- ↓After↓ ---")
            for [i,line] in i_line_list:
                result_list.append(f"{i}行 :{line.replace(key_word,replace)}")
            result_list.append("\n\n")
    result_text = '\n'.join(result_list)
    return result_text



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



def replace_proc(text_file_list, key_word, replace):
    print('上記の内容で上書きします。よろしいですか？')
    choice = ''
    choice = input("Please respond with 'yes' or 'no' [y/N]: ")
    if choice in ['y', 'ye', 'yes']:
        for text_file in text_file_list:
            with open(text_file) as f:
                text = f.read()
            text = text.replace(key_word,replace)
            with open(text_file,'w') as f:
                f.write(text)
        print('置換が終了しました。')
    else:
        print('上書きしませんでした。')
        sys.exit()



if __name__ == '__main__':
    main()
