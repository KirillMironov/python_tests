n = int(input())
groups = list(input().split())

s = 0

n1, n2, n3, n4 = 0, 0, 0, 0
counter = 0

for i in range(n):
    if groups[i] == '1':
        n1 += 1
    elif groups[i] == '2':
        n2 += 1
    elif groups[i] == '3':
        n3 += 1
    elif groups[i] == '4':
        n4 += 1

for i in range(4):
    if n4 % 2 == 0:
        counter = counter + n4
        n4 = 0
    elif (n4 - 1) % 2 == 0:
        counter = counter + n4 - 1
        n4 = n4 - counter
    elif n4 == 1:
        counter = counter + 1

# n4

if n4 % 2 == 0:
    counter = counter + n4
    n4 = 0
elif (n4 - 1) % 2 == 0:
    counter = counter + n4 - 1
    n4 = n4 - counter
elif n4 == 1:
    counter = counter + 1

# n3




