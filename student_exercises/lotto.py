#! /usr/bin/python
# Author: BersuitX
# Description: This script does
"""
    Docstring:
"""

import random
from asyncio import timeout
from time import sleep

lotto = set()
dups = set()
historyNumbers = []
cnt = 0

while cnt < 10:
    while len(lotto) < 6:
        num = random.randint(1, 50)
        if num not in historyNumbers and num not in lotto:
            lotto.add(num)
        else:
            print("Duplicate number: ", num)
            dups.add(num)
    print("Lottery numbers =", lotto, cnt)
    historyNumbers.append(lotto)
    lotto = set()
    cnt += 1
    # sleep(.0009)

print("Numbers", historyNumbers)
print(f"Duplicates: {dups}")

# lotto = set() # Empty set
# while len(lotto) < 6:
#     num = random.randint(1, 50)
#     lotto.add(num)
#
# print("Lottery numbers =", sorted(lotto))