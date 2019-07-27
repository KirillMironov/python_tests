n, h = input().split(' ')
n = int(n)
h = int(h)
a = input().split(' ')
counter = 0

for i in range(n):
    if int(a[i]) <= h:
        counter += 1
    else:
        counter += 2

print(counter)






