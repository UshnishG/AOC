def max_two_digit(line):
    digits = list(map(int, line.strip()))
    n = len(digits)

    # Precompute max digit to the right for each position
    max_right = [0] * n
    max_right[-1] = -1  # No digit to the right of last
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], digits[i + 1])

    best = -1
    for i in range(n - 1):
        if max_right[i] != -1:   # there is at least one digit to the right
            best = max(best, 10 * digits[i] + max_right[i])

    return best


total = 0
with open("input.txt") as f:      # <- replace with your file name or input method
    for line in f:
        total += max_two_digit(line)

print(total)
