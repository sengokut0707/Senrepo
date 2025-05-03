#!/usr/bin/env bash

#RDIR=/mnt/remote_server
RDIR=/home/Storage
sudo mkdir -p -m 777 $RDIR
sshfs sengokut0707@deskmini1974.ddns.net:$RDIR $RDIR -p 1974 -o IdentityFile=~/.ssh/id_rsa && echo "mount \"Raspi\" >> \"$RDIR\""
echo ''
read -p "please Enter to umount \"$RDIR\": "
sudo umount $RDIR && sudo rm -r $RDIR && echo "umount \"$RDIR\""
