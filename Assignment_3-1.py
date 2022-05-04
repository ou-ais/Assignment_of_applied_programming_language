import itertools

a_count = 0
ab_count = 0

for choku in itertools.product('ab', repeat=8):
    a_count_j = 0

    for moji in choku:
        if moji == 'a':
            a_count_j += 1

    if a_count_j >= 3:
        a_count += 1

    for i in range(len(choku) - 1):
        if choku[i] == 'a' and choku[i+1] == 'b':
            ab_count += 1
            break

print('a_count:%d' % a_count)
print('ab_count:%d' % ab_count)
