with open('/home/robdev/Desktop/Advent of Code/Advent_of_Code_tachyon.txt') as f:
    lines = [line.strip() for line in f]

rows = [list(line) for line in lines]
#Part 1
"""
H, W = len(rows), len(rows[0])
visited = set()

from collections import deque

# find S
start_r = start_c = None
for i in range(H):
    for j in range(W):
        if rows[i][j] == 'S':
            start_r, start_c = i, j
            break
    if start_r is not None:
        break

splits = 0
q = deque()

q.append((start_r + 1, start_c))

while q:
    r, c = q.popleft()

    if not (0 <= r < H and 0 <= c < W):
        continue

    if (r, c) in visited:
        continue
    visited.add((r, c))

    cell = rows[r][c]

    if cell == '.':
        q.append((r + 1, c))

    elif cell == '^':
        splits += 1

        # left beam
        if c - 1 >= 0:
            q.append((r, c - 1))

        # right beam
        if c + 1 < W:
            q.append((r, c + 1))

    elif cell == 'S':
        # treat S like empty space if ever hit from above (unlikely except weird inputs)
        q.append((r + 1, c))

print(splits)"""

#Part2
H, W = len(rows), len(rows[0])

# find S
for i in range(H):
    for j in range(W):
        if rows[i][j] == 'S':
            start_r, start_c = i, j
            break

# memo: ways to exit from (r,c)
memo = {}

def ways(r, c):
    # out of bounds => 1 timeline
    if r < 0 or r >= H or c < 0 or c >= W:
        return 1

    if (r, c) in memo:
        return memo[(r, c)]

    cell = rows[r][c]

    if cell == '.':
        result = ways(r + 1, c)

    elif cell == '^':
        result = 0
        result += ways(r, c - 1)   # left timeline
        result += ways(r, c + 1)   # right timeline

    elif cell == 'S':
        result = ways(r + 1, c)

    memo[(r, c)] = result
    return result

# start just below S
answer = ways(start_r + 1, start_c)

print(answer)
