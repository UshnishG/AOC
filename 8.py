from math import sqrt
from itertools import combinations

# ---------- Load points ----------
points = []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))

n = len(points)

# ---------- Disjoint Set Union ----------
parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path compression
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False  # already connected
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

# ---------- Build all pairs with squared distance ----------
edges = []
for i in range(n):
    x1, y1, z1 = points[i]
    for j in range(i + 1, n):
        x2, y2, z2 = points[j]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        dist2 = dx*dx + dy*dy + dz*dz
        edges.append((dist2, i, j))

# Sort by distance squared
edges.sort(key=lambda e: e[0])

# ---------- Process the 1000 closest pairs ----------
pairs_to_process = 1000
processed = 0
idx = 0

while processed < pairs_to_process and idx < len(edges):
    _, i, j = edges[idx]
    # We "attempt" this connection regardless of whether it merges anything
    union(i, j)
    processed += 1
    idx += 1

# ---------- Compute component sizes ----------
# Root -> total size
component_sizes = {}
for i in range(n):
    r = find(i)
    component_sizes[r] = component_sizes.get(r, 0) + 1

sizes = sorted(component_sizes.values(), reverse=True)
if len(sizes) < 3:
    raise ValueError("Less than 3 components; unexpected for this puzzle.")

answer = sizes[0] * sizes[1] * sizes[2]
print("Three largest circuit sizes:", sizes[0], sizes[1], sizes[2])
print("Answer:", answer)
