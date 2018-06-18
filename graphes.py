import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as cols
from mpl_toolkits.mplot3d import Axes3D
import multiprocessing
from sympy import *


pi = math.pi
e = math.e
a = 1
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
    y = (-1)**m * np.sqrt((2*l+1)/4/pi*math.factorial(l-abs(m))/math.factorial(l+abs(m))) *np.exp(complex(0,1)*m*phi)*LegendrePloy(np.cos(theta),l,m)
    return y



#n=1-7 l<n  abs(m)<=l  r 0-10 theta 0-2pi phi -pi - pi

#x = rcos(phi)sin(theta) y=rsin()sin z=rcos(thetr)

step = 0.1
# phi = np.arange(-pi,pi,step)
theta = np.arange(0,pi,step)
phi = np.arange(0,2*pi,step)


n = 3
l = np.arange(0,n,1)
m = np.arange(0,n,1)
colors = ['y','r','b','black','chocolate','darkgray','gold','lightpink','oldlace','orange']

ax = plt.subplot(111, projection='3d')
p = []
# for r in np.arange(1,11,0.1):#11
#     for theta_one in theta:
#         for phi_one in phi:
#             R = cal(n,2,1,r,theta_one,phi_one)
#             #R = abs(Y(2,3,theta_one,phi))**2
#             x_r = r*np.sin(theta_one)*np.cos(phi_one)
#             y_r = r*np.sin(theta_one)*np.sin(phi_one)
#             z_r = r*np.cos(theta_one)
            # if (R * 1e7 - 4.52) < 0.0001:
            #     ax.scatter(x_r,y_r,z_r,c = 'blue',marker = ',')

# cos_phi = np.cos(phi)
# sin_phi = np.sin(phi)

def func(theta):
    global phi
    # R = []
    x_r = []
    y_r = []
    z_r = []
    R_r = []
    c_r = []
    for r in np.arange(1,11,1):#11
        for theta_one in theta:
        #     tempR = cal(n,2,1,r,theta_one,phi)
        #     if (tempR[0] - 5e-6 )< 1e-8:
        #         # R.append(tempR)
        #         #R = abs(Y(2,3,theta_one,phi))**2
        #         x_r.append(r*np.sin(theta_one)*cos_phi)
        #         y_r.append(r*np.sin(theta_one)*sin_phi)
        #         z_r.append(r*np.cos(theta_one))
        #     for theta_one in theta:
            for phi_one in phi:
                R = cal(n,2,1,r,theta_one,phi_one)
                if abs(R - 5e-6 )< 1e-6 and abs(R - 5e-6 )>1e-7:
                # if abs(R)>1e-6:
                #R = abs(Y(2,3,theta_one,phi))**2
                    x_r.append(r*np.sin(theta_one)*np.cos(phi_one))
                    y_r.append(r*np.sin(theta_one)*np.sin(phi_one))
                    # z_r.append(r*np.cos(theta_one))
                # R_r.append(math.ceil(R*1e8))
                # c_r.append(cols.to_rgb())


    return x_r,y_r

# depthshade=False
# 必须显示声明 dtype => 'float64'
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
# ax.scatter(x_r[:8], y_r[:8], res[:8])
theta1 = theta[0:8]
theta2 = theta[8:16]
theta3 = theta[16:24]
theta4 = theta[24:32]
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 4)

    result1 = pool.apply_async(func, (theta1, ))
    result2 = pool.apply_async(func, (theta2, ))
    result3 = pool.apply_async(func, (theta3, ))
    result4 = pool.apply_async(func, (theta4, ))    
    
    pool.close()
    pool.join()
    
    res1 = result1.get()
    res2 = result2.get()
    res3 = result3.get()
    res4 = result4.get()
    ax.scatter(res1[0] ,res1[1],res1[2], c = 'blue',alpha = 0.5)
    ax.scatter(res2[0] ,res2[1],res2[2], c = 'blue',alpha = 0.5)
    ax.scatter(res3[0] ,res3[1],res3[2], c = 'blue',alpha = 0.5)
    ax.scatter(res4[0] ,res4[1],res4[2], c = 'blue',alpha = 0.5)
    
    ax.set_zlabel('Z')  # 坐标轴
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    plt.show()

