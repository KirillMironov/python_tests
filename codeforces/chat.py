hello = list('hello')
a = list(input())
b = []
tem = 0

for i in range(len(hello)):
    for j in range(len(a)):
        if j == 0:
            if hello[i] == a[j]:
                b.append(j)
                tem = j
                break
        elif j > 0:
            if hello[i] == a[j] and j > tem:
                b.append(j)
                tem = j
                break

if len(b) >= 5 and b == sorted(b):
    print('YES')
else:
    print('NO')




