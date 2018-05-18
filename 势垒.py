
    # Created by YHY
    
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

e = math.e
#---------------
# m 电子质量
# h 普朗克常数/2pi
# E  粒子能量
# U0  势垒高度
# A1  粒子的入射波能量
# a   势垒宽度
# x1,x2,x3    x1<0 0<x2<a a<x3
# ---------------- 

def cal(m,h,E,U0,A1,a,x1,x2,x3):

    k1 = (2*m*E/h**2)**(1/2)
    k2 = (2*m*(E-U0)/h**2)**(1/2)        
    # temp = cmath.sin(1000j)
    A2 = 2*1j*(k1**2-k2**2)*cmath.sin(k2*a)*A1/( (k1-k2)**2*e**(a*k2*1j)-(k1+k2)**2*e**(-a*k2*1j) )
    B1 = 2*k1*(k1+k2)*e**(-1j*k2*a)*A1/( (k1+k2)**2*e**(-a*k2*1j)-(k1-k2)**2*e**(a*k2*1j) )
    B2 = 2*k1*(k1-k2)*e**(1j*k2*a)*A1/( (k1-k2)**2*e**(a*k2*1j)-(k1+k2)**2*e**(-a*k2*1j) )
    C = 4*k1*k2*e**(-1j*k1*a)*A1/( (k1+k2)**2*e**(-1j*k2*a) - (k1-k2)**2*e**(1j*k2*a) )

    phi1 = A1*e**(1j*k1*x1) + A2*e**(-1j*k1*x1)
    phi2 = B1*e**(1j*k2*x2) + B2*e**(-1j*k2*x2)
    phi3 = C*e**(1j*k1*x3)
    
    T = abs(C)**2/abs(A1)**2   #透射率
    R = abs(A2)**2/abs(A1)**2  #反射率

    plt.plot(x1,phi1,'r',x2,phi2,'g',x3,phi3,'orange')
    # plt.scatter(x1,phi1)
    # plt.scatter(x2,phi2)
    # plt.scatter(x3,phi3)
    plt.axvline(0)
    plt.axvline(a)
    
    plt.show()
    
    return


step = 100

m = 9.1e-31
h = 1.05457266e-34
E = h**2/m
U0 = 1.00001*E
a = 1
A1 = 1
x1 = np.linspace(-5,0,step)
x2 = np.linspace(0,a,step)
x3 = np.linspace(a,6,step)
cal(m,h,E,U0,A1,a,x1,x2,x3)
# cal1(m,h,E,U0,A1,a,x1,x2,x3)
