s = "aabccde"
d={
    
}
for i in s:
    d[i]=d.get(i,0)+1
    
for j in d:
    if d[j]==1:
        print(j)
        break
    