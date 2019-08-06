import sys

n = int(input())
s = list(input().split(' '))
s = [int(item) for item in s]
s.sort(reverse=True)
temp = 0
count = 0


def check_len(array):
    if len(array) > 0:
        return 1
    else:
        return 0


def search(a):
    global temp
    global count
    count = 0
    for i in range(len(a)):
        count = 0

        if a[i] == 4:   # For 4
            temp += 1

        if a[i] == 3:   # For 3
            del a[i]
            temp += 1
            for j in range(len(a)):
                if a[j] == 1:
                    del a[j]
                    if check_len(a) == 1:
                        return search(a)
                    else:
                        print(temp)
                        sys.exit(0)

        if a[i] == 2:   # For 2
            count += a[i]
            del a[i]
            temp += 1
            for k in range(len(a)):
                if a[k] == 2:
                    count += a[k]
                    del a[k]
                    if check_len(a) == 1:
                        return search(a)
                    else:
                        print(temp)
                        sys.exit(0)
            for l in range(len(a)):
                if a[l] == 1 and count <= 4:
                    del a[l]

        if a[i] == 1:   # For 1
            count += a[i]
            del a[i]
            for t in range(len(a)):
                if a[t] == 3:
                    count += a[t]
                    del a[t]
                    temp += 1
            for y in range(len(a)):
                if a[y] == 2 and count <= 4:
                    count += a[y]
                    del a[y]
            for o in range(len(a)):
                if a[o] == 1 and count <= 4:
                    del a[o]

        if check_len(a) == 1:
            return search(a)
        else:
            print(temp)
            sys.exit(0)


search(s)



