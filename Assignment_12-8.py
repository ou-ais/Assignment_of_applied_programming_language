import io
import tkinter
import numpy as np


# Read data from clipboard
clipped_data = tkinter.Tk().clipboard_get()
clipped_data_stream = io.StringIO(unicode(clipped_data))
data = np.loadtxt(clipped_data_stream)

X = data.T[0]
Y = data.T[1]

a = np.polyfit(np.log(X), np.log(Y), 1)
print(a[0])