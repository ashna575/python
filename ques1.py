# For an array of integers, arr[n], its prefix sum array, psum[n], is constructed as psum[i] = sum(arr[0].arr[i]) where 0 <= i<n The beauty of psum[n] is psum[0]-psum [1] + psum [2]-psum[3]... (-1)^n-1psum[n-1]. 
# Note: (- 1) ^ (n - 1) psum[n-1] indicates the last element may be added subtracted, depending on the parity of n - 1 If arr can be rearranged arbitrarily, find th-e maximum possible value of the beauty of psum[n]. Example n = 5 
# arr [3, 4, 5, 1, 1]
# The optimal arrangement of arr is [3,1,5,1,4) psum [3, 4, 9, 10, 14]. 
# The beauty of psum is 3 - 4 + 9 - 10 + 14 = 12 The answer is 12.
def fun(a):
    arr = sorted(a)
    n = len(arr)
    
    new = [0]*n
    mid = n//2
    
    low = 0
    high = n-1
    
    for i in range(n):
        if i == 0:
            new[i] = arr[mid]
        elif i % 2 != 0:
            new[i] = arr[low]
            low += 1
        else:
            new[i] = arr[high]
            high -= 1
            
    return new


a = [1,1,3,4,5]
s = fun(a)
print(s)          # [3,1,5,1,4]

# prefix sum
psum = [0]*len(s)
total = 0
for j in range(len(s)):
    total += s[j]
    psum[j] = total

print(psum)       # [3,4,9,10,14]

def fun2(b):
    even = 0
    odd = 0
    
    for i in range(len(b)):
        if i % 2 == 0:
            even += b[i]
        else:
            odd += b[i]
            
    return even - odd

print(fun2(psum))
