#!/usr/bin/env bash

function gitf_proc () {
    echo "--- $(basename `pwd`) ---"
    if git branch | grep master -q && git status | grep 'working tree clean' -q ; then
        git pull --rebase
    else
        echo '### SKIP ###'
        git branch
        git status -s
    fi
}

#if [ -d ./.git ]; then
#    gitf_proc
#
#else
    currentdir=`pwd`
    cd ~/*Git_dir

    for i in `ls` ;do
        cd $i
        gitf_proc
        echo
        cd ../ 
    done

    cd $currentdir
#fi
