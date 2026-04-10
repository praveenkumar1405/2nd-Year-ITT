from itertools import cycle

l= [4, 8, 12]
c= cycle(l)
r= [next(c) for _ in range(9)]
print()
print(r)
print()
