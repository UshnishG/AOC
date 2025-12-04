position = 50
zeros = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])

        if direction == "R":
            position = (position + distance) % 100
        elif direction == "L":
            position = (position - distance) % 100
        else:
            raise ValueError(f"Unknown direction in line: {line}")

        if position == 0:
            zeros += 1

print("Password:", zeros)
