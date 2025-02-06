#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo NOT FINISHED
"""
    Docstring:
"""

import re

nports = set()

fh_in = open(r"C:\Windows\System32\drivers\etc\Services", mode="rt")

for line in fh_in:
    m = re.search(r"(\d+)/(tcp|udp)", line)
    #m = re.search(r"^echo", line)
    if m:
        nport = int(m.group(1))
        nports.add(nport)
        print(line, end="")

fh_in.close()

print(nports, end="")