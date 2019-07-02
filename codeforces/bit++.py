n = int(input())
x = 0

while n > 0:
    temp = input()
    if temp == '++X':
        x = x + 1
    elif temp == 'X++':
        x = x + 1
    else:
        x = x - 1
    n = n - 1

print(x)

