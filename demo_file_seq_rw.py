#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does open, close, and
# read, write and add to a text file
"""
    Docstring:
"""

movies = {
    'william': ['fury', 'pulp fiction', 'shawshank redemption'],
    'kirill': ['pulp fiction', 'the departed', 'snach'],
    'mark': ['fifth element', 'armageddon', 'slapshot'],
    'mahendran': ['titanic', 'rambo', 'men in black'],
}

fh_out = open(r"c:\Users\Admin\course\Python_Labs_Feb_2025\movies.txt", mode="wt")

# Iterate
for name in movies.keys():
    print(f"{name} {movies[name]}", end="\n")
    #fh_out.write(name + str(movies[name]))
    fh_out.write(f"{name} str{movies[name]}\n")


fh_out.close()

print("-" * 60)
fh_in = open(r"c:\Users\Admin\course\Python_Labs_Feb_2025\movies.txt", mode="rt")

# text = fh_in.read() # Read entire file into string object
# text = fh_in.read(30) # Read entire file into string object
# text = fh_in.read(30) # Read entire file into string object
# text = fh_in.readline() # Read entire file into string object
# text_lines = fh_in.readlines() # Read entire file into string object

# print(type(text_lines))

for line in fh_in:
    print(line, end="")

fh_in.close()