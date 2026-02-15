a = [10,20,30,40,50]

i = 0
j = len(a) - 1

while i < j:
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

    i += 1
    j -= 1

print(a)
