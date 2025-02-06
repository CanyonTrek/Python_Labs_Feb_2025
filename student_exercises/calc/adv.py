#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does advance calculator functions
"""
    Docstring: Includes mod, power, and sqrt
"""

import sys

def mod(x, z):
    """ return Remainder of x divided by z """
    return x % z

def power(x, z):
    """ Return power of x to z """
    return x**z

def sqrt(x):
    """ Return square root of x"""
    return round(x**0.5, 2)

def main():
    print("Advanced Calculator App")
    print("-" * 30)
    print(f"100 % 30 = {mod(100, 30)}")
    print(f"100 ** 3 = {power(100, 3)}")
    print(f"\N{square root}100 = {sqrt(100)}")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
