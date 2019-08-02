def recursion(a, b):
    if a > b:
        if a == b:
            return print(a)
        return print(a), recursion(a-1, b)
    else:
        if a == b:
            return print(a)
        return print(a), recursion(a+1, b)


recursion(5, 2)
print('-------------')
recursion(2, 5)






