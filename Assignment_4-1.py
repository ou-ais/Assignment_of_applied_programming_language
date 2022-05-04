import itertools

count = 0
for five in itertools.combinations(range(10), 5):
    count += 1
print(count / 2)