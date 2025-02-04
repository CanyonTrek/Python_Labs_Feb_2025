#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""

import sys
import os
print(sys.platform)

if sys.platform == "win32":
    home_dir = os.environ["HOMEPATH"]
else:
    home_dir = os.environ["HOME"]

print(home_dir)

