a, b = int(input()), int(input())

t = a // b
t = (t + 2) % (t + 1)
n = t * a + (1 - t) * b
print(n)
