#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""
import sys
import basic
import adv

def main():
    menu = """
        calculator app
        --------------
        1. test basic
        2. test adv
    """

    print(menu)
    option = input("choose 1 or 2:")
    if option == "1":
        print (f"100 + 40 + 10 = {basic.add(100,40,10)}")
        print(f"100 + 40 + 10 = {basic.mul(100, 40, 10)}")
    elif option == "2":
        print(f"mod of 100 by 45 = {adv.mod(100, 45)}")
    else:
        print("invalid choice")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)

