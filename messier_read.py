#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""

for line in open('\labs\messier.txt',encoding='latin_1'):
    if not line: break

    #print(line)
    if line[0]=="M":
        print(line[6:39].strip(),"|",line[40:63].strip(),"|",line[64:79].strip(),sep="")
