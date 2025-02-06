#! /usr/bin/python
# Author: BersuitX 
# Description: This about script describe the use of functions
"""
    Docstring:
"""

def say_hello(greeting:str="Hi", recipient:str="friends", *countries):
    message = str(greeting) + " " + str(recipient)
    print(message)
    return None

say_hello("Hola", "Amigos")
say_hello(greeting="Hi", recipient="guys!")
say_hello(greeting="Hi", recipient="guys!")
say_hello("yo", recipient="homies!")
say_hello("bonjour", 5)
say_hello(greeting="yaya", recipient="Locos")
say_hello()

