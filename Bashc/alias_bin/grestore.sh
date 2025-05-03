#!/usr/bin/env bash

for f in $@; do
    c=`git rev-list -n 1 HEAD -- $f`
    if [ -n "$c" ];then
        git checkout "$c"^ -- "$f"
        git restore --staged "$f"
        echo "$f restored"
    fi
done
