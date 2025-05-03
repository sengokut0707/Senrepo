#!/usr/bin/bash


#mkdir /mnt/root
#
#mount "/dev/disk/by-label/root_disk" /mnt/root
#mount "/dev/disk/by-label/boot_disk" /mnt/root/boot
#mount "/dev/disk/by-label/home_disk" /mnt/root/home
#
pacman -Sy archlinux-keyring
pacstrap -K /mnt/root linux linux-firmware base base-devel dhcpcd linux-headers

#genfstab -U /mnt/root >> /mnt/root/etc/fstab
