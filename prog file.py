x,y=(input(),input())
a,b=(input(),input())
d={}
f={}
g={}
h={}
p={}
m={}
o=list()
t=list()
r=[]
for i in range (1,9): #for rook
    if i != int (x):
        d[i]=int(y)
for i in range (1,9):
    if i != int (y):
        f[i]=int(x)

for k,v in  f.items():
    o.append((v,k))
w=list(d.items())+o

for i in range (1,9): #for queen
    if i != int (a):
        g[i]=int(b)
for i in range (1,9):
    if i != int (b):
        h[i]=int(a)

for k,v in h.items():
    t.append((v,k))

for i in range (1,9):
    if i!=int(a):
        y=i+int(b)-int(a)
        z=-i+int(b)+int(a)
        if z>0:
            k=z
            m[i]=z
        if y>0:
            l=y
            p[i]=y
u=list(p.items()) + list(g.items())+t+list(m.items())

                        #for comparison
for i in range (len(u)):
    for j in range (len(w)):
        if u[i]==w[j]:
            r.append(u[i])
r.sort()
for i in range(len(r)):
    print(r[i])
