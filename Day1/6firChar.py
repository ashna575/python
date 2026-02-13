s="swiss"
d={}

for i in s:
    d[i]=d.get(i,0)+1


for m in d:
    if d[m]==1:
        print(m)
        break