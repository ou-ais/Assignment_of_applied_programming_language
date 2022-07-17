import itertools

dice = [1, 2, 3, 4, 5, 6]

i = 0
for a, b, c, d in itertools.product(dice, dice, dice, dice):
    n = a * 1000 + b * 100 + c * 10 + d * 1
    if n % 45 == 0:
        i += 1
print(i)