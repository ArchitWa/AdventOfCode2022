import re
inp = open("data/day_15_input.txt")

lines = inp.readlines()

sensors = [] 
beacons = [] 
distances = []

find_dist = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

for i in range(len(lines)):
    nums = list(map(int, re.findall(r'-?\d+', lines[i].strip())))

    sensors.append((nums[0], nums[1]))
    beacons.append((nums[2], nums[3]))
    distances.append(find_dist(sensors[i], beacons[i]))

def part1():
    s = 0
    max_x = max([sensor[0] for sensor in sensors] + [beacon[0] for beacon in beacons])

    for i in range(0 - (max_x * 2), max_x * 2):
        if i % 1_000_000 == 0: print(i)
        for j in range(len(sensors)):
            loc = (i, 2_000_000)
            if loc == beacons[j]: break
            if find_dist(sensors[j], loc) <= distances[j]:
                    s += 1
                    break
    print(f"Ans: {s}") # 5809294


def part2():
    for i in range(len(sensors)):
        s_x, s_y = sensors[i]
        for j in range(distances[i] + 2):
            for ang_x, ang_y in [(1,1),(-1,1),(-1,-1),(1,-1)]:
                x_test = (s_x + j) * ang_x
                y_test = (s_y + distances[i] + 1 - j) * ang_y
                if not 0<=x_test<=4_000_000 or not 0<=y_test<=4_000_000:
                    continue
                c = 0
                for l in range(len(sensors)):
                    if find_dist(sensors[l], (x_test, y_test)) <= distances[l]:
                        
                        break
                    c += 1
                if c == len(sensors): print(f"Ans: {x_test * 4_000_000 + y_test}") # 10693731308112
                    
            
part1()
#part2()