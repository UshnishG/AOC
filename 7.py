def count_splits(lines):
    # Remove only newline characters; keep spaces exactly
    lines = [line.rstrip("\n") for line in lines]
    if not lines:
        return 0

    H = len(lines)
    W = len(lines[0])

    # 1. Find S
    start_row = start_col = None
    for r, row in enumerate(lines):
        c = row.find("S")
        if c != -1:
            start_row, start_col = r, c
            break

    if start_row is None:
        raise ValueError("No S found in input")

    # 2. Initial beam: just below S
    beams = {(start_row + 1, start_col)}  # set of (row, col)
    splits = 0

    # 3. Simulate until no beams remain
    while beams:
        new_beams = set()
        for r, c in beams:
            # If beam is outside the manifold, it disappears
            if r < 0 or r >= H or c < 0 or c >= W:
                continue

            cell = lines[r][c]

            if cell == "." or cell == "S":
                # Beam continues straight down
                new_beams.add((r + 1, c))
            elif cell == "^":
                # Beam is split once here
                splits += 1
                # Original beam stops; two new beams come out below-left and below-right
                new_beams.add((r + 1, c - 1))
                new_beams.add((r + 1, c + 1))
            else:
                # If there are only '.', 'S', and '^', anything else is unexpected
                raise ValueError(f"Unexpected character {cell!r} at ({r}, {c})")

        # Merge beams that landed in the same place
        beams = new_beams

    return splits


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    answer = count_splits(lines)
    print("Number of splits:", answer)
