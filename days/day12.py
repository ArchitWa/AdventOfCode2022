# aocd > data/day_12_input.txt
# python submit.py 12 a _
# python submit.py 12 b _ 
from collections import deque


inp = open("data/day_12_input.txt")


lines = inp.readlines()
h_map = [[*line.strip()] for line in lines]

rows = len(h_map)
cols = len(h_map[0])

elevations = "abcdefghijklmnopqrstuvwxyz"

start = None
end = None
starts = []
for i in range(len(h_map)):
    for j in range(len(h_map[i])):
        if h_map[i][j] == "a":
            starts.append((i, j))
        if h_map[i][j] == "S":
            start = (i, j)
            starts.append(start)
            h_map[i][j] = "a"
        if h_map[i][j] == "E":
            end = (i, j)
            h_map[i][j] = "z"


def part1(start):
    nodes = deque()
    seen = set()
    nodes.append((start, 0))
    while nodes:
        (i, j), dist = nodes.popleft()
        if (i, j) in seen:
            continue
        seen.add((i, j))

        if i == end[0] and j == end[1]:
            return dist
        
        if 0 <= i - 1 < rows and 0 <= j < cols and elevations.index(h_map[i][j]) + 1 >= elevations.index(h_map[i-1][j]):
            nodes.append(((i - 1, j), dist + 1))
        if 0 <= i + 1 < rows and 0 <= j < cols and elevations.index(h_map[i][j]) + 1 >= elevations.index(h_map[i+1][j]):
            nodes.append(((i + 1, j), dist + 1))
        if 0 <= i < rows and 0 <= j - 1 < cols and elevations.index(h_map[i][j]) + 1 >= elevations.index(h_map[i][j-1]):
            nodes.append(((i, j - 1), dist + 1))
        if 0 <= i < rows and 0 <= j + 1 < cols and elevations.index(h_map[i][j]) + 1 >= elevations.index(h_map[i][j+1]):
            nodes.append(((i, j + 1), dist + 1))
        
def part2():
    steps_list = []
    for start in starts:
        steps_list.append(part1(start))
    steps_list = [i for i in steps_list if i is not None]
    print(min(steps_list))

part2()



