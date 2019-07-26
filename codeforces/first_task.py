import sys

n, m = input().split(' ')
n = int(n)
m = int(m)

for i in range(1, m + 1):
    if i ** n % m == 0:
        print(i)
        sys.exit(1)

print('ABSENT')
