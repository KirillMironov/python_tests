from collections import Counter

n = int(input())
s = list(input().split(' '))
s = [int(item) for item in s]
c = Counter(s)
counter = 0

counter += c[4]
counter += c[3]
c[1] -= c[3]
if c[1] < 0:
    c[1] = 0
if c[2] == 1:
    counter += 1
    c[1] -= 2
else:
    counter += c[2] // 2
    if c[2] % 2 != 0:
        counter += 1
        if c[1] > 1:
            c[1] -= 2
        elif c[1] == 1:
            c[1] -= 1
if c[1] < 0:
    c[1] = 0
counter += c[1] // 4
if c[1] % 4 != 0:
    counter += 1

print(counter)
