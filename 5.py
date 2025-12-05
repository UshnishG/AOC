def merge_ranges(ranges):
    ranges.sort()
    merged = [ranges[0]]

    for curr in ranges[1:]:
        prev = merged[-1]
        # If ranges overlap or touch, merge them
        if curr[0] <= prev[1] + 1:
            merged[-1] = (prev[0], max(prev[1], curr[1]))
        else:
            merged.append(curr)

    return merged

def is_fresh(id_value, ranges):
    # binary search for efficiency
    import bisect
    starts = [r[0] for r in ranges]
    pos = bisect.bisect_right(starts, id_value) - 1

    if pos >= 0:
        low, high = ranges[pos]
        return low <= id_value <= high
    return False

def main():
    ranges = []
    ids = []

    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f]

    # Split based on the blank line
    blank_index = lines.index("")

    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    # Parse ranges
    for r in range_lines:
        a, b = map(int, r.split('-'))
        ranges.append((a, b))

    # Parse IDs
    for idv in id_lines:
        if idv.strip() != "":
            ids.append(int(idv))

    # Merge overlapping ranges
    ranges = merge_ranges(ranges)

    # Count fresh IDs
    fresh_count = sum(1 for v in ids if is_fresh(v, ranges))

    print(fresh_count)

if __name__ == "__main__":
    main()
