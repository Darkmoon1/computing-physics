# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:37:21 2015

@author: Eddy_zheng
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.random.randint(0, 255, size=[40, 40, 40])

x, y, z = data[0], data[1], data[2]
ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度

# x = np.arange(1,10,1)
# y = np.arange(10,1,-1)
z = np.array([-0,0.0430785586036973,0.0430785586036973,0.0430785586036973,0.0430785586036973,0.0430785586036973,0.0430785586036973])
y = np.array([-0.0,      -0.70807342586036973, -0.82682181586036973 ,-0.01991486586036973 ,-0.57275002586036973 ,-0.91953576586036973
, -0.07807302586036973])
x = np.array([-0.0, -0.45464871586036973 , 0.37840125586036973 , 0.13970775586036973 ,-0.49467912586036973 , 0.27201056586036973, 0.26828646586036973])

ax.scatter(x, y, z, c='y')  # 绘制数据点


ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
print(np.sin(2*3.14))