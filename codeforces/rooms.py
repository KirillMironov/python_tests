n = int(input())
counter = 0
p = []
q = []

for i in range(n):
    a, b = input().split()
    p.append(int(a))
    q.append(int(b))

for i in range(n):
    if q[i] - p[i] >= 2:
        counter += 1

print(counter)
