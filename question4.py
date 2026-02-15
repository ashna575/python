a="a2b3a1c2b4"
d={}
i=0
while i< len(a):
    char=a[i]
    num=int(a[i+1])
    d[char]=d.get(char,0)+num
    i+=2
    result=""
    for i in d:
        result += i+str(d[i])
        
print(result)  
      