k, n, w = input().split()
s = 0

for i in range(int(w)):
    s += int(k) * (i+1)

if s - int(n) >= 0:
    print(s - int(n))
else:
    print(0)

