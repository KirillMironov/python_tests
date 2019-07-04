a = input()
inp = list(a)

for i, ii in enumerate(inp):
    if inp[i] == '+':
        inp.remove(inp[i])

inp.sort()

for i, ii in enumerate(inp):
    if i % 2 != 0:
        inp.insert(i, '+')

print(''.join(inp))

