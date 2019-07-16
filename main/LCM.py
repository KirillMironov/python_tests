a = int(input())
b = int(input())
aa = a
bb = b

while True:
    if a != b:
        if a < b:
            a += aa
        else:
            b += bb
    else:
        print('Result:', a)
        break
