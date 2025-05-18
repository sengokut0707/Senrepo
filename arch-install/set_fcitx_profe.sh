#!/usr/bin/env bash

text="/
export INPUT_METHOD=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
export SDL_IM_MODULE=fcitx
export GLFW_IM_MODULE=fcitx
"
text=$(echo "$text" | xargs)

mkdir -p ~/.config/environment.d/
echo $text > ~/.config/environment.d/envvars.conf
echo $text > ~/.xprofile

