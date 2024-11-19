#! /usr/bin/env python3
# Author: Brad
# version: 1.0
# Description: f-strings Script Info



Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print("-" * len(Belgium))
print(Belgium.replace(",", ":"))

pop_country = int(Belgium[8:16])
pop_capital = int(Belgium[26:32])

print(f"Population of Country and Capital = {pop_country + pop_capital}")
print("-" * len(Belgium))


