#!/usr/bin/env python3
import base64
import subprocess
import argparse

# 内部に埋め込んだIR信号データ
IR_DATA = {
    'light1': {
        'on':   'JgBoAAABJ5MTEhMSExITExMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExMSExITEhMSExITEhMSExMSExM3EwAFHgABJkkSAA0FAAAAAAAAAAA=',
        'off':  'JgBoAAABKZMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExMSEzYTAAXoAAEmSRMAA0FAAAAAAAAAAA=',
        'mini': 'JgBoAAABKJQTEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExM2EwAF6AABJkkTAA0FAAAAAAAAAAA=',
    },
    'light2': {
        'on':   'JgBoAAABJ5MTExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhM2EwAF6AABJkkSAA0FAAAAAAAAAAA=',
        'off':  'JgBoAAABKZMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExMSEzYTAAXnAAEmSRMAA0FAAAAAAAAAAA=',
        'mini': 'JgBoAAABKJQTEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExITEhMSExM2EwAF5gABJkkTAA0FAAAAAAAAAAA=',
    }
}

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--light', default='12', choices=['1', '2', '12'])
    parser.add_argument('-m', '--mode', default='on', choices=['on', 'off', 'mini'])
    return parser.parse_args()

def generate_ir_signal(light, mode):
    return IR_DATA[light][mode]

def main():
    args = get_args()
    mode = args.mode
    light = args.light

    if light == '1':
        light_list = ['light1']
    elif light == '2':
        light_list = ['light2']
    else:
        light_list = ['light1', 'light2']

    for light in light_list:
        b64 = generate_ir_signal(light, mode)
        decoded = base64.b64decode(b64).decode('latin1')
        subprocess.run(['/usr/local/bin/bto_advanced_USBIR_cmd', '-d', decoded])
        print(f"{light}:{mode}")

if __name__ == '__main__':
    main()
