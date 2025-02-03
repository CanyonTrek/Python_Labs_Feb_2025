#! /usr/bin/env python
# Author: BersuitX
# Version: 1.0
# Description: This is oir first script

name = input("Enter your name: ")
number = input("Enter the number : ")

print("My name is", name)
print("My name is " + name)
print("The number is: ", type(number))

import random
print("Lucky number is", random.randint(1, 50))

from math import cos
print("Cosine of 0.5 is", cos(0.5))


