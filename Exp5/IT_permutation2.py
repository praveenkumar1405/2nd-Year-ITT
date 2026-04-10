from itertools import permutations

s = '345'
p = list(permutations(s))
print()
for x in p:
    print(''.join(x))
print()
