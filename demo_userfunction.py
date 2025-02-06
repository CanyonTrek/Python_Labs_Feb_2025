#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""

def sayhallo(greeting, recipient):
    message = greeting + " " + recipient
    print(message)
    return None

sayhallo("hi","David")
sayhallo(greeting="hallo",recipient="George")
