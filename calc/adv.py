#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""

import sys

def mod(x, z):
    return x % z

def power(x, z):
    return x**z

def sqrt(x):
    return round(x**0.5, 2)

def main():
    print("Adv Calc app")
    print(f"100 mod 30 = {mod(100,30)}")
    print(f"100^30 = {power(100,30)}")
    print(f"\N{square root} 100  = {sqrt(100)}")
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
