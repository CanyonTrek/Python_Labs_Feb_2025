#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""

def get_numbers():
    """return list of numbers"""
    numbers=[]
    for x in range(0,10):
        numbers.append(x)
    return numbers

for z in get_numbers():
    print(z)
