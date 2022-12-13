# aocd > data/day_13_input.txt
# python submit.py 13 a _
# python submit.py 13 b _ 

inp = open("data/day_13_input.txt")

#pairs = [[eval(x) for x in pair.splitlines()] for pair in inp.read().split("\n\n")]

def find_score(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return l - r
    if isinstance(l, list) and isinstance(r, list):
        comb = zip(l, r)
        for l_n, r_n in comb:
            score = find_score(l_n, r_n)
            if score != 0:
                return score
            
        return len(l) - len(r)
    if isinstance(l, list):
        return find_score(l, [r])
    if isinstance(r, list):
        return find_score([l], r)

pairs = list(map(eval, inp.read().split()))

def part1():
    s = 0
    for p_c, (left, right) in enumerate(pairs):
        if find_score(left, right) < 0:
            s += (p_c + 1)
    print(s)
    
            
# part1()

def part2():
    two = 1
    six = 2
    for val in pairs:
        s_l_2 = find_score(val, [[2]])
        s_l_6 = find_score(val, [[6]])
        if s_l_2 < 0:
            two += 1
            six += 1
        if s_l_6 < 0 and s_l_2 > 0:
            six += 1
    print((two * six))

part2()