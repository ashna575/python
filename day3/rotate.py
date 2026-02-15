arr = [1,2,3,4,5]

# [4,5,1,2,3]
n=len(arr)
k=2

for i in range(k):
    last=arr[n-1]
    for j in range(n-1,0,-1):
        arr[j]=arr[j-1]
    arr[i]=last    

print(arr)    