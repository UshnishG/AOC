with open("input.txt") as f:
    *shapes, regions = f.read().strip().split("\n\n")

sizes = [sum(c == "#" for c in shape) for shape in shapes]

part1 = 0
for region in regions.split("\n"):
    w, h, *nums = map(int, region.replace("x", " ").replace(":", "").split(" "))
    if w * h >= sum(n * size for n, size in zip(nums, sizes)):
        part1 += 1

print(part1)