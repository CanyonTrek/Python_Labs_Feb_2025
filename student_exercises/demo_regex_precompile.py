#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""

import re

fh_in = open(r"c:\\labs\\words", mode="rt")

reobj = re.compile(r"^([A-Z]).*\1$")

for line in fh_in:
    m = reobj.search(line)  # Match lines start/end with SAME CAPITAL!
    if m:
        print(line, end="")