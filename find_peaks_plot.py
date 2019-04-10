#-*-coding:utf-8-*-
import os
import matplotlib.pyplot as plt
import numpy as np
import heapq

nums = [0.8254996538162231,
 0.9476225972175598,
 0.9118293523788452,
 0.7426753640174866,
 1.0082956552505493,
 0.690430760383606,
 0.9430007934570312,
 0.8363696932792664,
 0.9134036302566528,
 0.7780791521072388,
 0.8943929076194763,
 0.7841998338699341,
 0.7933627367019653,
 0.7789521813392639,
 0.979821503162384,
 0.9356294274330139,
 0.8437743186950684,
 0.9103038907051086,
 1.0974432229995728,
 0.937798798084259,
 0.7450103163719177,
 0.9357324838638306,
 0.8309947848320007,
 0.9419568181037903,
 0.8728816509246826,
 0.9262248277664185,
 0.8743247985839844,
 0.7461255788803101,
 1.0175384283065796,
 0.7959684133529663,
 0.9016406536102295,
 0.9141321778297424,
 0.8937291502952576,
 0.8078308701515198,
 0.8542062044143677,
 0.9457948803901672,
 0.8552749752998352,
 0.912862241268158,
 0.7126821279525757,
 0.7496225237846375,
 0.7769675850868225,
 0.8433071374893188,
 0.8129876255989075,
 0.7422658205032349,
 0.8152564764022827,
 0.8094494342803955,
 0.6807045936584473,
 0.8381760716438293,
 0.9032894968986511,
 0.8253363966941833,
 0.6917704939842224,
 0.7485485076904297,
 1.1334460973739624,
 0.49811995029449463,
 0.8442986011505127,
 0.8953750133514404,
 0.7721608877182007,
 0.7062458395957947,
 0.7439448833465576,
 0.8145563006401062,
 0.7848573923110962,
 1.0206515789031982,
 0.9222621321678162,
 0.9242947101593018]

peaks = []
troughs = []

for idx in range(1, len(nums)-1):
    if nums[idx-1] < nums[idx] > nums[idx+1]:
        peaks.append((idx, nums[idx]))
    if nums[idx-1] > nums[idx] < nums[idx+1]:
        troughs.append((idx, nums[idx]))

# for start and end
if nums[0]>nums[1]:
    peaks.append((0,nums[0]))
if nums[-1]>nums[-2]:
    peaks.append((len(nums)-1,nums[-1]))


plt.figure(figsize=(5,5))
plt.grid(linestyle = "--")      #设置背景网格线为虚线
ax = plt.gca() #获得坐标轴的句柄

ax.spines['bottom'].set_linewidth(3);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(3);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(3);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(3);####设置上部坐标轴的粗细


x = range(len(nums))
plt.plot(x, nums,"blue",label="ours",linewidth=5)
# 画点

# 设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=40)
labels = ax.get_xticklabels() + ax.get_yticklabels()
# print labels
[label.set_fontname('Times New Roman') for label in labels]

peaks_list = peaks
peaks_dots = np.array(peaks_list)
plt.scatter(peaks_dots[:,0],peaks_dots[:,1],c = 'red',s=600,marker = '.')

# plt.xlabel("channel index",fontsize=30,fontweight='bold')
# plt.ylabel("value",fontsize=30,fontweight='bold')

# 设置横纵坐标的名称以及对应字体格式
font2 = {'family': 'Arial',
         'weight': 'normal',
         'size': 37,
         # 'fontweight': 'bold',
         }
plt.xlabel("Channel index", font2)
plt.ylabel("Value", font2)
plt.show()