#!/usr/bin/env bash

function gitf_proc () {
    echo "--- $(basename `pwd`) ---"
    git remote set-url origin Raspi:/home/Git_dir.git/$(basename `pwd`)
}

currentdir=`pwd`
cd ~/*Git_dir

for i in `ls` ;do
    cd $i
    gitf_proc
    echo
    cd ../ 
done

cd $currentdir
