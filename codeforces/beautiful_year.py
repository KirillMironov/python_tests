import sys

y = int(input()) + 1

while True:
    y = str(y)
    a = list(y)
    if len(a) == len(set(a)):
        print(y)
        sys.exit(0)
    else:
        y = int(y)
        y += 1



