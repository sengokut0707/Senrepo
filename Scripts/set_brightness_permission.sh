#!/usr/bin/env bash


DIR="/sys/class/backlight/acpi_video0"
if [ -e $DIR ]; then
    :
else
    DIR="/sys/class/backlight/intel_backlight"
fi

sudo systemctl disable allow_brightness.service
sudo rm -rf /etc/systemd/system/allow_brightness.service 
sudo tee /etc/systemd/system/allow_brightness.service <<EOF >/dev/null
[Unit]
Description=allow_brightness daemon

[Service]
Type=oneshot
ExecStart=bash -c 'sleep 5 ; chmod 666 $DIR/brightness'

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable allow_brightness.service

echo "enable allow_brightness.service"
