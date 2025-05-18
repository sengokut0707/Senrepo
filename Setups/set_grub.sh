#!/usr/bin/env bash

sudo cp -vu /etc/default/grub /etc/default/grub_old
sudo sed -i 's/^GRUB_TIMEOUT=.*/GRUB_TIMEOUT=0/g' /etc/default/grub
sudo sed -i 's/^GRUB_CMDLINE_LINUX_DEFAULT=.*/GRUB_CMDLINE_LINUX_DEFAULT=\"acpi_backlight=video acpi_osi=!\"/g' /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg
echo "plaese '$ yay -S update-grub && sudo update-grub'"
