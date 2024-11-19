#! /usr/bin/env python3
# Author: Brad
# version: 1.0
# Description: Leap year Script Info

"""
    Docstring:
"""



def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        return True
    else:
        return False

def main():
    user_input = int(input("Enter a year: "))
    if is_leap_year(user_input):
        print(f"{user_input} is a leap year.")
    else:
        print(f"{user_input} is NOT a leap year.")

if __name__=="_main_":
    main()


