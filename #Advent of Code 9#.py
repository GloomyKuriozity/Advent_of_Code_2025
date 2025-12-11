from collections import deque

with open('/home/robdev/Desktop/Advent of Code/Advent_of_Code_tiles.txt') as f:
    points = [tuple(map(int, line.split(','))) for line in f]

# Unique sorted X and Y coordinates of red tiles
xs = sorted(set(x for x, y in points))
ys = sorted(set(y for x, y in points))

W = len(xs)
H = len(ys)
print("Compressed W, H =", W, H)

# Maps from original coord -> compressed index
x_idx = {x: i for i, x in enumerate(xs)}
y_idx = {y: i for i, y in enumerate(ys)}

# Compressed grid: '.' initially
grid = [['.' for _ in range(W)] for _ in range(H)]

# Mark red tiles ('#') at their compressed positions
for x, y in points:
    cx = x_idx[x]
    cy = y_idx[y]
    grid[cy][cx] = '#'

# Draw green boundary segments ('X') between consecutive red tiles (wrap around)
n = len(points)
for idx in range(n):
    x1, y1 = points[idx]
    x2, y2 = points[(idx + 1) % n]

    cx1, cy1 = x_idx[x1], y_idx[y1]
    cx2, cy2 = x_idx[x2], y_idx[y2]

    if cx1 == cx2:
        # vertical segment in compressed grid
        y_start, y_end = sorted((cy1, cy2))
        for cy in range(y_start + 1, y_end):
            if grid[cy][cx1] == '.':
                grid[cy][cx1] = 'X'
    elif cy1 == cy2:
        # horizontal segment in compressed grid
        x_start, x_end = sorted((cx1, cx2))
        for cx in range(x_start + 1, x_end):
            if grid[cy1][cx] == '.':
                grid[cy1][cx] = 'X'
    else:
        raise ValueError("Well damn.")

# Flood-fill from the compressed border to mark outside as 'O'
q = deque()
for x in range(W):
    q.append((0, x))
    q.append((H - 1, x))
for y in range(H):
    q.append((y, 0))
    q.append((y, W - 1))

while q:
    cy, cx = q.popleft()
    if not (0 <= cy < H and 0 <= cx < W):
        continue
    if grid[cy][cx] != '.':
        continue
    grid[cy][cx] = 'O'
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        q.append((cy + dy, cx + dx))

# Remaining '.' are inside → make them green 'X'
for cy in range(H):
    for cx in range(W):
        if grid[cy][cx] == '.':
            grid[cy][cx] = 'X'

# Build valid mask in compressed grid: 1 if red or green, else 0
valid = [[1 if grid[cy][cx] in ('#', 'X') else 0 for cx in range(W)] for cy in range(H)]

# 2D prefix sum over compressed grid
ps = [[0] * (W + 1) for _ in range(H + 1)]
for cy in range(H):
    row_sum = 0
    for cx in range(W):
        row_sum += valid[cy][cx]
        ps[cy + 1][cx + 1] = ps[cy][cx + 1] + row_sum

def rect_sum(cx1, cy1, cx2, cy2):
    # compressed indices, inclusive
    return (
        ps[cy2 + 1][cx2 + 1]
        - ps[cy1][cx2 + 1]
        - ps[cy2 + 1][cx1]
        + ps[cy1][cx1]
    )

max_area = 0

# For rectangles, we still use *real* coordinates for area,
# but use compressed indices for the validity check.
for i in range(len(points)):
    x1, y1 = points[i]
    cx1, cy1 = x_idx[x1], y_idx[y1]
    for j in range(i + 1, len(points)):
        x2, y2 = points[j]
        cx2, cy2 = x_idx[x2], y_idx[y2]

        c_xmin, c_xmax = sorted((cx1, cx2))
        c_ymin, c_ymax = sorted((cy1, cy2))

        # Number of compressed cells in that rectangle
        cells = (c_xmax - c_xmin + 1) * (c_ymax - c_ymin + 1)
        inside_cells = rect_sum(c_xmin, c_ymin, c_xmax, c_ymax)

        if inside_cells == cells:
            # Entire compressed rectangle lies in red/green region
            # Area in *original* coordinates:
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            if area > max_area:
                max_area = area

print(max_area)

"""max_area = 0

for i in range(len(points)):
    x1, y1 = points[i]
    for j in range(i + 1, len(points)):
        x2, y2 = points[j]

        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        area = width * height

        if area > max_area:
            max_area = area

print(max_area)"""
