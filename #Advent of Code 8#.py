with open('/home/robdev/Desktop/Advent of Code/Advent_of_Code_junction_boxes.txt') as f:
    lines = [line.strip() for line in f]

rows = [list(map(int, line.split(','))) for line in lines]

def dist2(a, b):
    return ((a[0] - b[0]) ** 2
          + (a[1] - b[1]) ** 2
          + (a[2] - b[2]) ** 2)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False   # already in same set

        # union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True       # successfully merged


edges = []
for i in range(len(rows)):
    for j in range(i+1, len(rows)):  # i < j to avoid duplicates/self
        d = dist2(rows[i], rows[j])
        edges.append((d, i, j))


edges.sort(key=lambda e: e[0])

N = len(rows)
dsu = DSU(N)

"""for idx, (d, i, j) in enumerate(edges):
    if idx == 1000:        # after 1000 edges, stop
        break
    dsu.union(i, j)        # we don't care if it merges or not
"""
successful = 0
last_edge = None

for d, i, j in edges:
    if dsu.union(i, j):        # ONLY count successful unions
        successful += 1
        last_edge = (i, j)

        if successful == N - 1:
            break

i, j = last_edge
answer = rows[i][0] * rows[j][0]   # X coordinates
print(answer)

""" components = {}
for i in range(N):
    root = dsu.find(i)
    components[root] = dsu.size[root]

sizes = sorted(components.values(), reverse=True)
answer = sizes[0] * sizes[1] * sizes[2]
print(answer)  """



