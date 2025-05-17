#!/usr/bin/env bash

pacages=(
    "noto-fonts"
    "noto-fonts-cjk"
    "noto-fonts-emoji"
    "noto-fonts-extra"
    "ttf-droid"
    "ttf-dejavu"
    "otf-ipafont"
    )

result="$(IFS=" "; echo "${pacages[*]}")"
sudo pacman -S $result
