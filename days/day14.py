inp = open("data/day_14_input.txt")

cave = [["."] * 1000 for _ in range(1000)]
idx = 0

for line in inp.readlines():
    line = line.strip()
    points = line.split(" -> ")
    for i in range(1, len(points)):
        x1, y1 = map(int, points[i-1].split(","))
        x2, y2 = map(int, points[i].split(","))
        
        if x1 == x2:
            for row in range(min(y1, y2), max(y1, y2)+1):
                cave[row][x1-idx] = "#"
        if y1 == y2:
            for col in range(min(x1, x2), max(x1, x2)+1):
                cave[y1][col-idx] = "#"

cave[0][500-idx] = '+'

lowest_rock = 0

def print_cave():
    for i in range(len(cave)):
        print(''.join(map(str, cave[i])))

for i in range(len(cave)):
    if "#" in cave[i]:
        lowest_rock = i

for i in range(len(cave[0])):
    cave[lowest_rock+2][i] = "#"

def sim_sand():
    sand_dropped = 0
    sand_r = 0
    sand_c = 500 - idx

    def move_sand_1(): # part 1
        nonlocal sand_r
        nonlocal sand_c
        if sand_r  >= len(cave):
            return False
        
        while (cave[sand_r + 1][sand_c] == "."):
            sand_r += 1
            if sand_r + 1 >= len(cave):
                return False
        if cave[sand_r + 1][sand_c - 1] == ".":
            sand_r += 1
            sand_c -= 1
            move_sand_1()

        if sand_r + 1 >= len(cave):
            return False
            
        if cave[sand_r + 1][sand_c + 1] == ".":
            sand_r += 1
            sand_c += 1
            move_sand_1()

        if sand_r + 1 >= len(cave):
            return False

        if cave[sand_r+1][sand_c] != "." and cave[sand_r+1][sand_c-1] != "." and cave[sand_r+1][sand_c+1] != ".":
            cave[sand_r][sand_c] = "o"
            return True

    def move_sand_2(): # part 2
        nonlocal sand_r
        nonlocal sand_c
        
        while (cave[sand_r + 1][sand_c] == "."):
            sand_r += 1
        if cave[sand_r + 1][sand_c - 1] == ".":
            sand_r += 1
            sand_c -= 1
            move_sand_2()
        if cave[sand_r + 1][sand_c + 1] == ".":
            sand_r += 1
            sand_c += 1
            move_sand_2()

        if sand_r == 0 and sand_c == 500 - idx:
                return False

        if cave[sand_r+1][sand_c] != "." and cave[sand_r+1][sand_c-1] != "." and cave[sand_r+1][sand_c+1] != ".":
            cave[sand_r][sand_c] = "o"
            return True

    while move_sand_2(): # change to move_sand_1 for part 1
        sand_dropped += 1
        sand_r = 0
        sand_c = 500 - idx
        
    print(sand_dropped + 1)

sim_sand()
