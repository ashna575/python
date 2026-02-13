a="madam"
flag=True
for i in  range(0,len(a)//2):
   if a[i]!=(a[len(a)-1-i]):
     flag=False
     break
 
 
if flag:
  print("YES")

else:
 print("No")     