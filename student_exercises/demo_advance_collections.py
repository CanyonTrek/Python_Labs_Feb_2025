#! /usr/bin/python
# Author: BersuitX 
# Description: This about script copy and optionally filter
# source collection to a destination collection using different methods.
"""
    Docstring:
"""

# Source collection - list of string
students = ['euler', 'jorge', 'aram', 'mark', 'elizabeth', 'jeremy', ' erik', 'javonn',
            'kirill', 'euler', 'aram']

# Iterate through the collection and copy to a destination
# Using an ITERATOR loop plus source, optional condition and expression
wee_names = []
for name in students:
    if len(name) <= 5:
        wee_names.append(name.upper())

print(f"1.Short names = {wee_names}")

# Using an ITERATOR loop plus source, user function for filtering, an expression
def filter_names(name):
    if len(name) <= 5:
        return True
    else:
        return False

wee_names = []
for name in students:
    if filter_names(name):
        wee_names.append(name.upper())

print(f"2.Short names = {wee_names}")

# Using built-in functions

wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

wee_names = list(filter(lambda name:len(name) <= 5, students))
print(f"4.Short names = {wee_names}")

wee_names = [ name.upper() for name in students if len(name) <=5 ]
print(f"5.Short names = {wee_names}")

wee_names = [ (name.upper(), len(name)) for name in students if len(name) <=5 ]
print(f"6.Short names = {wee_names}")

wee_names = { name.upper(): len(name) for name in students if len(name) <=5 }
print(f"6.Short names = {wee_names}")

wee_names = { name.upper() for name in students if len(name) <=5 }
print(f"8.Short names = {wee_names}")
