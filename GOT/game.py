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
    zane_tank.accel(44)
    aram_tank.rotate_left(289)
    aram_tank.accel(31)
    aram_tank.shoot()

    erik_tank.take_damage(37)
    zane_tank.take_damage(49)

    print(f"health of erik's tank is {erik_tank._health}")
    print(f"health of erik's and zane tank is {erik_tank + zane_tank}")

    erik_tank.set_health(100)
    #print(f"new health of erik's tank is {erik_tank._health}")
    print(f"new health of erik's tank is {erik_tank.tank_health}")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
