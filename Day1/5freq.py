text = "aabbbc"
d = {}

for x in text:
    d[x] = d.get(x, 0) + 1

for k in d:
    print(k, ":", d[k])
