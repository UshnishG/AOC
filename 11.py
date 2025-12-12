from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

# Read and parse input
graph = defaultdict(list)
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        device, outputs = line.split(":")
        outs = outputs.strip().split()
        graph[device.strip()] = outs

# DFS with memoization
memo = {}

def count_paths(node):
    if node == "out":
        return 1
    if node in memo:
        return memo[node]
    
    total = 0
    for nxt in graph[node]:
        total += count_paths(nxt)
    
    memo[node] = total
    return total

# Compute answer
answer = count_paths("you")
print("Total paths from 'you' to 'out':", answer)
