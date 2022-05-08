import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 5, 80)

y = x ** 4 - 3 * x ** 3 - 7 * x ** 2 + 7 * x + 2

coeff = [1, -3, -7, 7, 2]

roots = np.roots(coeff)
print('Roots of the polynomial are: %s' % roots)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, label='Polynomial curve')
ax.scatter(roots, np.zeros(4), color='red', label='roots')
ax.grid(True)
plt.show()