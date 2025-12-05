def merge_ranges(ranges):
    ranges.sort()
    merged = [ranges[0]]

    for curr in ranges[1:]:
        prev = merged[-1]
        if curr[0] <= prev[1] + 1:  # overlapping or adjacent
            merged[-1] = (prev[0], max(prev[1], curr[1]))
        else:
            merged.append(curr)
    return merged

def main():
    ranges = []

    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f]

    # First section before blank line = ranges
    blank_index = lines.index("")
    range_lines = lines[:blank_index]

    # Parse the ranges
    for r in range_lines:
        a, b = map(int, r.split('-'))
        ranges.append((a, b))

    # Merge ranges
    ranges = merge_ranges(ranges)

    # Count total IDs covered
    total_ids = sum(high - low + 1 for low, high in ranges)

    print(total_ids)

if __name__ == "__main__":
    main()
