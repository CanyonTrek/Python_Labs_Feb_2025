#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will simulate
# a high street bank ATM pin machine
"""
    Docstring:
"""
master_pin = "0123"
pin = None
attempts = 0

# loop whilst pin is incorrect
while pin!=master_pin and attempts < 3:
    pin = input("Enter pin: ")
    if pin==master_pin:
        print("valid pin")
    else:
        attempts+=1
        print("invalid pin")

if attempts==3:
    print("tried too many times, call your bank")

print("done.")