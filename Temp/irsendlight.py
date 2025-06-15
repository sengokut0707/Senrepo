#!/usr/bin/env python3
import base64
import subprocess
import os, pathlib
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--light', default='12', choices = ['1','2','12'])
    parser.add_argument('-m','--mode', default='on', choices = ['on','off','mini'])
    return parser.parse_args()

def main():
    args = get_args()
    mode = args.mode
    light = args.light

    if light == '1':
        light_list = ['light1']
    elif light == '2':
        light_list = ['light2']
    else:
        light_list = ['light1','light2']

    for light in light_list:
        b64 = generate_ir_signal(light, mode)
        proc = subprocess.run(['/usr/local/bin/bto_advanced_USBIR_cmd','-d',base64.b64decode(b64).decode("latin1")])
        print(f"{light}:{mode}")


# 共通部分（lighton1 などの後半部分）をあらかじめデコードして取り出しておく
COMMON_PARTS = {
    'on': base64.b64decode(
        "MHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4"
        "MTUsMHgwMCwweDE4LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAw"
        "LDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAw"
        "LDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAw"
        "LDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAw"
        "LDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxOCwweDAw"
        "LDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAw"
        "LDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAw"
        "LDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAw"
        "LDB4NDAsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAw"
        "LDB4NDAsMHgwMCwweDE3LDB4MDYsMHgxOQ=="
    ),
    'off': base64.b64decode(
        "MHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4MTUs"
        "MHgwMCwweDE4LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4MTUs"
        "MHgwMCwweDE4LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4NDAs"
        "MHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTgsMHgwMCwweDE1LDB4MDAsMHgxNywweDAwLDB4NDAs"
        "MHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTgsMHgwMCwweDE1LDB4MDAsMHgxNywweDAwLDB4NDAs"
        "MHgwMCwweDE4LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE1LDB4MDAsMHgxNywweDAwLDB4MTYs"
        "MHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4NDAs"
        "MHgwMCwweDE4LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4MTUs"
        "MHgwMCwweDE4LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4MTYs"
        "MHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4MTYs"
        "MHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxOCwweDAwLDB4MTUs"
        "MHgwMCwweDE3LDB4MDYsMHgxYQ=="
    ),
    'mini': base64.b64decode(
        "MHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4MTUs"
        "MHgwMCwweDE4LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4NDAs"
        "MHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4NDAs"
        "MHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4NDAs"
        "MHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4MTYs"
        "MHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxOCwweDAwLDB4NDAs"
        "MHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4MTYs"
        "MHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4NDAs"
        "MHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4MTUs"
        "MHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4MTYs"
        "MHgwMCwweDE3LDB4MDYsMHgxOQ=="
    )
}

# 各ライトとモードに応じた先頭バイト
PREFIXES = {
    'light1': {
        'on':   [0x01, 0x58],
        'off':  [0x01, 0x59],
        'mini': [0x01, 0x59]
    },
    'light2': {
        'on':   [0x01, 0x59],
        'off':  [0x01, 0x59],
        'mini': [0x01, 0x59]
    }
}

def generate_ir_signal(light: str, mode: str) -> str:
    if light not in PREFIXES:
        raise ValueError("light must be 'light1' or 'light2'")
    if mode not in COMMON_PARTS:
        raise ValueError("mode must be 'on', 'off', or 'mini'")

    prefix = PREFIXES[light][mode]
    body = COMMON_PARTS[mode]
    signal_bytes = bytes(prefix) + body
    return base64.b64encode(signal_bytes).decode()





if __name__ == "__main__":
    main()
