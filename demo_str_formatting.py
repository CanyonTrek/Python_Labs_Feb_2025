#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""

planets = {"Mercury":"58.1", "Venus":"60.1", "Earth":"32.1", "Mars":"22.1"}
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm\t" + str(hex(0xff)))

print("-" * 60)
# Use str concat plus justify methods - OK!
for planets in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet].center(12, '.') + " Gm " + str(hex(0xff))))

print("-" * 60)
# Use str.format() method - GOOD! plus justify methods - OK!
for planets in planets.keys():
    print()

print("-" * 60)
# Use str.format() method - GOOD! plus justify methods - OK!
for planets in planets.keys():
    print()
