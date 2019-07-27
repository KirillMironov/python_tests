a, b = input().split(' ')
a = int(a)
b = int(b)
counter = 0

while a <= b:
    a *= 3
    b *= 2
    counter += 1

print(counter)
