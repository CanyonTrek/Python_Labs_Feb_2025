#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""

# Sample /etc/passwd on Linux
line = "root:x:0:0:The super User:/root:/bin/ksh"

# Separeted the line in fields according char
fields = line.split(":")
fields[4] = "The Administrator"
fields[6] = "/bin/bash"

line = ":".join(fields)

print(line)