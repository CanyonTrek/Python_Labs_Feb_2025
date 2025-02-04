#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will generate 6 random lottery numbers
"""
    Docstring:
"""
import random

lotto = []


while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("duplicate number =", num)


print("lottery number =", lotto)
