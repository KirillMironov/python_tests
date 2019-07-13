inp = list(input())
counter = 0

for i in range(len(inp)):
    if inp[i] == 'H' or inp[i] == 'Q' or inp[i] == '9':
        counter = 1

if counter == 1:
    print('YES')
else:
    print('NO')

