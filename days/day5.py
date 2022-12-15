inp = open('data/day_5_input.txt')
s1 = ["B", "Q", "C"]
s2 = ["R", "Q", "W", "Z"]
s3 = ["B", "M", "R", "L", "V"]
s4 = ["C", "Z", "H", "V", "T", "W"]
s5 = ["D", "Z", "H", "B", "N", "V", "G"]
s6 = ["H", "N", "P", "C", "J", "F", "V", "Q"]
s7 = ["D", "G", "T", "R", "W", "Z", "S"]
s8 = ["C", "G", "M", "N", "B", "W", "Z", "P"]
s9 = ["N", "J", "B", "M", "W", "Q", "F", "P"]
stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]


def part1():
    for line in inp.readlines():
        if line.startswith("move"):
            w = line.strip().split(" ")
            for _ in range(int(w[1])):
                stacks[int(w[5])-1].append(stacks[int(w[3]) - 1].pop())
    print("".join([stack.pop() for stack in stacks]))

def part2():
    for line in inp.readlines():
        if line.startswith("move"):
            w = line.strip().split(" ")
            for i in range(int(w[1])):
                stacks[int(w[5])-1].append(stacks[int(w[3]) - 1].pop(len(stacks[int(w[3]) - 1]) - int(w[1])+i))
    
    print("".join([stack.pop() for stack in stacks]))

part2()