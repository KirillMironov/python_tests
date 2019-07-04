matrix = []
counter = 0
position_i = 0
position_j = 0

for i in range(5):
    matrix.append([int(j) for j in input().split()])

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            position_i = i
            position_j = j

if position_i > 2:
    counter = position_i - 2
elif position_i < 2:
    counter = 2 - position_i

if position_j > 2:
    counter = counter + position_j - 2
elif position_j < 2:
    counter = counter + (2 - position_j)

print(counter)






