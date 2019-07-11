n = int(input())
en = []
ex = []
counter = 0
tem = 0

for i in range(n):
    a, b = (int(i) for i in input().split())
    ex.append(a)
    en.append(b)

for i in range(n):
    tem = tem - ex[i] + en[i]
    if counter < tem:
        counter = tem

print(counter)


