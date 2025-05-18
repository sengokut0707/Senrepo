#!/usr/bin/env bash

git clone https://github.com/seebi/dircolors-solarized.git ~/.dircolors-solarized
eval `dircolors ~/.dircolors-solarized/dircolors.256dark`



mkdir -p .temp_dir
cd ./.temp_dir

git clone https://github.com/altercation/vim-colors-solarized.git &&
mkdir -p ~/.vim/colors &&
cp -vr ./vim-colors-solarized/colors/solarized.vim ~/.vim/colors/

echo "以下の内容を~/.vimrcに記述してください。"
echo """\
syntax enable
set background=dark
colorscheme solarized
"""



cd ..
rm -rf ./.temp_dir
