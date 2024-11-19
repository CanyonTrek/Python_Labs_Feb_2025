#! /usr/bin/env python3
# Author: Brad
# version: 1.0
# Description: the script will simulate a high street bank pin machine.


"""
DocString
"""

master_pin = "0123"
pin = None

while pin != master_pin:
    pin = input("Enter PIN: ")
    if pin ==master_pin:
        print("Valid PIN")
    else:
        print("Invalid PIN")


print("Done. ")