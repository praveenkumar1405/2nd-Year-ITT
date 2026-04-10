from itertools import cycle, islice

l= ['d', 'e']
c= cycle(l)
r= list(islice(c, 6))
print()
print(r)
print()
