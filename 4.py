def count_accessible_rolls(grid_lines):
    grid = [line.strip() for line in grid_lines if line.strip()]
    R, C = len(grid), len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    accessible = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] != '@':
                continue

            neighbor_rolls = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '@':
                    neighbor_rolls += 1

            if neighbor_rolls < 4:
                accessible += 1

    return accessible


# Example usage: reading from a file called "input.txt"
with open("input.txt") as f:
    lines = f.readlines()

print(count_accessible_rolls(lines))
