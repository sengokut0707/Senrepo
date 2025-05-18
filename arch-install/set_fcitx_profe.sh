#!/usr/bin/env bash

file1=~/.config/environment.d/envvars.conf
file2=~/.xprofile

mkdir -p ~/.config/environment.d/

cat <<EOH | tee $file1 $file2
export INPUT_METHOD=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
export SDL_IM_MODULE=fcitx
export GLFW_IM_MODULE=fcitx
EOH
