dice = [1, 2, 3, 4, 5, 6]
count = 0

for i in dice:

    for j in dice:

        for k in dice:

            for m in dice:

                n = i * 1000 + j * 100 + k * 10 + m

                if n % 45 == 0:
                    count += 1
print(count)