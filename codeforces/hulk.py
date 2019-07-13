n = int(input())
output = ''

for i in range(n):
    if i % 2 == 0:
        output += 'I hate '
    elif i % 2 != 0:
        output += 'I love '

    if i != n-1:
        output += 'that '
    elif i == n-1:
        output += 'it'

print(output)




