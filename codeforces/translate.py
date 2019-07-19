import sys

s = list(input())
t = list(input())
t.reverse()

if s == t:
    print('YES')
else:
    print('NO')

# for i in range(len(s)):
#     if s[i] != t[i]:
#         print('NO')
#         sys.exit(0)
#
# print('YES')



