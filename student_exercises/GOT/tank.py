#! /usr/bin/python
# Author: BersuitX
# Description: This about script copy and optionally filter
# source collection to a destination collection using different methods.
"""
    Docstring:
"""
import vehicule

class Tank(vehicule.Vehicle):
    # Attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        super().__init__(country, model)
        self._location = {'x':0, 'y':0, 'z':0}
        self._direction = 0
        self._shells = 20
        self._health = 100
        # No Explicit Return, as called implicitly.


    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    def __add__(self, other):
        return self._health + other._health

    def __del__(self):
        print("Boom..!")
        return None

    def get_health(self):
        return self._health

    def set_health(self, newhealth):
        self._health = newhealth
        return None
