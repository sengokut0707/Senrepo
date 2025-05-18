#!/usr/bin/env python3

import subprocess
import argparse

def get_args():
    description = 'デフォルトアプリを設定します。'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-s','--set_app',action='store_true')
    parser.add_argument('-b','--browser',nargs='*')
    parser.add_argument('-p','--pdf_viewer',nargs='*')
    parser.add_argument('-f','--file_manager',nargs='*')
    parser.add_argument('-i','--image_viewer',nargs='*')
    parser.add_argument('-t','--text_editor',nargs='*')
    parser.add_argument('-m','--media_player',nargs='*')
    parser.add_argument('-a','--audio_player',nargs='*')
    return parser.parse_args()


def get_types_dict():
    types_dict = {
      'browser':['x-scheme-handler/http','x-scheme-handler/https','text/html'],
      'pdf_viewer':['application/pdf'],
      'file_manager':['inode/directory'],
      'image_viewer':['image/jpeg','image/png'],
      'text_editor':['text/plain'],
      'media_player':['video/mp4','video/webm','video/avi'],
      'audio_player':['audio/mpeg','audio/x-wav']
    }
    return types_dict


def main_proc():
    args = get_args()
    types_dict = get_types_dict()

    set_app = args.set_app

    browser = args.browser
    pdf_viewer = args.pdf_viewer
    file_manager = args.file_manager
    image_viewer = args.image_viewer
    text_editor = args.text_editor
    media_player = args.media_player
    audio_player = args.audio_player

    app = ''
    if browser != None:
        app = browser
        types_list = types_dict.get('browser')
    elif pdf_viewer != None:
        app = pdf_viewer
        types_list = types_dict.get('pdf_viewer')
    elif file_manager != None:
        app = file_manager
        types_list = types_dict.get('file_manager')
    elif image_viewer != None:
        app = image_viewer
        types_list = types_dict.get('image_viewer')
    elif text_editor != None:
        app = text_editor 
        types_list = types_dict.get('text_editor')
    elif media_player != None:
        app = media_player
        types_list = types_dict.get('media_player')
    elif audio_player != None:
        app = audio_player
        types_list = types_dict.get('audio_player')

    if app != '':
        if set_app:
            set_default_app(app[0],types_list)
        get_default_app(types_list[0])


def main():
    main_proc()


def set_default_app(app,types_list):
    for type in types_list:
        command = 'xdg-mime default {}.desktop {}'.format(app,type)
        proc = subprocess.run(command,shell=True)
        print(proc)


def get_default_app(type):
    command = "xdg-mime query default {} | sed 's/.desktop//g'".format(type)
    proc = subprocess.run(command,shell=True)


if __name__ == '__main__':
    main()
    #browser = 'vivaldi-stable'
    #pdf_viewer = 'xpdf','llpp','foxitreader'
    #file_manager = 'thunar'
    #image_viewer = 'viewnior'
    #text_editor = 'leafpad'
    #media_player = 'mpv'
    #audio_player = 'audacious'

