inp = open("data/day_3_input.txt")
PR = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1():
    s = 0
    for line in inp.readlines():
        start, end = line[:int(len(line) / 2)], line[int((len(line) / 2)):]
        l = list(set(start).intersection(end))[0]
        s += PR.index(l)
    print(s)

def part2():
    s = 0
    lines = [line.strip() for line in inp.readlines()]
    for i in range(0, len(lines) - 2, 3):
        l = list(set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2]))[0]
        s += PR.index(l)
    print(s)

# part1()
part2()