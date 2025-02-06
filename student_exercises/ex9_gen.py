#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""


def frange(start:float=0.0, end:float=0.0, step:float=0.25):
    num_range = []
    while (start <= end) & (step > 0):
        num_range.append(start)
        start = round(float(start+step),2)
    return num_range


# num = lambda start, step, end:float(start+step <= end)
#    print(num)

# print(list(frange(end=100, step=7)))
# print(list(frange(5,20)))

one = list(frange(0, 3.5, 0.25))
two = list(frange(3.5))
if one == two:
    print("Defaults worked!")
else:
    print("Ooops! Defaults did not work")
    print("one:", one)
    print("two:", two)