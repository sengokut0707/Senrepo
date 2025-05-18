#!/usr/bin/env bash

wasd_change="\
clear lock
keycode  66 = Shift_L NoSymbol Shift_L

keycode  25 = Up    w w W
keycode  38 = Left  a a A
keycode  39 = Down  s s S
keycode  40 = Right d d D

keycode  31 = Up    i i I
keycode  44 = Left  j j J
keycode  45 = Down  k k K
keycode  46 = Right l l L
"

wasd_defalt="\
clear lock
keycode  66 = Shift_L NoSymbol Shift_L

keycode  25 = w W w W
keycode  38 = a A a A
keycode  39 = s S s S
keycode  40 = d D d D

keycode  31 = i I i I
keycode  44 = j J j J
keycode  45 = k K k K
keycode  46 = l L l L
"

if grep "keycode  25 = Up" ~/.Xmodmap_wasd > /dev/null; then
    echo "$wasd_defalt" > ~/.Xmodmap_wasd
    echo "wasd,ijklキーをデフォルトに戻します"
else
    echo "$wasd_change" > ~/.Xmodmap_wasd
    echo "wasd,ijklを矢印キーに変更"
fi

xmodmap ~/.Xmodmap_wasd
