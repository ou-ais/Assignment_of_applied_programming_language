import numpy as np
import io
import matplotlib.pyplot as plt
import tkinter


# Read data from clipboard
clipped_data = tkinter.Tk().clipboard_get()
clipped_data_stream = io.StringIO(unicode(clipped_data))
data = np.loadtxt(clipped_data_stream)
n = data.size

# Fourier transform
fft_data = np.fft.fft(data)
# Power spectrum
ps_data = np.abs(fft_data) ** 2
ps_data = ps_data.astype(int)

component = np.where(ps_data > 0)[0]

fft_component = component[np.all([component < n/2-1, component > 1], axis=0)]

print(n / fft_component)