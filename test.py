 
X={"x0":0.0}
P={"p0":0.0}
G={"g0":0.0}
nn=0

x=-4
s=0.05
m=160
E=0.5

for i in list(range(m+1)):
    X["x%s" % i]=0.0 #储存x

for i in list(range(m+1)):
    P["p%s" % i]=0.0 #储存psi
    
for i in list(range(m+1)):
    G["g%s" % i]=0.0 #储存g

P["p1"]=0.0001
X["x0"]=x
X["x1"]=X["x0"]+s
G["g0"]=X["x0"]*X["x0"]-2*E
G["g1"]=X["x1"]*X["x1"]-2*E
ss=s*s/12

for i in range(1,m+1):
    X["x%s" % (i+1)]=X["x%s" % i]+s
    G["g%s" % (i+1)]=X["x%s" % (i+1)]*X["x%s" % (i+1)]-2*E
    P["p%s" % (i+1)]=(-P["p%s" % (i-1)]+2*P["p%s" % i]+10*G["g%s" % i]*P["p%s" % i]*ss+G["g%s" % (i-1)]*P["p%s" % (i-1)]*ss)/(1-G["g%s" % (i+1)]*ss)
    if (P["p%s" % i]*P["p%s" % (i+1)]<0):
        nn=nn+1
        
print("Er="+str(E))
print("Nodes="+str(nn))
for i in range(m+1):
    print("Psir(%f)=%f" % (X["x%s" % i],P["p%s" % i]))