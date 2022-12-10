#      --------Part 1---------   --------Part 2---------
# Day       Time    Rank  Score       Time    Rank  Score
#  10   00:13:26    1972      0   00:47:32    4828      0

f = open("data/day_10_input.txt")

def part1(f):
    cycle_c = s_s = 0
    x = 1
    cycles = [20, 60, 100, 140, 180, 220]

    def update_s_s(s_s, x):
        if cycle_c in cycles:
            s_s += cycle_c * x
            cycles.remove(cycle_c)
        return s_s


    for line in f.readlines():
        line = line.strip()
        s_s = update_s_s(s_s, x)

        if line == 'noop':
            cycle_c += 1
            s_s = update_s_s(s_s, x)
        if line.startswith('addx'):
            for _ in range(2):
                cycle_c += 1
                s_s = update_s_s(s_s, x)
            x += int(line.split(" ")[1])

    print(s_s)

def part2(f):
    screen = [[""] * 40 for _ in range(6)]
    x = 1
    cycle_c = r = c = 0

    for line in f.readlines():
        line = line.strip()
        if (r == 5 and c == 39): break

        def update_screen():
            if x - 1 <= cycle_c % 40 and cycle_c % 40 <= x + 1:
                screen[r][c] = "#"
            else:
                screen[r][c] = '.'
        def update_cycle(cycle_c, r, c):
            cycle_c += 1
            if c < 39:
                c += 1
            else:
                c = 0
                r += 1
            return cycle_c, r, c

        update_screen()

        if line == 'noop':
            cycle_c, r, c = update_cycle(cycle_c, r, c)
            update_screen()
        else:  
            for _ in range(2):
                cycle_c, r, c = update_cycle(cycle_c, r, c)
                update_screen()
            x += int(line.split(" ")[1])

    for i in screen:
        print(''.join(map(str, i)))
