#!/usr/bin/env bash

sudo pacman -Rns $(pacman -Qtdq)
yay -Sc
