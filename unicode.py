#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""
for pos in range(0,65536):
    try:
        #print(pos,chr(pos))
        print(chr(pos), end=" ")
        if pos % 16 ==0:
            print()
    except UnicodeEncodeError:
        print(" ")