#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""
from operator import truediv

students = ['euler','jorge', 'aram','mark','elizabeth', 'jeremy','erik', 'javonn', 'kiril']

wee_names = []
for name in students:
    if len(name) <= 5:
        wee_names.append(name)

print(f"short names = {wee_names}")

def filter_names(name):
    if len(name) <= 5:
        return True
    else:
        return False

wee_names = []
for name in students:
    if filter_names(name):
        wee_names.append(name)

print(f"short names = {wee_names}")


wee_names = list(filter(filter_names, students))
print(f"short names = {wee_names}")

wee_names = list(filter(lambda name:len(name)<=5, students))
print(f"short names = {wee_names}")


wee_names = [ name for name in students if len(name) <=5 ]
print(f"short names = {wee_names}")

