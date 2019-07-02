a = input()
inp = list(a)
tem = 1
i = len(inp) - 1

while i > 0:
    if inp[i] == inp[i-1]:
        tem += 1
    elif tem < 6:
        tem = 0
    i -= 1

if inp[0] == inp[1] == inp[2] == inp[3] == inp[4] == inp[5] == inp[6]:
    tem += 1

if tem > 6:
    print('YES')
else:
    print('NO')







