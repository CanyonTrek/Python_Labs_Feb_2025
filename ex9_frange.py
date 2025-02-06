#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""

def frange(vstart, vstop, vstep=1):

    if vstep==0:
        print(f"step supplied is 0, not valid, replaced with 1")
        vstep=1

    i = vstart
    #yield i
    while i < vstop:
        yield i
        i += vstep


print(list(frange(1.1,5.0,1)))
print(list(frange(-1,-.5,0.1)))
print(list(frange(1,3,1)))
print(list(frange(3,1)))
print(list(frange(1,2)))
