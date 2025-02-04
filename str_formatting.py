#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""
planets = {'mer':57.91,
           'ven':108.2,
           'earth':149.59,
           'mars':227.94
}

for planet in planets.keys():
    print(planet)
    print("\t\t" + planet + ": " +str(planets[planet]) + " Gm\t" + str(hex(0xff)))

print("-" * 40)

for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12) + " Gm\t" + str(hex(0xff)).rjust(6))

print("+" * 40)

for planet in planets.keys():
    print("{0:12s} {1:12f} Gm {2:6x}".format(planet,planets[planet],0xff))
