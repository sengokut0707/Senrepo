#!/usr/bin/env python3
import base64
import subprocess
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--light', default='light12', choices=['light1', 'light2', 'light12'])
    parser.add_argument('-m', '--mode', default='on', choices=['on', 'off', 'mini'])
    return parser.parse_args()


def main():
    args = get_args()
    mode = args.mode
    light = args.light

    if light == 'light12':
        light_list = ['light1', 'light2']
    else:
        light_list = [light]

    for light in light_list:
        b64 = IR_DATA[light][mode]
        decoded = base64.b64decode(b64).decode('latin1')
        subprocess.run(['/usr/local/bin/bto_advanced_USBIR_cmd', '-d', decoded])
        print(f"{light}:{mode}")

IR_DATA = {
    'light1': {
        'on':
            "MHgwMSwweDU4LDB4MDAsMHhhYywweDAwLDB4MTcsMHgwMCwweDE1LDB4MDAsMHgxNywweDAwLDB4"
            "NDAsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAw"
            "LDB4MTUsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNyww"
            "eDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgx"
            "NywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAs"
            "MHgxNywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4"
            "MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDQw"
            "LDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCww"
            "eDQxLDB4MDAsMHgxNywweDAwLDB4MTUsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTgsMHgw"
            "MCwweDQwLDB4MDAsMHgxNywweDAwLDB4MTUsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcs"
            "MHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4NDAsMHgwMCwweDE4LDB4MDAsMHgxNSwweDAwLDB4"
            "MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDYsMHgxOQ=="
            ,
        'off':
            "MHgwMSwweDU5LDB4MDAsMHhhYiwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4"
            "NDAsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTgsMHgwMCwweDE1LDB4MDAsMHgxNywweDAw"
            "LDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTgsMHgwMCwweDE1LDB4MDAsMHgxNyww"
            "eDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTgsMHgwMCwweDE1LDB4MDAsMHgx"
            "NywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTgsMHgwMCwweDE1LDB4MDAs"
            "MHgxNywweDAwLDB4NDAsMHgwMCwweDE4LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE1LDB4"
            "MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDQw"
            "LDB4MDAsMHgxNywweDAwLDB4NDAsMHgwMCwweDE4LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCww"
            "eDQwLDB4MDAsMHgxNywweDAwLDB4MTUsMHgwMCwweDE4LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgw"
            "MCwweDQwLDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcs"
            "MHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4"
            "MTcsMHgwMCwweDQwLDB4MDAsMHgxOCwweDAwLDB4MTUsMHgwMCwweDE3LDB4MDYsMHgxYQ=="
            ,
        'mini':
            "MHgwMSwweDU5LDB4MDAsMHhhYiwweDAwLDB4MTcsMHgwMCwweDE1LDB4MDAsMHgxNywweDAwLDB4"
            "NDEsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAw"
            "LDB4MTUsMHgwMCwweDE4LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNyww"
            "eDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgx"
            "NywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAs"
            "MHgxNywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4"
            "MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDQw"
            "LDB4MDAsMHgxOCwweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCww"
            "eDQwLDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgw"
            "MCwweDQwLDB4MDAsMHgxNywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcs"
            "MHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4MTUsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4"
            "MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDYsMHgxOQ=="
    },
    'light2': {
        'on':
            "MHgwMSwweDU5LDB4MDAsMHhhYiwweDAwLDB4MTcsMHgwMCwweDE1LDB4MDAsMHgxNywweDAwLDB4"
            "NDAsMHgwMCwweDE4LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAw"
            "LDB4MTUsMHgwMCwweDE4LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNyww"
            "eDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgx"
            "NywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAs"
            "MHgxNywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MSwweDAwLDB4MTcsMHgwMCwweDE1LDB4"
            "MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDQw"
            "LDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCww"
            "eDQwLDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgw"
            "MCwweDQwLDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcs"
            "MHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4"
            "MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDYsMHgxYg=="
            ,
        'off':
            "MHgwMSwweDU5LDB4MDAsMHhhYiwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4"
            "NDAsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAw"
            "LDB4MTUsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNyww"
            "eDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgx"
            "NywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAs"
            "MHgxNywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTgsMHgwMCwweDE1LDB4"
            "MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDQw"
            "LDB4MDAsMHgxNywweDAwLDB4NDAsMHgwMCwweDE4LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCww"
            "eDQwLDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgw"
            "MCwweDQxLDB4MDAsMHgxNywweDAwLDB4MTUsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcs"
            "MHgwMCwweDE1LDB4MDAsMHgxOCwweDAwLDB4MTUsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4"
            "MTcsMHgwMCwweDQwLDB4MDAsMHgxNywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDYsMHgxYg=="
            ,
        'mini':
            "MHgwMSwweDU5LDB4MDAsMHhhYSwweDAwLDB4MTcsMHgwMCwweDE1LDB4MDAsMHgxNywweDAwLDB4"
            "NDEsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNywweDAw"
            "LDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgxNyww"
            "eDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE2LDB4MDAsMHgx"
            "NywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MSwweDAwLDB4MTcsMHgwMCwweDE1LDB4MDAs"
            "MHgxNywweDAwLDB4NDEsMHgwMCwweDE3LDB4MDAsMHg0MCwweDAwLDB4MTcsMHgwMCwweDE1LDB4"
            "MDAsMHgxOCwweDAwLDB4MTUsMHgwMCwweDE3LDB4MDAsMHgxNiwweDAwLDB4MTcsMHgwMCwweDQw"
            "LDB4MDAsMHgxNywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDAsMHg0MSwweDAwLDB4MTcsMHgwMCww"
            "eDQwLDB4MDAsMHgxNywweDAwLDB4MTUsMHgwMCwweDE4LDB4MDAsMHgxNSwweDAwLDB4MTcsMHgw"
            "MCwweDQwLDB4MDAsMHgxNywweDAwLDB4NDEsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4MTcs"
            "MHgwMCwweDE2LDB4MDAsMHgxNywweDAwLDB4MTYsMHgwMCwweDE3LDB4MDAsMHgxNSwweDAwLDB4"
            "MTcsMHgwMCwweDQxLDB4MDAsMHgxNywweDAwLDB4NDAsMHgwMCwweDE3LDB4MDYsMHgxYg=="
    }
}

if __name__ == '__main__':
    main()
