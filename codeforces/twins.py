n = int(input())
a = list(input().split(' '))
d = 0
s = 0
tem = 0
counter = 0

for i in range(n):
    s = s + int(a[i])

s = s / 1.9999
a = sorted(a, key=int, reverse=True)

for i in range(n):
    if tem < s:
        tem = tem + int(a[i])
        counter += 1
    else:
        break

if counter < 1:
    print(1)
else:
    print(counter)


