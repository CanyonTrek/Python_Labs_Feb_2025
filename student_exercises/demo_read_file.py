#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""
for line in open('messier.txt', encoding="latin-1"):
    # print(len(line))
    line.replace(" ","|", count=-1)
    if line.startswith("M"):
        print(line, end="")

    # heroes = ['john doe', 'donald', 'Ada lovelace', 'keanu reeves']
    # print(min(heroes))
    # print(max(heroes))
    # a, b, c, *d = 10, 20, 30, 40, 50, 60
    # print(*d)
    # print(dir(heroes))
    # heroes.sort()
    # print(type(heroes))