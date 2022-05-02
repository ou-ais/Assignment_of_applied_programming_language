import numpy as np
import matplotlib.pyplot as plt

id = 52
b = (id + 100) * 2

X = np.linspace(0, 2999, 3000)
Y = - X ** 2 + b * X - 5000

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(X, Y, color='green', linestyle='dashed', linewidth=3)
ax.grid(True)
ax.set(xlabel='X', ylabel='Y', title='My student ID curve')

plt.show()