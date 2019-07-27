import sys

n = int(input())
a = list(input().split(' '))
even = 0
odd = 0

for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        even += 1
    else:
        odd += 1

if even == 1:
    for j in range(len(a)):
        if int(a[j]) % 2 == 0:
            print(j+1)
            sys.exit(0)
else:
    for k in range(len(a)):
        if int(a[k]) % 2 != 0:
            print(k+1)
            sys.exit(0)
