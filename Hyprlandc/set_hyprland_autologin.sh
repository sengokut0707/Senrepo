#!/usr/bin/env bash

sudo cp /usr/lib/systemd/system/getty@.service /usr/lib/systemd/system/autologin@.service

sudo sed -i 's/^ExecStart=-\/sbin\/agetty.*$/ExecStart=-\/sbin\/agetty --noclear -a sengokut0707 %I 38400 linux/' /usr/lib/systemd/system/autologin@.service

sudo systemctl disable lightdm
sudo systemctl disable getty@tty1
sudo systemctl enable autologin@tty1


cat > ~/.bash_profile << 'EOF'
if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then
  exec Hyprland
fi

source ~/.bashrc
EOF

