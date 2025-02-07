#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""
import sys

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

def mul(*args):
    total = 1
    for num in args:
        total *= num
    return total

def div(x, y):
    return round(x/y, 3)

def main():
    print("Basic Calculator App")
    print(f"4 + 3 = {add(4,3)}")
    print(f"4 + 3 + 2 = {add(4,3,2)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 * 3 * 2 = {mul(4,3,2)}")
    print(f"4 / 3 = {div(4,3)}")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
