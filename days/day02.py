

inp = open('data/day_2_input.txt')

PTS = {
    "A" : 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

RES = {
    "A": {"X": 3, "Y": 6, "Z": 0}, 
    "B": {"X": 0, "Y": 3, "Z": 6}, 
    "C": {"X": 6, "Y": 0, "Z": 3}
}

LS = {
    "A": 3,
    "B": 1,
    "C": 2
}
WS = {
    "A": 2,
    "B": 3,
    "C": 1,
}


def part1():
    print(sum(PTS[line[2]] + RES[line[0]][line[2]] for line in inp.readlines()))
    

def part2():
    s = 0
    for line in inp.readlines():
        if line[2] == 'X':
            s += LS[line[0]]
        elif line[2] == 'Y':
            s += 3 + PTS[line[0]]
        else:
            s += 6 + WS[line[0]]
    
    print(s)

#part1()
part2()
