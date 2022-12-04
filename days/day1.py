
inp = open('data/day_1_input.txt', "r")

lines = inp.readlines()

c = 0
elf_cal = []
for line in lines:
    if line.strip():
        c += int(line)
    else:
        elf_cal.append(c)
        c = 0


c = max(elf_cal)
elf_cal.remove(max(elf_cal))
c += max(elf_cal)
elf_cal.remove(max(elf_cal))
c += max(elf_cal)


print(c)
