def parse_ranges(line: str):
    ranges = []
    for part in line.strip().split(","):
        if not part:
            continue  # handles trailing comma
        start_str, end_str = part.split("-")
        ranges.append((int(start_str), int(end_str)))
    return ranges


def sum_invalid_ids(ranges):
    # global min & max over all ranges
    lo = min(a for a, b in ranges)
    hi = max(b for a, b in ranges)

    invalid_ids = set()

    max_digits = len(str(hi))

    # Only even total lengths: 2, 4, 6, ...
    for total_len in range(2, max_digits + 1, 2):
        half_len = total_len // 2

        # h has half_len digits, so its first digit can't be 0
        start = 10 ** (half_len - 1)
        end = 10 ** half_len - 1

        for h in range(start, end + 1):
            s = str(h)
            n = int(s + s)  # doubled pattern

            if n < lo:
                continue
            if n > hi:
                break  # further h will only make n larger

            # Check if n is in any of the ranges
            for a, b in ranges:
                if a <= n <= b:
                    invalid_ids.add(n)
                    break

    return sum(invalid_ids)


def main():
    with open("input.txt") as f:
        line = f.read().strip()

    ranges = parse_ranges(line)
    answer = sum_invalid_ids(ranges)
    print("Sum of all invalid IDs:", answer)


if __name__ == "__main__":
    main()
