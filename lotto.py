#! /usr/bin/env python3
# Author: Brad
# version: 1.0
# Description: lotto Script Info

"""
"""
import random
lotto = [] # create an empty list

while len(lotto) < 6:
    num = random.randit( 1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number: ", num
print("Lottery numbers =", lotto