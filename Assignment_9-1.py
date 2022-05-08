from pydoc import cli
import numpy as np
import io
import matplotlib.pyplot as plt
import tkinter

clipped_data = tkinter.Tk().clipboard_get()

clipped_data_stream = io.StringIO(unicode(clipped_data))

temperature_data = np.loadtxt(clipped_data_stream)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(temperature_data[:,0], temperature_data[:, 1], 'o-')
ax.grid(True)
ax.set(xlabel='Data', ylabel='Temperature/($^\circ$C)', title='Nagano city lowest temperature March 2018')
plt.show()