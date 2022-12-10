def part1(pts, line, s):
    if line[0] == 'A':
        if line[2] == 'Y':
            s += pts[line[2]] + 6
        elif line[2] == 'X':
            s += pts[line[2]] + 3
        else:
            s += 3
    if line[0] == 'B':
        if line[2] == 'Z':
            s += pts[line[2]] + 6
        elif line[2] == 'Y':
            s += pts[line[2]] + 3
        else:
            s += 1
    if line[0] == 'C':
        if line[2] == 'X':
            s += pts[line[2]] + 6
        elif line[2] == 'Z':
            s += pts[line[2]] + 3
        else:
            s += 2

def solve():
    inp = open('data/day_2_input.txt', "r")

    pts = {
        "A" : 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    ls = {
        "A": 3,
        "B": 1,
        "C": 2
    }
    ws = {
        "A": 2,
        "B": 3,
        "C": 1,
    }

    s = 0
    for line in inp.readlines():
        if line[2] == 'X':
            s += ls[line[0]]
        elif line[2] == 'Y':
            s += 3 + pts[line[0]]
        else:
            s += 6 + ws[line[0]]
    
    print(s)


solve()