#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""

import shelve

movies = {
    'william': ['fury', 'pulp fiction', 'shawshank redemption'],
    'kirill': ['pulp fiction', 'the departed', 'snach'],
    'mark': ['fifth element', 'armageddon', 'slapshot'],
    'mahendran': ['titanic', 'rambo', 'men in black'],
}
tv_series = { 'william': ['fame', 'walking dead'],
              'kirill': ['got', 'outlander'],
              'mark': ['cagney and lacey', 'scooby doo']
}

books = { 'william': 'the hobbit',
          'kirill': 'lotr',
          'mark': 'world war z'
}

with shelve.open(r"movies") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"movies") as db:
    print(f"Williams favourite movies are {db['movies']['william']}")
    print(f"Kirill's favourite tv_Series is  {db['tv_series']['kirill'][0]}")
    print(f"Mark's favourite book is {db['books']['mark']}")