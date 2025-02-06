#! /usr/bin/env python
# Author: BersuitX
# Description: This about script copy and optionally filter
# source collection to a destination collection using different methods.
"""
    Docstring:
"""
from random import random, randint

import tank
import sys

def main():
    winner = None
    erik_tank = tank.Tank("german", "tiger")
    zane_tank = tank.Tank("american", "sherman")
    aram_tank = tank.Tank("british", "churchill")

    aram_tank.accel(randint(1, 100))
    erik_tank.accel(randint(1,100))
    zane_tank.accel(randint(1,100))

    aram_tank.rotate_left(randint(0,360))
    erik_tank.rotate_left(randint(0, 360))
    zane_tank.rotate_left(randint(0, 360))

    aram_tank.accel(randint(1,100))
    erik_tank.accel(randint(1, 100))
    zane_tank.accel(randint(1, 100))

    aram_tank.shoot()
    erik_tank.shoot()
    zane_tank.shoot()

    aram_tank.take_damage(randint(1, 99))
    erik_tank.take_damage(randint(1,99))
    zane_tank.take_damage(randint(1,99))

    # print(f"Health of Erik-s tanks is {erik_tank._health}")
    # print(f"Health of Aram's tanks is {aram_tank._health}")
    # print(f"Health of Zane's tanks is {zane_tank._health}")
    # print(f"Status of Erik's and Zane's is {erik_tank + zane_tank}")
    # # erik_tank.set_health(100 - erik_tank._health)
    # print(f"Health of Erik-s tanks is {erik_tank._health}")
    print(aram_tank.__dict__)
    print(erik_tank.__dict__)
    print(zane_tank.__dict__)

    # if erik_tank._health > zane_tank._health > aram_tank._health:
    #     winner = erik_tank.country

    print(f"And the winner is: {winner}")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)