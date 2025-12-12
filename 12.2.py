import numpy as np

presents = []
problems = []
with open('input.txt', 'r') as f:
    present = []
    for line in f.readlines():
        if 'x' not in line:
            if '#' in line or '.' in line:
                present.append([1 if char == '#' else 0 for char in line.strip()])
            elif not line.strip():
                presents.append(np.array(present))
                present = []
        else:
            tokens = line.strip().split()
            width, height = (int(x) for x in tokens[0][:-1].split('x'))
            present_counts = tuple(int(x) for x in tokens[1:])
            problems.append((width, height, present_counts))

present_orientations = []
for present in presents:
    orients = []
    temp = present.copy()
    for _ in range(4):
        orients.append(temp)
        temp = np.rot90(temp)
    temp = np.flip(temp)
    for _ in range(4):
        orients.append(temp)
        temp = np.rot90(temp)
    present_orientations.append(np.unique(orients, axis=0))

def solve(width, height, present_counts):
    spaces = width*height
    present_spaces = 0
    for i, count in enumerate(present_counts):
        present_size = np.sum(presents[i])
        present_spaces += (present_size*count)
    if present_spaces > spaces:
        return False

    start_state = (np.zeros((height, width)), present_counts)
    q = [start_state]
    visited = set()
    while q:
        current_m, current_present_counts = q.pop()
        rep = str(current_m)
        if (rep, current_present_counts) in visited:
            continue
        visited.add((rep, current_present_counts))

        for iter, count in enumerate(current_present_counts):
            if count != 0:
                break
        orients = present_orientations[iter]
        for p in orients:
            done = False
            for i in range(height - 2):
                if done:
                    break
                for j in range(width - 2):
                    new_m = current_m.copy()
                    new_m[i:i+3, j:j+3] += p
                    if not np.all(new_m <= 1):
                        continue
                    new_present_counts = list(current_present_counts)
                    new_present_counts[iter] -= 1
                    new_present_counts = tuple(new_present_counts)
                    if all(x == 0 for x in new_present_counts):
                        return True
                    if (str(new_m), new_present_counts) in visited:
                        continue
                    q.append((new_m, new_present_counts))
                    if j == 0:
                        done = True
                    break
    return False

result = 0
for width, height, present_counts in problems:
    s = solve(width, height, present_counts)
    result += s
print(result)