k = int(input())
hours = k % (60 * 24) // 60
minutes = k % 60
print(hours, minutes)
