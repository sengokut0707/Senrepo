#!/usr/bin/env bash

str="$(IFS=+; echo "$*")"
xdg-open "https://www.google.com/search?q=${str}" 1>/dev/null 2>/dev/null &
