#! /usr/bin/python
#                    1         2         3         4
#          012345678901234567890123456789012345678901234567890
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

a = len(Belgium)
print(a)

print("-" * a)

fields = Belgium.split(",")
Belgium = ":".join(fields)
print(Belgium)

totpop = int(fields[1])+int(fields[3])
print(totpop)
print("-" * a)

