#-*-coding:utf-8-*-
import os
import matplotlib.pyplot as plt
import numpy as np

pruned_ratios = [0.1,0.2,0.3,0.4,0.5,0.6,0.61,0.62,0.63,0.64,0.65,0.7]

after_bn = [0.9288,0.9288,0.9288,0.9288,0.9288,0.9288,0.9246,0.8725,0.7513,0.2997,0.2091,0.1048]
before_bn = [0.9287,0.9287,0.9174,0.9179,0.9181,0.8627,0.6535,0.3586,0.1238,0.1079,0.1042,0.1007]
sliming = [0.9287,0.9287,0.9267,0.9259,0.7561,0.4254,0.3564,0.1832,0.1047,0.084,0.061,0.061]
random = [0.8514,0.8012,0.6451,0.4178,0.2415,0.1341,0.1054,0.0912,0.1132,0.0924,0.0724,0.055]

plt.figure(figsize=(5,5))
plt.grid(linestyle = "-.", linewidth=1)      #设置背景网格线为虚线
ax = plt.gca() #获得坐标轴的句柄

ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);####设置上部坐标轴的粗细


# red, blue, green, magenta, yellow, black

plt.plot(pruned_ratios, after_bn,"red",label="scaling layer after BN",linewidth=3)
plt.plot(pruned_ratios, before_bn,"blue",label="scaling layer before BN",linewidth=3)
plt.plot(pruned_ratios, sliming,"green",label="network-sliming",linewidth=3)
plt.plot(pruned_ratios, random,"magenta",label="random",linewidth=3)

legend_font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 30}
plt.legend(prop=legend_font, loc=3)

# 设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=40)
labels = ax.get_xticklabels() + ax.get_yticklabels()
# print labels
[label.set_fontname('Times New Roman') for label in labels]

# 画点
plt.scatter(pruned_ratios,after_bn,c = 'red',s=200,marker = '.')
plt.scatter(pruned_ratios,before_bn,c = 'blue',s=200,marker = '.')
plt.scatter(pruned_ratios,sliming,c = 'green',s=200,marker = '.')
plt.scatter(pruned_ratios,random,c = 'magenta',s=200,marker = '.')


# 设置横纵坐标的名称以及对应字体格式
font2 = {'family': 'Arial',
         'weight': 'normal',
         'size': 37,
         # 'fontweight': 'bold',
         }
plt.xlabel("Pruning ratio", font2)
plt.ylabel("Accuracy", font2)
plt.show()