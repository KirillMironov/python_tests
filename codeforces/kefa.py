import sys

n = int(input())
a = list(input().split(' '))
output = []

if n == 1:
    print(1)
    sys.exit(0)


def find(array):
    temp = 1
    if len(array) == 1:
        output.append(1)
        return
    else:
        for i in range(len(array)-1):
            if int(array[i]) <= int(array[i+1]):
                temp += 1
                if i == len(array)-2:
                    output.append(temp)
                    del array[0:len(array)]
                    return
            else:
                output.append(temp)
                del array[0:i+1]
                break
    if len(array) > 0:
        find(array)
    else:
        return


find(a)
output.sort(reverse=True)
print(output[0])
