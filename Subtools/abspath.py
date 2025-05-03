#!/usr/bin/env python3
import os,sys

argv = sys.argv[1:]
for file in argv:
    path = os.path.abspath(file)
    print(path)
