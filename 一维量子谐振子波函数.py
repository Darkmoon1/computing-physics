# Created by YHY
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
# 递推函数
def cal(G,phi,s,n):
    phinplusone = (2*phi[n]-phi[n-1]+5*G[n]*phi[n]*(s**2)/6+G[n-1]*phi[n-1]*(s**2)/12)/(1-G[n+1]*(s**2)/12)
    return phinplusone

# 递推算法    
def Numerov(func,Xmin,Xmax,args,step = 0.05):
    nn = 0
    x = np.linspace(Xmin,Xmax,8/step + 1)
    res = [0]*len(x)
    # 合理猜测phi1取0.0001
    res[1] = 0.0001

    for i in range(1,len(x)-1):
        res[i+1] = cal(args,res,step,i)
        if res[i]*res[i+1]<0:
            nn = nn+1

    print(nn)
    return res

Xmin = -4
Xmax = 4
x = np.linspace(Xmin,Xmax,8/0.05 + 1)
Eguess =[0.5,1.5,2.5]
V = 1/2*x**2
G0 = 2*V - 2*Eguess[0]
G1 = 2*V - 2*Eguess[1]
G2 = 2*V - 2*Eguess[2]

res0 = Numerov(cal,Xmin,Xmax,G0)
res1 = Numerov(cal,Xmin,Xmax,G1)
res2 = Numerov(cal,Xmin,Xmax,G2)

plt.plot(x,res0,x,res1,x,res2)
plt.grid(True)
plt.show()
