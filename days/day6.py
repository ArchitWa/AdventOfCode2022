inp = open('data/day_6_input.txt')


def part1():
    a = inp.readline().strip()
    for i in range(len(a) - 4):
        if len(set(a[i:i+4])) == 4:
            print(i + 4)
            break

def part2():
    a = inp.readline().strip()
    for i in range(len(a) - 4):
        if len(set(a[i:i+14])) == 14:
            print(i + 14)
            break
part1()