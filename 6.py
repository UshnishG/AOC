def parse_and_solve(lines):
    # Strip trailing newlines but keep spacing
    lines = [line.rstrip("\n") for line in lines]
    if not lines:
        return 0

    # Make all lines the same length by right-padding with spaces
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    H = len(lines)
    W = len(lines[0])

    # 1. Find separator columns (columns that are all spaces)
    separator = [all(lines[r][c] == " " for r in range(H)) for c in range(W)]

    # 2. Find problem bands: contiguous stretches of non-separator columns
    bands = []
    c = 0
    while c < W:
        # Skip separator columns
        while c < W and separator[c]:
            c += 1
        if c >= W:
            break
        start = c
        while c < W and not separator[c]:
            c += 1
        end = c - 1
        bands.append((start, end))

    op_line = lines[-1]
    total = 0

    # 3. Process each band
    for start, end in bands:
        # Find operator within this band on the bottom line
        op = None
        for c in range(start, end + 1):
            if op_line[c] in "+*":
                op = op_line[c]
                break
        if op is None:
            # No operator: skip (just in case, though puzzle says there will be one)
            continue

        nums = []
        # Collect numbers from all lines except the operator line
        for r in range(H - 1):
            segment = lines[r][start:end + 1].strip()
            if segment:
                nums.append(int(segment))

        if not nums:
            continue

        # 4. Evaluate this problem
        if op == "+":
            result = sum(nums)
        else:  # op == "*"
            result = 1
            for n in nums:
                result *= n

        total += result

    return total


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    answer = parse_and_solve(lines)
    print("Grand total:", answer)
