n = int(input())
a = list(input())
counter = 0

for i, ii in enumerate(a):
    if i == n-1:
        break
    if a[i] == a[i+1]:
        counter += 1

print(counter)
