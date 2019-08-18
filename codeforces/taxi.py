n = int(input())
s = list(input().split(' '))
s = [int(item) for item in s]
s.sort(reverse=True)
temp = 0
counter = 0


def find_number(number):
    for j in range(len(s)):
        if s[j] == number:
            s[j] = 0
            return True
    return False


def search():
    global temp

    for i in range(len(s)):
        if s[i] == 0:   # For 0
            continue

        if s[i] == 4:   # For 4
            temp += 1
            s[i] = 0
            continue

        if s[i] == 3:   # For 3
            find_number(1)
            s[i] = 0
            temp += 1
            continue

        if s[i] == 2:   # For 2
            s[i] = 0
            if find_number(2):
                find_number(2)
                temp += 1
                continue
            elif find_number(1):
                find_number(1)
                find_number(1)
                s[i] = 0
                temp += 1
                continue
            else:
                temp += 1
                continue

        if s[i] == 1:   # For 1
            s[i] = 0
            if find_number(3):
                find_number(3)
                temp += 1
                continue
            elif find_number(2):
                find_number(2)
                find_number(1)
                temp += 1
                continue
            elif find_number(1):
                find_number(1)
                find_number(1)
                find_number(1)
                temp += 1
                continue
            else:
                temp += 1
                continue

    return temp


print(s)
print(search())


# 78
# 2 2 2 2 3 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 2 3 2 2 2 2 2 2 2 1 1 2 2 2 2 2 2 2 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
