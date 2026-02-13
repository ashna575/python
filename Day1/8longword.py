a="i love coding interviews"
b=(a.split(" "))

long=b[0]
for j in b:
   if len(long)<len(j):
       long=j
print(long)    