# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

# 要素数 12 の NumPy 配列で表される数列を扱うこととする
n = 12

# t を、要素 0, 1, ..., 11 が並んだ NumPy 配列とする
t = np.arange(n)

# nami を、周期 12 の正弦波と、周期 6 の正弦波とを足し合わせた数列とする
# ベクトル計算により計算
nami = np.sin((2 * np.pi / n) * t) + np.sin((2 * np.pi / (n/2)) * t)

# nami に対し、離散フーリエ変換をほどこす
f_nami = np.fft.fft(nami)

# ベクトル計算により、各要素について、絶対値の2乗を計算
# これをパワースペクトルと呼ぶ
ps_nami = np.abs(f_nami)**2

# 以下、NumPy配列を表示するときに、指数表記をしないようにする
np.set_printoptions(suppress=True)

# パワースペクトルの性質：
# パワースペクトルの要素数を n とする。
# パワースペクトルの、添字 1 以上 n/2 - 1 以下の要素について、
# もし添字 k の要素が正ならば、元の数列は、周期 n/k の成分をもつ
print(nami)
print(ps_nami)

# 数列 nami のグラフを描いてみる
# plt.plot(t, nami)
# plt.show()
