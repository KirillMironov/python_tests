def recursion(n):
    if n == 2:
        return print('YES')
    if n < 2:
        return print('NO')
    recursion(n/2)


recursion(128)
recursion(5)
recursion(32)
recursion(2)
