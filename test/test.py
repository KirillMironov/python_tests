alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

a = list(str(input()))
res = ''


def ret_index(elm):
    for index in range(len(alphabet)):
        if elm == alphabet[index]:
            if index < 24:
                return alphabet[index+2]
            elif index == 24:
                return alphabet[0]
            elif index == 25:
                return alphabet[1]


for i in range(len(a)):
    if a[i] in alphabet:
        a[i] = ret_index(a[i])
    else:
        continue

print(*a)

