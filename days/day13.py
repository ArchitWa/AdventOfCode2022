from functools import cmp_to_key

inp = open("data/day_13_input.txt")

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

def part1():
    pairs = [[eval(x) for x in pair.splitlines()] for pair in inp.read().split("\n\n")]
    s = 0
    for p_c, (left, right) in enumerate(pairs):
        if find_score(left, right) < 0:
            s += (p_c + 1)
    print(s)
    
            
#part1()

def part2():
    packets = list(map(eval, inp.read().split()))
    packets.append(eval("[[2]]"))
    packets.append(eval("[[6]]"))
    packets = sorted(packets, cmp=cmp_to_key(find_score))
    print((packets.index([[2]]) + 1)*(packets.index([[6]]) + 1))

part2()