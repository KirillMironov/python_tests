for i in range(int(input())):
    n = int(input())
    a = sorted(list(input().split(' ')), reverse=True)
    if len(a) == 2:
        print(0)
    else:
        print(min(int(a[1]) - 1, n - 2))







