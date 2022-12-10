pr = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1():
    inp = open("data/day_3_input.txt")

    s = 0
    for line in inp.readlines():
        start = line[:int(len(line) / 2)]
        end = line[int((len(line) / 2)):]
        l = ""
        for i in start:
            if i in end:
                l = i
        s += pr.index(l)
    print(s)

def part2():
    inp = open("data/day_3_input.txt")

    c = 0
    temp_lines = []
    s = 0
    for line in inp.readlines():
        line = line.strip()
        if c < 3:
            temp_lines.append(line)
            c += 1
        if c == 3:
            c = 0
            l = ''
            for i in temp_lines[0]:
                if i in temp_lines[1] and i in temp_lines[2]:
                    l = i
            temp_lines = []
            s += pr.index(l)
    print(s)

part1()
part2()