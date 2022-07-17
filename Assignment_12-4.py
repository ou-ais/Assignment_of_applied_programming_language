import itertools

N = range(1, 101)
x = 0
for a, b, c in itertools.combinations(N, r=3):
    x +=  a * b * c
print(x)