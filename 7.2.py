def count_quantum_timelines(lines):
    # Keep all spaces; just strip newline characters
    lines = [line.rstrip("\n") for line in lines]
    if not lines:
        return 0

    H = len(lines)
    W = len(lines[0])

    # 1. Find the starting position S
    sr = sc = None
    for r, row in enumerate(lines):
        c = row.find("S")
        if c != -1:
            sr, sc = r, c
            break

    if sr is None:
        raise ValueError("No 'S' found in input")

    # 2. Initial timelines: just below S
    start_row = sr + 1
    if start_row >= H:
        # S is on the bottom row; particle immediately exits
        return 1

    # current: mapping column -> number of timelines at this (row, col)
    current = {sc: 1}
    finished = 0

    # 3. Process each row from start_row downwards
    for r in range(start_row, H):
        new = {}

        for c, count in current.items():
            # If somehow outside horizontally, treat as already exited
            if c < 0 or c >= W:
                finished += count
                continue

            cell = lines[r][c]

            if cell in ".S":
                nr = r + 1
                if nr >= H:
                    # Exits below the manifold
                    finished += count
                else:
                    new[c] = new.get(c, 0) + count

            elif cell == "^":
                nr = r + 1
                # Each timeline splits into two: left and right
                for nc in (c - 1, c + 1):
                    if nr >= H or nc < 0 or nc >= W:
                        # That branch exits the manifold
                        finished += count
                    else:
                        new[nc] = new.get(nc, 0) + count

            else:
                raise ValueError(f"Unexpected character {cell!r} at ({r}, {c})")

        current = new

    # All timelines should have exited by now
    return finished


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    answer = count_quantum_timelines(lines)
    print("Total quantum timelines:", answer)
