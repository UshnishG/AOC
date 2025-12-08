from math import sqrt
from collections import Counter

# -----------------------------
# Parsing
# -----------------------------
def parse_input(filename: str):
    points = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y, z = map(int, line.split(","))
            points.append((x, y, z))
    return points

# -----------------------------
# Build all pair distances
# -----------------------------
def build_pairs(points):
    pairs = []
    n = len(points)
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d = sqrt(dx*dx + dy*dy + dz*dz)
            pairs.append((d, i, j))
    return pairs

# -----------------------------
# Union-Find (Disjoint Set)
# -----------------------------
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
            return False   # no merge
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True        # merged

# -----------------------------
# Part 1
# -----------------------------
def solve_part1(points, pairs):
    pairs_sorted = sorted(pairs, key=lambda x: x[0])
    n = len(points)
    dsu = DSU(n)

    # Connect the first 1000 useful pairs
    count = 0
    idx = 0
    while count < 1000 and idx < len(pairs_sorted):
        _, i, j = pairs_sorted[idx]
        if dsu.union(i, j):
            count += 1
        idx += 1

    # compute component sizes
    roots = [dsu.find(i) for i in range(n)]
    comp = Counter(roots)
    sizes = sorted(comp.values(), reverse=True)

    # largest 3
    while len(sizes) < 3:
        sizes.append(1)

    return sizes[0] * sizes[1] * sizes[2]

# -----------------------------
# Part 2
# -----------------------------
def solve_part2(points, pairs):
    pairs_sorted = sorted(pairs, key=lambda x: x[0])
    n = len(points)
    dsu = DSU(n)

    components = n
    last_pair = None

    for d, i, j in pairs_sorted:
        if dsu.union(i, j):
            components -= 1
            last_pair = (i, j)
            if components == 1:
                break

    i, j = last_pair
    x1, _, _ = points[i]
    x2, _, _ = points[j]
    return x1 * x2

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    points = parse_input("input.txt")
    pairs = build_pairs(points)

    part1 = solve_part1(points, pairs)
    print("Part 1:", part1)

    part2 = solve_part2(points, pairs)
    print("Part 2:", part2)
