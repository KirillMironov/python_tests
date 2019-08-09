# task 1

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def print_elements(s):
    for i in s:
        if s[i] < 5:
            print(s[i])
        else:
            break


def print_elements_short(s):
    print([elem for elem in s if elem < 5])


print_elements(a)
print_elements_short(a)
print('--------------')

# task 2

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []
a = a + b
a.sort()


def duplicates(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            result.append(s[i])
    print(set(result))


duplicates(a)












