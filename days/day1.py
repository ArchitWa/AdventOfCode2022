
inp = open('data/day_1_input.txt', "r")


def part1():
    print(max(sum(int(elf_cal) for elf_cal in elf.split()) for elf in inp.read().split("\n\n")))

def part2():
    elfs = [sum(int(elf_cal) for elf_cal in elf.split()) for elf in inp.read().split("\n\n")]
    c = max(elfs)
    elfs.remove(max(elfs))
    c += max(elfs)
    elfs.remove(max(elfs))
    c += max(elfs)
    print(c)

part2()
