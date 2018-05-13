"""
    Created by Yanxing Li on 2018/5/7.
    Copyright © 2018年 WATT LEE. All rights reserved.
    """

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from pylab import *

n = 1

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
    return array([y[1],-(n**2*math.pi**2*y[0])])
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
def OdeSolve(f,a,b,alpha,m,k):
    x = linspace(a,b,k)
    yinit = array([alpha,m])
    y = odeint(f,yinit,x)
    return y[:,0]

"""
    @brief: shootev
    @param: n       num
    @param: a       the initial value of x
    @param: b       the last value of x
    @param: func    the differential equation
    @param: alpha   the first value of y
    @param: beta    the last value of y
    @param: m1      the guessed derivative on x=a
    @param: tor     tolerence
    @return: x      selceted x value
    @return: y      solved y value
    """
def shootev(k,a,b,alpha,beta,m1,tor):
    m = []
    yb = []
    x = linspace(a,b,k)
    m.append(m1)
    y = OdeSolve(func,a,b,alpha,m[0],k)
    yb.append(y[k-1])
    if abs(yb[0]-beta) >= tor:
        m.append(m[0]*beta/yb[0])
        y = OdeSolve(func,a,b,alpha,m[1],k)
        yb.append(y[k-1])
        i = 1
        while abs(yb[i]-beta) >= tor :
            l = len(m)
            m.append(m[l-1]+(beta-yb[i])*(m[l-1]-m[l-2])/(yb[i]-yb[i-1]))
            y = OdeSolve(func,a,b,alpha,m[i+1],k)
            yb.append(y[k-1])
            i = i + 1
        datas = data(x,y)
        return datas
    else:
        datas = data(x,y)
        return datas

for i in range(1,4):
    res = shootev(1000,0,1,0,0,np.sqrt(2)*math.pi*n-0.1,0.0001)
    plt.plot(res.x,res.y,label='E ='+str(i))
    n = n + 1
plt.xlabel('x')
plt.ylabel('phi')
plt.grid(True)
plt.legend(loc=4)
plt.title('shoot method on 1D infinite deep well mapping')
plt.show()
