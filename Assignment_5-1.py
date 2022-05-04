import numpy as np

id = 52
b = (id + 100) * 2

X = np.arange(3000)
idx = (b * X - X ** 2 - 5000 > 0)

X_ = X[idx]

print(X_.size)