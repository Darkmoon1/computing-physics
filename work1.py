import math
import cmath
import numpy
from sympy import *

e = math.e
a = 0.529e-10
#n l m int r theta phi float
def cal(n,l,m,r,theta,phi):
    Y_m_l_theta_phi = Y(m,l,theta,phi)
    column = (2.0/n/a)**3 * math.factorial(n-l-1)
    column = column/2.0/n/math.factorial(n+l)**3
    column = math.sqrt(column)
    column = column * math.pow(e,-r/n/a) * math.pow(2*r/n/a,l)
    #由于L函数定义参数为p q 因此此处应该将q-p替换为q
    column = column*L(2*l+1,n+l,2*r/n/a)
    column = column * Y_m_l_theta_phi
    column = column**2 * Y_m_l_theta_phi**2 * r**2
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
    y = pow(-1,m)*sqrt((2*l+1)/4/math.pi*math.factorial(l-abs(m))/math.factorial(l+abs(m)))*cmath.exp(complex(0,1)*m*phi)*LegendrePloy(math.cos(theta),l,m)
    return y




print(cal(1,0,0,a,0.0,0.0))



