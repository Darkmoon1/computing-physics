import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import *

pi = math.pi
e = math.e
a = 1
sw = true
#n=1-7 l<n  abs(m)<=l  r 0-10 theta 0-2pi phi -pi - pi
# a = 0.529e-10
#n l m int r theta phi float
def cal(n,l,m,r,theta,phi):
    Y_m_l_theta_phi = Y(m,l,theta,phi)
    column = (2.0/n/a)**3 * math.factorial(n-l-1)
    column = column/2.0/n/math.factorial(n+l)**3
    column = math.sqrt(column)
    column = column * e**(-r/n/a) * (2*r/n/a)**l
    #由于L函数定义参数为p q 因此此处应该将q-p替换为q
    column = column*L(2*l+1,n+l,2*r/n/a)
    column = column * Y_m_l_theta_phi
    column = abs(column)**2
    return column

def L(p,q,y):
    x = Symbol("x")
    column = e**(-x)*x**q
    for i in range(0,q):
        column = diff(column,x)
    column = column * e**x

    for i in range(0,q):
        column = diff(column,x)
    column = column * (-1)**p
    res = column.subs(x,y)
    return res

def LegendrePloy(y,l,m):
    t = Symbol("x")
    s = pow(t**2-1,l)
    for i in range(0,l):
        s = diff(s,t)
    k = pow((1-t**2),abs(m)/2)
    for i in range(0,abs(m)):
        s = diff(s,t)
    pl0 = k * s
    pl = 1/pow(2,l)/math.factorial(l)*pl0.subs(t,y)
    return pl

def Y(m,l,theta,phi):
    y = (-1)**m *sqrt((2*l+1)/4/pi*math.factorial(l-abs(m))/math.factorial(l+abs(m))) *np.exp(complex(0,1)*m*phi)*LegendrePloy(np.cos(theta),l,m)
    return y



#n=1-7 l<n  abs(m)<=l  r 0-10 theta 0-2pi phi -pi - pi

#x = rcos(phi)sin(theta) y=rsin()sin z=rcos(thetr)

step = 0.1
# phi = np.arange(-pi,pi,step)
theta = np.arange(0,pi,step)
phi = np.arange(0,2*pi,step)


n = 6
l = np.arange(0,n,1)
m = np.arange(0,n,1)
colors = ['y','r','b','black','chocolate','darkgray','gold','lightpink','oldlace','orange']

ax = plt.subplot(111, projection='3d')
for r in range(1,11):#11
    for theta_one in theta:
        for phi_one in phi:
            R = cal(n,2,2,r,theta_one,phi_one)
            #R = abs(Y(2,3,theta_one,phi))**2
            x_r = r*np.sin(theta_one)*np.cos(phi_one)
            y_r = r*np.sin(theta_one)*np.sin(phi_one)
            z_r = r*np.cos(theta_one)
            ax.scatter(x_r,y_r,z_r,c = 'black',alpha = R*10000)

# 必须显示声明 dtype => 'float64'
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
# ax.scatter(x_r[:8], y_r[:8], res[:8])


ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()

