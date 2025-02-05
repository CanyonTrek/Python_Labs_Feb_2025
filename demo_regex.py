#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""
fh_in = open(r"c:\labs\words", mode="rt")

for line in fh_in:
    if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
        print(line, end="")

