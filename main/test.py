print('Введите строку:')
inp = input()
arr = []
s = 0

for i in range(0, len(inp), 7):
    arr.append(int(inp[i])*60+int(inp[i+2:i+4]))
    # print(float(inp[i:i+4]))
    # print(inp[i]+':'+inp[i+2:i+4]+'.'+'00')


print("\n", sum(arr)/len(arr))
print(len(arr))

