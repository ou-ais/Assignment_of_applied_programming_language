# coding: utf-8

# モジュール numpy をインポート、以後 np という名前で使う
import numpy as np

# モジュール matplotlib.pyplot をインポート、以後 plt という名前で使う
import matplotlib.pyplot as plt

# サイコロの目が並んだ NumPy 配列を作る
saikoro = np.arange(1,7)

print(saikoro)

# ベクトル計算により、各要素について、2乗を計算
saikoro_nijou = saikoro**2

print(saikoro_nijou)

print('#' * 30)

######################################################################

# saikoro の、平均、分散を表示
print(np.mean(saikoro))
print(np.var(saikoro))

# saikoro_nijou の、平均、分散を表示
print(np.mean(saikoro_nijou))
print(np.var(saikoro_nijou))

print('#' * 30)

######################################################################

# saikoro と saikoro_nijou の、相関係数を表示
# 関数 np.corrcoef の返り値（返り値は NumPy 2次元配列）のうち、
# 第1行第2列（添字は[0][1]）が相関係数である
m = np.corrcoef(saikoro, saikoro_nijou)
print(m[0][1])

print('#' * 30)

######################################################################

# saikoro に対する、saikoro_nijou の、線形回帰を行う
# 関数 np.polyfit の返り値（返り値は NumPy 1次元配列）のうち、
# 第1要素（添字は[0]）が傾き、第2要素（添字は[1]）が切片である
saikoro_nijou_kaiki = np.polyfit(saikoro, saikoro_nijou, 1)
print(saikoro_nijou_kaiki)

# ベクトル計算により、
# saikoro_nijou_kaiki[0] を傾きとし、
# saikoro_nijou_kaiki[1]を切片とする直線の、
# 縦軸データを表す NumPy 配列を作る
chokusen = saikoro_nijou_kaiki[0] * saikoro + saikoro_nijou_kaiki[1]

# 横軸データ saikoro に対し、
# 縦軸データ saikoro_nijou を丸で、
# 加えて、縦軸データ chokusen を直線で描く
plt.plot(saikoro, saikoro_nijou, 'o', saikoro, chokusen, '-')
plt.show()
