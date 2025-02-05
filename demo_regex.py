#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""

import re

fh_in = open(r"c:\labs\words", mode="rt")

for line in fh_in:
    #if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    #m = re.search("the", line) #the in any position
    #m = re.search("^the", line) #beginning with the
    #m = re.search("ing$", line)  # ending with ing
    m = re.search("^ring$", line)  # exact match

    if m:
        print(line, end="")

