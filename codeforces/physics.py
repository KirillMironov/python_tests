a = []
n = int(input())
s1 = 0
s2 = 0
s3 = 0

for i in range(n):
    a.append(input().split())

for i in range(n):
    s1 += int(a[i][0])
    s2 += int(a[i][1])
    s3 += int(a[i][2])

if s1 == s2 == s3 == 0:
    print('YES')
else:
    print('NO')



