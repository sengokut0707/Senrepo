#!/usr/bin/bash


mkdir /mnt/root

mount "/dev/disk/by-label/ROOT_DISK" /mnt/root
mkdir /mnt/root/boot
mkdir /mnt/root/home
mount "/dev/disk/by-label/BOOT_DISK" /mnt/root/boot
mount "/dev/disk/by-label/HOME_DISK" /mnt/root/home

pacman -Sy archlinux-keyring
pacstrap -K /mnt/root linux linux-firmware base base-devel dhcpcd linux-headers

genfstab -U /mnt/root >> /mnt/root/etc/fstab
