def max_k_digit_number(line, k):
    """
    Given a string of digits `line`, choose exactly k digits in order
    to form the lexicographically largest possible number.
    """
    digits = line.strip()
    n = len(digits)
    remove = n - k               # how many digits we are allowed to drop
    stack = []

    for ch in digits:
        # While we can still remove digits and the last one in the stack
        # is smaller than the current, pop it to make the number larger.
        while remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    # If we still have removals left (digits never popped at the end),
    # drop them from the right.
    if remove > 0:
        stack = stack[:-remove]

    # Now stack length is exactly k
    return int("".join(stack[:k]))


def total_output_joltage(filename, k=12):
    total = 0
    with open(filename) as f:
        for line in f:
            if line.strip():  # skip empty lines just in case
                total += max_k_digit_number(line, k)
    return total


if __name__ == "__main__":
    # Change "input.txt" to your actual input file name
    print(total_output_joltage("input.txt", k=12))
