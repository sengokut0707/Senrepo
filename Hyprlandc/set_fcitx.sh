#!/bin/bash
sudo tee /etc/environment > /dev/null <<EOF
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
EOF
