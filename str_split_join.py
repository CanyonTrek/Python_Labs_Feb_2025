#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""

line = "root:x:0:0:The Super User:/root:/bin/ksh"
fields = line.split(":")
fields[4] = "the administrator"
fields[6] = "/bin/bash"
print(type(fields))
print(fields)

line = ":".join(fields)

print(line)