def part1():
    inp = open("data/day_8_input.txt")
    lines = inp.readlines()
    size = len(lines[0].strip())
    grid = [ [""]* size for i in range(size)]

    i = 0
    for line in lines:
        line = line.strip()

        for j in range(len(line)):
            grid[i][j] = line[j]

        i += 1

    v_t = 0

    for r in range(size ):
        for c in range(size):
            tree = grid[r][c]

            if (all(grid[r][j] < tree for j in range(c)) or 
                all(grid[r][j] < tree for j in range(c + 1, size)) or 
                all(grid[j][c] < tree for j in range(r)) or 
                all(grid[j][c] < tree for j in range(r + 1, size))):
                v_t += 1
            
    print(v_t)


def part2():
    inp = open("data/day_8_input.txt")
    lines = inp.readlines()
    size = len(lines[0].strip())
    grid = [ [""]* size for l in range(size)]

    i = 0
    for line in lines:
        line = line.strip()
        for j in range(len(line)):
            grid[i][j] = line[j]

        i += 1

    scores = []

    for r in range(size):
        for c in range(size):
            val = grid[r][c]
            a1, b1, c1, d1 = 0, 0, 0, 0

            for j in range(c - 1, -1, -1):
                a1 += 1
                if grid[r][j] >= val:
                    break
            for j in range(c + 1, size):
                b1 += 1
                if grid[r][j] >= val:
                    break
            for j in range(r - 1, -1, -1):
                c1 += 1
                if grid[j][c] >= val:
                    break
            for j in range(r + 1, size):
                d1 += 1
                if grid[j][c] >= val:
                    break

            scores.append(a1 * b1 * c1 * d1)
    print(max(scores))

part1()
part2()
