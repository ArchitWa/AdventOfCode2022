inp = open("data/day_8_input.txt")
size = 99
def part1():
    grid = [ [""]* size for i in range(size)]

    i = 0
    for line in inp.readlines():
        line = line.strip()

        for j in range(len(line)):
            grid[i][j] = line[j]
    
        i += 1
    
    v_t = 0

    for r in range(size ):
        for c in range(size):
            tree = grid[r][c]

            t1, t2, t3, t4 = 0,0,0,0
            for j in range(c):
                if grid[r][j] < tree:
                    t1 += 1
            for j in range(c + 1, size):
                if grid[r][j] < tree:
                    t2 += 1
            for j in range(r):
                if grid[j][c] < tree:
                    t3 += 1
            for j in range(r + 1, size):
                if grid[j][c] < tree:
                    t4 += 1
            if (t1 == c or t2 == size - c - 1 or t3 == r or t4 == size - r - 1):
                v_t += 1
        

    print(v_t)


def part2():
    grid = [ [""]* size for l in range(size)]

    i = 0
    for line in inp.readlines():
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
    
part2()
