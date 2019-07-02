n = int(input())
counter = 0

while n > 0:
    a, b, c = (int(i) for i in input().split())
    s = a + b + c
    if int(s) >= 2:
        counter = counter + 1
    n = n - 1
    s = 0


print(counter)






