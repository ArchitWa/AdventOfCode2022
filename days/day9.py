dirs = {
    "R": [0, 1],
    "L": [0, -1],
    "D": [1, 0],
    "U": [-1, 0],
}

def touching(a, b, c, d):
    if (a == c and b == d): return True
    if (abs(a - c) == 1 and abs(b - d) == 0): return True
    if (abs(a - c) == 0 and abs(b - d) == 1): return True
    if (abs(a - c) == 1 and abs(b - d) == 1): return True
    return False

def part1():
    inp = open("data/day_9_input.txt")
    seen = set()

    h_r = h_c = t_r = t_c = 250

    for line in inp.readlines():
        dir, mag = line.strip().split(" ")
        mag = int(mag)

        for _ in range(mag):
            h_r += dirs[dir][0]
            h_c += dirs[dir][1]

            if (not touching(h_r, h_c, t_r, t_c)):
                if ((h_c == t_c) and abs(h_r - t_r) == 2):
                    t_r += 1 if h_r - t_r == 2 else -1
                if ((h_r == t_r) and abs(h_c - t_c) == 2):
                    t_c += 1 if h_c - t_c == 2 else -1
                if (h_r != t_r and h_c != t_c):
                    if (h_c > t_c):
                        if (h_r < t_r):
                            t_r -= 1
                            t_c += 1
                        else:
                            t_r += 1
                            t_c += 1
                    else:
                        if (h_r < t_r):
                            t_r -= 1
                            t_c -= 1
                        else:
                            t_r += 1
                            t_c -= 1
            seen.add((t_r, t_c))
    print(len(seen))


def part2():
    inp = open("data/day_9_input.txt")
    knots = [[0, 0] for _ in range(10)]
    seen = set()

    seen.add((knots[-1][0], knots[-1][1]))
    h_r = h_c = t_r = t_c = 0

    for line in inp.readlines():
        line = line.strip()
        dir, mag = line.split(" ")

        for _ in range(int(mag)):
            knots[0][0] += dirs[dir][0]
            knots[0][1] += dirs[dir][1]

            for j in range(1, len(knots)):
                h_r = knots[j-1][0]
                h_c = knots[j-1][1]
                t_r = knots[j][0]
                t_c = knots[j][1]

                if (not touching(h_r, h_c, t_r, t_c)):
                    if ((h_c == t_c) and abs(h_r - t_r) == 2):
                        t_r += 1 if h_r - t_r == 2 else -1
                    if ((h_r == t_r) and abs(h_c - t_c) == 2):
                        t_c += 1 if h_c - t_c == 2 else -1

                    if (h_r != t_r and h_c != t_c):
                        if (h_c > t_c):
                            if (h_r < t_r):
                                t_r -= 1
                                t_c += 1
                            else:
                                t_r += 1
                                t_c += 1
                        else:
                            if (h_r < t_r):
                                t_r -= 1
                                t_c -= 1
                            else:
                                t_r += 1
                                t_c -= 1
                knots[j][0] = t_r
                knots[j][1] = t_c

            seen.add((knots[-1][0], knots[-1][1]))

    print(len(seen))
part1()
part2()



