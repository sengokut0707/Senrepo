#!/bin/bash

sudo sed -i 's/^autologin-session=.*$/autologin-session=sway/' /etc/lightdm/lightdm.conf
