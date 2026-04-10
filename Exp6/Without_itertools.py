# ===============================
# ITERTOOLS PROGRAMS 
# ===============================

from itertools import combinations, permutations, combinations_with_replacement
from itertools import product, cycle, count, repeat, compress
from itertools import dropwhile, takewhile, accumulate, groupby, islice
import operator

# ===============================
# 1. Without itertools – combinations of pairs
# ===============================
data = [1, 2, 3]
pairs = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        pairs.append((data[i], data[j]))
print(pairs)


# ===============================
# 2. Without itertools – Cartesian product
# ===============================
A = [1, 2]
B = ['a', 'b']
product_list = []
for x in A:
    for y in B:
        product_list.append((x, y))
print(product_list)


# ===============================
# 3. Using itertools.combinations
# ===============================
data = [1, 2, 3]
print(list(combinations(data, 2)))


# ===============================
# 4. Using itertools.product
# ===============================
A = [1, 2]
B = ['a', 'b']
print(list(product(A, B)))


# ===============================
# 5. itertools.permutations
# Generate all permutations of length 2
# ===============================
data = [1, 2, 3]
print(list(permutations(data, 2)))


# ===============================
# 6. itertools.combinations
# ===============================
print(list(combinations(data, 2)))


# ===============================
# 7. itertools.combinations_with_replacement
# ===============================
print(list(combinations_with_replacement(data, 2)))


# ===============================
# 8. itertools.product (again)
# ===============================
data1 = [1, 2]
data2 = ['A', 'B']
print(list(product(data1, data2)))


# ===============================
# 9. itertools.cycle
# ===============================
counter = 0
for item in cycle([1, 2, 3]):
    print(item, end=" ")
    counter += 1
    if counter > 7:
        break
print()


# ===============================
# 10. itertools.count
# ===============================
for i in count(10, 2):
    if i > 20:
        break
    print(i, end=" ")
print()


# ===============================
# 11. itertools.repeat
# ===============================
print(list(repeat("Hi", 3)))


# ===============================
# 12. itertools.compress
# ===============================
data = "ABCDEF"
selectors = [1, 0, 1, 0, 0, 1]
print(list(compress(data, selectors)))


# ===============================
# 13. itertools.dropwhile
# ===============================
print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 8, 3])))


# ===============================
# 14. itertools.takewhile
# ===============================
print(list(takewhile(lambda x: x < 5, [1, 4, 6, 8, 3])))


# ===============================
# 15. itertools.accumulate (sum & product)
# ===============================
data = [1, 2, 3, 4]
print(list(accumulate(data)))
print(list(accumulate(data, operator.mul)))


# ===============================
# 16. itertools.groupby
# ===============================
data = [(1, 'A'), (1, 'B'), (2, 'C'), (2, 'D'), (3, 'E')]
for key, group in groupby(data, lambda x: x[0]):
    print(key, list(group))


# ===============================
# HOMEWORK PROGRAMS
# ===============================

# 17. Generate combinations of 2 from ['A','B','C','D']
data = ['A', 'B', 'C', 'D']
print(list(combinations(data, 2)))


# ===============================
# 18. Permutations of string '123'
# ===============================
print(list(permutations('123')))


# ===============================
# 19. combinations_with_replacement for [1,2]
# ===============================
print(list(combinations_with_replacement([1, 2], 2)))


# ===============================
# 20. First 5 numbers from count starting at 10
# ===============================
c = count(10)
for _ in range(5):
    print(next(c), end=" ")
print()


# ===============================
# 21. Cycle through [5,10,15] for 3 iterations
# ===============================
c = cycle([5, 10, 15])
for _ in range(3):
    print(next(c), end=" ")
print()


# ===============================
# 22. Permutations of ['X','Y','Z']
# ===============================
print(list(permutations(['X', 'Y', 'Z'])))


# ===============================
# 23. First 6 items from cyclic ['a','b'] using islice
# ===============================
print(list(islice(cycle(['a', 'b']), 6)))


# ===============================
# 24. Product combinations with repetition
# ['red','green','blue'] choose 2
# ===============================
colors = ['red', 'green', 'blue']
print(list(product(colors, repeat=2)))
