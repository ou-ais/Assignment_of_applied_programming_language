from cProfile import label
import numpy as np
import io
import matplotlib.pyplot as plt
import tkinter

clipped_data = tkinter.Tk().clipboard_get()

clipped_data_stream = io.StringIO(unicode(clipped_data))

temperature_data = np.loadtxt(clipped_data_stream)

regression = np.polyfit(temperature_data[:, 0], temperature_data[:, 1], 1)
print('Linear regression slope is: %.3f' % regression[0])

regress_curve = regression[0] * temperature_data[:, 0] + regression[1]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(temperature_data[:, 0], temperature_data[:, 1], 'o-', label='Temperature')
ax.plot(temperature_data[:, 0], regress_curve, '-', label='Regression')
ax.grid(True)
ax.set(xlabel='Data', ylabel='Temperature/($^\circ$C)', title='Nagano city lowest temperature March 2018')
plt.legend(loc='lower right')
plt.show()