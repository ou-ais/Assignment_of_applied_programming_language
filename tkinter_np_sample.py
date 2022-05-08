# coding: utf-8

import numpy as np
import io
import tkinter

# 注意：先にクリップボードにコピーしてから、このプログラムを実行すること

# クリップボードから、文字列を得る
clipped_data = tkinter.Tk().clipboard_get()

# 関数 io.StringIO を用いて、
# 文字列をあえて、ストリームとして扱うことにする
clipped_data_stream = io.StringIO(clipped_data)
print(clipped_data_stream)

# 関数 numpy.loadtxt を用いて、
# ストリームを読み取り、NumPy 2次元配列に変換し、変数 tatenaga に代入
tatenaga = np.loadtxt(clipped_data_stream)

print(tatenaga)

# NumPy 2次元配列 tatenaga が、何行何列かを表示
# アトリビュート shape は、何行何列かを表すタプル
print(tatenaga.shape)

print('#' * 30)

######################################################################

# tatenaga を転置した NumPy 2次元配列を変数 yokonaga に代入する
# アトリビュート T は、転置した NumPy 配列
yokonaga = tatenaga.T

print(yokonaga)

print('#' * 30)

######################################################################

# 転置した NumPy 配列の、第 1 行と第 2 行を表示
print(yokonaga[0])
print(yokonaga[1])
