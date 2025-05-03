#!/bin/bash

sudo sed -i 's/^autologin-session=.*$/autologin-session=i3/' /etc/lightdm/lightdm.conf
