#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does HOWto match and subtitute
# a pattern a replacement string
"""
    Docstring:
"""

# Sample line from /etc/passwd on linux for the root user login

import re

line = "root:x:0:0:The Super User:/root:/bin/ksh"
line = re.sub(r"[Ss]uper [Uu]ser", r"Administrator", line)
(line, num) = re.subn(r"ksh", r"bash", line)
print(f"Modified line = {line} with {num} changes")
