inp = open('data/day_4_input.txt')

def part1():
    c = 0
    for line in inp.readlines():
        a1, a2, b1, b2 = list(map(int, line.replace(",", "-").split("-")))
        if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
            c += 1
    print(c)

def part2():
    c = 0
    for line in inp.readlines():
        a1, a2, b1, b2 = list(map(int, line.replace(",", "-").split("-")))
        if (a1 >= b1 and a1 <= b2) or (b1 >= a1 and b1 <= a2):
            c += 1
    print(c)

part2()
