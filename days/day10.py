f = open("data/day_10_input.txt")

def part1(f):
    cycle_c = s_s = 0
    x = 1

    def tick():
        nonlocal cycle_c, s_s, x
        cycle_c += 1
        if cycle_c in [20, 60, 100, 140, 180, 220]:
            s_s += cycle_c * x

    for line in f.readlines():
        if line.startswith('noop'):
            tick()
        if line.startswith('addx'):
            for _ in range(2):
                tick()
            x += int(line.split(" ")[1])

    print(s_s)

def part2(f):
    screen = [[""] * 40 for _ in range(6)]
    x = 1
    cycle_c = 0

    for line in f.readlines():
        def tick():
            nonlocal cycle_c
            screen[cycle_c // 40][cycle_c % 40] = "##" if abs(cycle_c%40 - x) <= 1 else "  "
            cycle_c += 1

        if  'noop' in line:
            tick()
        else:  
            for _ in range(2):
                tick()
            x += int(line.split(" ")[1])

    for i in screen:
        print(''.join(map(str, i)))

part2(f)