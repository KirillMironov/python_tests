k = int(input())
h = k // 3600
k = k % 3600
m = k // 60
s = k % 60

m = str(m)
s = str(s)

if len(m) < 2:
    m = '0' + m
if len(s) < 2:
    s = '0' + s

print(h, ":", m, ":", s)
