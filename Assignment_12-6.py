import io
import tkinter
import itertools
import numpy as np
import pandas as pd


# Read data from clipboard
clipped_data = tkinter.Tk().clipboard_get()
clipped_data_stream = io.StringIO(unicode(clipped_data))
data = np.loadtxt(clipped_data_stream)

areas = range(6)
# ['Nagano': 0, 'Matsumoto': 1, 'Ueda': 2, 'Ina': 3, 'Sugadaira': 4, 'Nobeyama': 5]

Res = []
for a, b in itertools.product(areas, areas):
    if a != b:
        temp_a = pd.Series(data.T[a])
        temp_b = pd.Series(data.T[b])
        corr = temp_a.corr(temp_b)
        Res.append([corr, a, b])

Res_arr = np.array(Res)
print(Res_arr[np.argmax(Res_arr.T[0])])
