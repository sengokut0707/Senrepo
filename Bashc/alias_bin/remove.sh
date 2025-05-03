#!/usr/bin/env bash

type trash-put > /dev/null 2>&1
if [ $? -eq 0 ] ; then
    trash-put -v $@
else
#    /usr/bin/rm -v $@
    echo "!!! error !!!\nplease install trash-cli or use rmf"
fi

