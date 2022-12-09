inp = open("data/day_9_input.txt")

def part1():
    size = 1500

    seen = [ ["."] * (size ) for i in range(size)]

    h_r = 250
    h_c = 250
    t_r = 250
    t_c = 250

    for line in inp.readlines():
        dir, mag = line.strip().split(" ")
        mag = int(mag)
        

        def touching(a, b, c, d):
            if (a == c and b == d): return True
            if (abs(a - c) == 1 and abs(b - d) == 0): return True
            if (abs(a - c) == 0 and abs(b - d) == 1): return True
            if (abs(a - c) == 1 and abs(b - d) == 1): return True
            return False

        if dir == "R":
            for i in range(mag):
                h_c += 1
                if (not touching(h_r, h_c, t_r, t_c)):
                    if (h_r - t_r == 2 and h_c == t_c):
                        t_r += 1
                    if (h_r - t_r == -2 and h_c == t_c):
                        t_r -= 1
                    if (h_c - t_c == 2 and h_r == t_r):
                        t_c += 1
                    if (h_c - t_c == -2 and h_r == t_r):
                        t_c -= 1
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
                seen[t_r][t_c] = "#"
        elif dir == "L":
            for i in range(mag):
                h_c -= 1
                if (not touching(h_r, h_c, t_r, t_c)):
                    
                    if (h_r - t_r == 2 and h_c == t_c):
                        t_r += 1
                    if (h_r - t_r == -2 and h_c == t_c):
                        t_r -= 1
                    if (h_c - t_c == 2 and h_r == t_r):
                        t_c += 1
                    if (h_c - t_c == -2 and h_r == t_r):
                        t_c -= 1
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
                seen[t_r][t_c] = "#"
        elif dir == "U":
            for i in range(mag):
                h_r -= 1
                if (not touching(h_r, h_c, t_r, t_c)):
                    
                    if (h_r - t_r == 2 and h_c == t_c):
                        t_r += 1
                    if (h_r - t_r == -2 and h_c == t_c):
                        t_r -= 1
                    if (h_c - t_c == 2 and h_r == t_r):
                        t_c += 1
                    if (h_c - t_c == -2 and h_r == t_r):
                        t_c -= 1
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
                seen[t_r][t_c] = "#"
        else:
            for i in range(mag):
                h_r += 1
                if (not touching(h_r, h_c, t_r, t_c)):
                    
                    if (h_r - t_r == 2 and h_c == t_c):
                        t_r += 1
                    if (h_r - t_r == -2 and h_c == t_c):
                        t_r -= 1
                    if (h_c - t_c == 2 and h_r == t_r):
                        t_c += 1
                    if (h_c - t_c == -2 and h_r == t_r):
                        t_c -= 1
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
                seen[t_r][t_c] = "#"
        
    c1 = 0

    for r in range(size):
        for c in range(size):
            if seen[r][c] == "#":
                c1 += 1
    print(c1)




knots = [[0, 0] for _ in range(10)]
seen = set()

seen.add((knots[-1][0], knots[-1][1]))

dirs = {
    "R": [0, 1],
    "L": [0, -1],
    "D": [1, 0],
    "U": [-1, 0],
}

h_r = h_c = t_r = t_c = 0

def touching(a, b, c, d):
    if (a == c and b == d): return True
    if (abs(a - c) == 1 and abs(b - d) == 0): return True
    if (abs(a - c) == 0 and abs(b - d) == 1): return True
    if (abs(a - c) == 1 and abs(b - d) == 1): return True
    return False

for line in inp.readlines():
    line = line.strip()
    dir, mag = line.split(" ")

    for i in range(int(mag)):
        knots[0][0] += dirs[dir][0]
        knots[0][1] += dirs[dir][1]

        for j in range(1, len(knots)):
            h_r = knots[j-1][0]
            h_c = knots[j-1][1]
            t_r = knots[j][0]
            t_c = knots[j][1]

            if (not touching(h_r, h_c, t_r, t_c)):
                if (h_r - t_r == 2 and h_c == t_c):
                    t_r += 1
                if (h_r - t_r == -2 and h_c == t_c):
                    t_r -= 1
                if (h_c - t_c == 2 and h_r == t_r):
                    t_c += 1
                if (h_c - t_c == -2 and h_r == t_r):
                    t_c -= 1
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




