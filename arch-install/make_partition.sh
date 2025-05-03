#!/usr/bin/env bash

#ls /sys/firmware/efi/
#lsblk

wipefs -a /dev/sda
sgdisk --zap-all /dev/sda

sgdisk -n 1:0:+1G   -t 1:ef00 -c 1:"BOOT_DISK" /dev/sda
sgdisk -n 2:0:+30G  -t 2:8300 -c 2:"ROOT_DISK" /dev/sda
sgdisk -n 3:0:0     -t 3:8300 -c 3:"HOME_DISK" /dev/sda

partprobe /dev/sda
sleep 2

# 各パーティションをフォーマット
mkfs.fat -F32 -n BOOT_DISK "/dev/sda1"
mkfs.ext4     -L ROOT_DISK "/dev/sda2"
mkfs.ext4     -L HOME_DISK "/dev/sda3"

partprobe /dev/sda
sleep 2

lsblk -f /dev/sda
