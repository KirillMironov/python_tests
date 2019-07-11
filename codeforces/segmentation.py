tokens = ['4', '7', '']

lucky_nums = [int(x + y + z) for x in tokens for y in tokens for z in tokens if len(x+y+z) > 0]

n = int(input())

lucky = 'NO'
for num in lucky_nums:
    if n % num == 0:
        lucky = 'YES'
        break

print(lucky)


