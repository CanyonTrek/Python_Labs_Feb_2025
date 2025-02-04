#! /usr/bin/env python3
# Author: Roberto F
# Description: This script will demo
"""
    Docstring:
"""
films = ['casshern','pulpfiction','idiocrazy','matrix','top gun']


for (idx,film) in enumerate(films): #generate tupple (0,'casshern'), next loop (1, 'pulpfiction')
    films[idx]=film.title()
    #print(film.title(), end="\n")
    print(films[idx], end="\n")
