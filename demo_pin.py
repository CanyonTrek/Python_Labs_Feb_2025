#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will simulate
# a high street bank ATM pin machine
"""
    Docstring:
"""
master_pin = "0123"
pin = None

# loop whilst pin is incorrect
while pin!=master_pin:
    pin = input("Enter pin: ")
    if pin==master_pin:
        print("valid pin")
    else:
        print("invalid pin")

print("done.")