import numpy as np

nagano = np.array([3.6, -1.3, -3.5, -1.2, 2.7,
                   -1.3, -2.3, 2.9, 1.2, -1.5,
                   -3.5, -0.5, -2.3, 0.8, 3.3,
                   0.2, -0.8, -2, 1.8, 0.8,
                   0.4, 3.5, 2.1, -0.1, 0.8,
                   1.2, 4, 4.2, 4.6, 0.9, -1.3])

below_zero_idx = nagano < 0.
rise_two_idx = np.diff(nagano) >= 2.0

print('Temperatures below zero are: %d days.' % nagano[below_zero_idx].size)

print('Temperatures rose by two degrees are: %d days.' % nagano[1:][rise_two_idx].size)