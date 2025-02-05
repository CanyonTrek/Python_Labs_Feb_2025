#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""

s1 = "a"
s2 = "e"
s3 = "i"
s4 = "j"
s5 = "b"

a = "a", "b", "c"
b = ("d", "e", "f")
c = {"g", "h", "i"}
d = ["j", "k", "l"]
e = {"a":"1", "b":"2"}
f = c.add("1")

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

print(s1 in a)
print(s2 in b)
print(s3 in c)
print(s4 in d)
print(s5 in e)
print(f)

