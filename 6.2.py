def solve_cephalopod_part2(lines):
    # Keep spacing exactly, just strip newlines
    lines = [line.rstrip("\n") for line in lines]
    if not lines:
        return 0

    # Make all lines same width by padding with spaces on the right
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    H = len(lines)
    W = len(lines[0])

    # 1. Separator columns = all spaces in that column
    separator = [all(lines[r][c] == " " for r in range(H)) for c in range(W)]

    # 2. Bands = contiguous runs of non-separator columns
    bands = []
    c = 0
    while c < W:
        while c < W and separator[c]:
            c += 1
        if c >= W:
            break
        start = c
        while c < W and not separator[c]:
            c += 1
        end = c - 1
        bands.append((start, end))

    op_line = lines[-1]   # bottom row has operators
    total = 0

    # 3. Process each band (one problem per band)
    for start, end in bands:
        # Operator for this problem (anywhere in the band on the bottom line)
        op = None
        for col in range(start, end + 1):
            if op_line[col] in "+*":
                op = op_line[col]
                break
        if op is None:
            continue  # should not happen in valid input

        numbers = []

        # 4. Each column in the band is one number (digits top→bottom)
        for col in range(start, end + 1):
            digits = []
            for row in range(H - 1):  # exclude bottom operator row
                ch = lines[row][col]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                num = int("".join(digits))
                numbers.append(num)

        if not numbers:
            continue

        # 5. Evaluate this problem
        if op == "+":
            result = sum(numbers)
        else:  # op == "*"
            result = 1
            for n in numbers:
                result *= n

        total += result

    return total


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    answer = solve_cephalopod_part2(lines)
    print("Grand total:", answer)
