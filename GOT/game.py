#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""

import tank
import sys

def main():
    erik_tank = tank.Tank("german","tiger")
    zane_tank = tank.Tank("american", "sherman")
    aram_tank = tank.Tank("british", "churchill")

    erik_tank.accel(61)
    zate_tank.accel(44)
    aram_tank.rotate_left(289)
    aram_tank.accel(31)
    aram_tank.shoot()

    erik_tank.take_damage(37)
    zane_tank.take_damage(49)




    return None

if __name__ == "__name__":
    main()
    sys.exit(0)