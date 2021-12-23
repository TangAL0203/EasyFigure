#-*-coding:utf-8-*-

'''
Method 1: use excel to plot histogram.
Method 2: use matplotlib to plot histogram.

'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

use_chines = True
# setting of font
if use_chines:
    font = {}
    # 设置matplotlib正常显示中文和负号
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
else:
    font = {'family': 'Consolas',
            'weight': 'normal',
            'size': 10,
            'fontweight': 'bold',
    }


# size setting
W, H = (500, 500)
plt.figure(figsize=(W/100.0, H/100.0))  # WH
# plt.grid(linestyle = "-.", linewidth=1)  #设置背景网格线为虚线

# generating data
data = np.random.randn(10000)
range_value = (data.min(), data.max())

"""
绘制直方图
data:必选参数，绘图数据
bins:直方图的长条形数目，可选项，默认为10
normed:是否对直方图做归一化, 默认为0, 代表不归一化. normed=1，表示归一化，显示频率。
facecolor:长条形的颜色
edgecolor:长条形边框的颜色
alpha:透明度
"""
plt.hist(data, bins=20, range=range_value, normed=0,
         facecolor="blue", edgecolor="black", alpha=0.7)  # if error, normed > cumulative
# 显示横轴标签
plt.xlabel("Score范围", fontdict=font)
# 显示纵轴标签
plt.ylabel("TP Score分布", fontdict=font)
# 显示图标题
plt.title("TP Score分布直方图", fontdict=font)
# 设置坐标轴刻度
x_ticks = np.arange(0.9, 1.01, 0.01)
plt.xticks(x_ticks)
plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
# plt.close()


'''
bins : int or sequence or str, optional
    If an integer is given, ``bins + 1`` bin edges are calculated and
    returned, consistent with `numpy.histogram`.

    If `bins` is a sequence, gives bin edges, including left edge of
    first bin and right edge of last bin.  In this case, `bins` is
    returned unmodified.

    All but the last (righthand-most) bin is half-open.  In other
    words, if `bins` is::

        [1, 2, 3, 4]

    then the first bin is ``[1, 2)`` (including 1, but excluding 2) and
    the second ``[2, 3)``.  The last bin, however, is ``[3, 4]``, which
    *includes* 4.

'''
