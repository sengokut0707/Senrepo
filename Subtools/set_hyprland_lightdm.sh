#!/bin/bash

# Hyprlandセッションファイルを作成
sudo tee /usr/share/xsessions/hyprland.desktop > /dev/null <<'EOF'
[Desktop Entry]
Name=Hyprland
Comment=Wayland window manager
Exec=Hyprland
Type=Application
DesktopNames=Hyprland
EOF

sudo sed -i 's/^autologin-session=.*$/autologin-session=Hyprland/' /etc/lightdm/lightdm.conf


echo "Hyprland セッションファイルを作成しました。"
