#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""
def get_numbers():
    # numbers = []
    for x in range(0, 100):
    #     numbers.append(x)
    # return numbers
        yield x

for z in get_numbers():
    print(id(z))

print(id(get_numbers()))