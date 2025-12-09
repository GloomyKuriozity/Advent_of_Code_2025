import numpy as np

matrix = []
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]
result = 0
ting = 1

def neighbors(matrix, r, c):
    rows = len(matrix)
    cols = len(matrix[0])

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield matrix[nr][nc], nr, nc

def count_neighbors(matrix, r, c, target):
    count = 0
    for val, nr, nc in neighbors(matrix, r, c):
        if val == target:
            count += 1
    return count

with open('/home/robdev/Desktop/Advent of Code/Advent_of_Code_rolls_location.txt') as f:
    for line in f:
        line = line.strip() 
        matrix.append(list(line))  

while(ting == 1):
    ting = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '@': 
                n = count_neighbors(matrix, r=i, c=j, target='@')
                if n < 4:
                    ting = 1
                    result += 1
                    matrix[i][j] = '.'

print(result)




