a="listen"
b="silet"
d={}
e={}
for i in a:
    d[i]=d.get(i,0)+1
for i in b:
    e[i]=e.get(i,0)+1    
    
if d == e:
    print("yes")   
else:
    print("no")