n = int(input())  # кол-во слов
a = []

for i in range(n):
    a.append(input())
    tem = list(a[i])
    n = len(tem)
    if n > 10:
        print(tem[0]+str(n-2)+tem[n-1])
    else:
        print(a[i])


