k = int(input())
a = k // 1000
b = k // 100 % 10
c = k % 100 // 10
d = k % 10

if (a == d) and (b == c):
    print(1)
else:
    print(0)
