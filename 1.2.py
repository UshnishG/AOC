def count_zero_clicks(lines):
    pos = 50          # starting position
    total_zeros = 0   # total times *any click* lands on 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        d = int(line[1:])

        if direction == "R":
            # first click index j0 that hits 0 when moving right
            if pos == 0:
                j0 = 100
            else:
                j0 = 100 - pos

            if d >= j0:
                total_zeros += 1 + (d - j0) // 100

            pos = (pos + d) % 100

        elif direction == "L":
            # first click index j0 that hits 0 when moving left
            if pos == 0:
                j0 = 100
            else:
                j0 = pos

            if d >= j0:
                total_zeros += 1 + (d - j0) // 100

            pos = (pos - d) % 100

        else:
            raise ValueError(f"Unknown direction in line: {line}")

    return total_zeros

# If your puzzle input is in input.txt:
with open("input.txt") as f:
    lines = f.readlines()

answer = count_zero_clicks(lines)
print("Password (method 0x434C49434B):", answer)
