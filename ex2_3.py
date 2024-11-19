#! /usr/bin/env python3
#Author: Brad
#version: 1.0
#Description: Ex2_3.py python script

#how do i import pi, tan and cos??

import math

math.pi()
math.tan()
math.cos()

g = 9.81
v0 = 44
theta = 80 * (pi/180)
x = 0.5
y0 = 1

y = y0 + x*tan(theta) - (g * x**2)/(2 * ((v0 * cos*(theta))**2))

print('Height:', y, 'm')
