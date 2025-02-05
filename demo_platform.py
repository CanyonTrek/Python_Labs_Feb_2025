#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""

import sys
import os

if sys.platform == "win32":
    home_dir = os.environ["HOMEPATH"]
else:
    home_dir = os.environ["HOME"]

print(home_dir)