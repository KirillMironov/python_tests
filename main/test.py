print('Введите строку:')
inp = input()
arr = []

for i in range(0, len(inp), 4):
    arr.append(int(inp[i]) * 60 + int(inp[i+2:i+4]))

s = sum(arr)/len(arr)
res = str(round(s // 60)) + ','

if int(s - 60 * (s // 60)) < 10:
    res += '0' + str(round(s - 60 * (s // 60)))
else:
    res += str(round(s - 60 * (s // 60)))

print('\n', res)


