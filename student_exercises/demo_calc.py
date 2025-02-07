#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Calculator app with add, multiply and divide functions
"""


def add(x, z):
    return float(x+z)

def mul(x, z):
    return float(x*z)

def div(x, z):
    return round(x/z, 3)

print(f"4 + 3 = {add(4, 3)}")
print(f"4 + 3 = {mul(4, 3)}")
print(f"4 + 3 = {div(4, 3)}")

l_add = lambda x, z:float(x+z)
print(f"4 + 3 = {l_add(4, 3)}")