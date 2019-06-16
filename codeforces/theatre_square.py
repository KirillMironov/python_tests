import math

n, m, a = (int(i) for i in input().split())

n1 = n / a
m1 = m / a

if n1 % 2 != 0:
    b = n / a
    b = math.ceil(b)
else:
    b = n // a

if m1 % 2 != 0:
    c = m / a
    c = math.ceil(c)
else:
    c = m // a

print(b * c)
