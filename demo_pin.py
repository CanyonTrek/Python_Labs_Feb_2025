#! /usr/bin/env python3
# Author: Brad
# version: 1.0
# Description: the script will simulate a high street bank pin machine.
#Max 3 attempts!

"""
DocString
"""

import getpass



master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts <3:
    pin = getpass.getpass("Enter PIN: ")
    if pin ==master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts +=1

else:
    # Executes only once when conditions False.
    print("Too many attempts")
    print("Your card has been retained. Have a nice day!")

print("Done. ")