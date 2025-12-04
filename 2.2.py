def parse_ranges(line: str):
    ranges = []
    for part in line.strip().split(","):
        if not part:
            continue  # handles optional trailing comma
        start_str, end_str = part.split("-")
        ranges.append((int(start_str), int(end_str)))
    return ranges


def merge_ranges(ranges):
    ranges = sorted(ranges)
    merged = []
    for a, b in ranges:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)
    return merged


def in_any_range(x, merged):
    # binary search in merged, non-overlapping ranges
    lo, hi = 0, len(merged) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        a, b = merged[mid]
        if x < a:
            hi = mid - 1
        elif x > b:
            lo = mid + 1
        else:
            return True
    return False


def sum_invalid_ids_part2(ranges):
    merged = merge_ranges(ranges)
    lo = min(a for a, b in ranges)
    hi = max(b for a, b in ranges)
    max_len = len(str(hi))

    invalid_ids = set()

    # block length d, repetition count k >= 2
    for d in range(1, max_len // 2 + 1):
        start_block = 10 ** (d - 1)
        end_block = 10 ** d - 1
        max_k = max_len // d

        for h in range(start_block, end_block + 1):
            s = str(h)
            for k in range(2, max_k + 1):
                n_str = s * k
                n = int(n_str)

                if n > hi:
                    break  # larger k will only make n bigger

                if n < lo:
                    continue

                if in_any_range(n, merged):
                    invalid_ids.add(n)

    return sum(invalid_ids)


def main():
    with open("input.txt") as f:
        line = f.read().strip()

    ranges = parse_ranges(line)
    answer = sum_invalid_ids_part2(ranges)
    print("Sum of all invalid IDs (Part 2):", answer)


if __name__ == "__main__":
    main()
