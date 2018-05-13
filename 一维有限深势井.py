"""

Created by Yanxing Li on 2018/5/8.
Copyright © 2018年 WATT LEE. All rights reserved.

"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from pylab import *

tol = 1e-6
dpsi0=0.5
n = 1000
e1 = -1

class data:
    x = []
    y = []
    def __init__(self,x,y):
        self.x = x
        self.y = y
"""
@brief: the differential equation
"""
def func(y,x):
    return array([y[1],50**2*(-e1-1+x**2/2)*y[0]])
"""
@brief: OdeSolve function
@param: f       derived function
@param: a       the initial value of x
@param: b       the last value of x
@param: alpha   the first value of y
@param: m       the derivative on x=a
@param: k       number of intervals
@return: y[:,0] the value of y
"""
def OdeSolve(f,a,b,alpha,m,n): 
    x = linspace(a,b,n)
    yinit = array([alpha,m])
    y = odeint(f,yinit,x)
    datas = data(x,y)
    return datas

for i in range(1,10):
    delta = 2*tol
    de = 2*tol
    e1 = e1 + abs(e1)/70
    while abs(delta) > tol :
        xturn = -sqrt(abs(2*(e1+1)))
        k = 0.0001*np.power(-1,i+1)
        res1 = OdeSolve(func,-1,xturn,0,k,n)
        res2 = OdeSolve(func,1,xturn,0,-0.0001,n)
        y1 = res1.y
        y2 = res2.y
        dpsi = y1[n-1,1]-y2[n-1,1]
        delta = -dpsi*delta/(dpsi-dpsi0)
        dpsi0 = dpsi
        e1 = e1 + delta
    subplot(3,3,i)
    plt.plot(res1.x,y1[:,0],res2.x,y2[:,0],label='n ='+str(i))
    plt.xlabel('x')
    plt.ylabel('phi')
    plt.grid(True)
    plt.tight_layout()
plt.show()
