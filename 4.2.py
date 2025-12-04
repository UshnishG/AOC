def neighbors(r, c, R, C):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                yield nr, nc

def count_accessible_and_remove(grid):
    R, C = len(grid), len(grid[0])
    to_remove = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] != '@':
                continue
            count_neighbors = 0
            for nr, nc in neighbors(r, c, R, C):
                if grid[nr][nc] == '@':
                    count_neighbors += 1
            if count_neighbors < 4:
                to_remove.append((r, c))


    for r, c in to_remove:
        grid[r][c] = '.'

    return len(to_remove)

def total_removed_rolls(grid_lines):
    grid = [list(line.strip()) for line in grid_lines if line.strip()]
    total_removed = 0

    while True:
        removed_this_round = count_accessible_and_remove(grid)
        if removed_this_round == 0:
            break
        total_removed += removed_this_round

    return total_removed

with open("input.txt") as f:
    lines = f.readlines()

print(total_removed_rolls(lines))
