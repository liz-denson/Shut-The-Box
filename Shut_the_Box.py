######################################
# Shut the Box programming assignment
# Liz Denson & Connor Loudermilk
# 2023-09-29
######################################

from CSC201Ut import MSDie

def __add__(self, other):
    return self._value + other._value
MSDie.__add__ = __add__

d1 = MSDie(6)
d2 = MSDie(6)
print(d1, d2)
print (d1 + d2)

# { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
# { {1, 6}, {}} ... etc ---> look at a power set function
# (run through all possible combinations and see which combinations equal the sum of the die)
# then decide based on all of the combos/permutations (count in binary from 0 to the number for the tiles to lay down)