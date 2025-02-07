#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""

import sys
import re

with open(r"c:\\Windows\\System32\drivers\etc\services", mode="rt") as service:
    for line in service:
        if line.isspace(): continue
        obj = re.compile("^#")
        if not obj.search(line):
            line = re.sub(r"\s+", repl="#", string=line)
            s = line.split("#")
            pp = s[1].split("/")
            if int(pp[0]) <= 200:
                print(f"Service: {s[0]} Port: {s[1]}", end="\n")
