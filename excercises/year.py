a = int(input())
if a // 4 == 0 and a // 100 != 0:
    print("YES")
if a // 400 == 0:
    print("YES")
if a // 100 != 0:
    print("NO")
