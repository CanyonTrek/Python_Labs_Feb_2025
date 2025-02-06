#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""
import sys

def add(*args):
    total = 0
    for n in args:
        total += n
    return total

def mul(*args):
    total = 1
    for n in args:
        total *= n
    return total

def dev(x, z):
    return round(x/z, 3)

print("Basic Calc app")
print(f"4 + 2 = {add(4,2)}")
print(f"4 + 2 + 3 = {add(4,2,3)}")
print(f"4 x 2 x 3 = {mul(4,2,3)}")
print(f"4 / 3  = {dev(4,3)}")

sys.exit(0)

