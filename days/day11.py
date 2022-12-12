import re

class Monkey:
    def __init__(self, inspections, items, op, test, true_throw, false_throw) -> None:
        self.inspections = inspections
        self.items = items
        self.op = op
        self.test = test
        self.t_t = true_throw
        self.f_t = false_throw

inp = open("data/day_11_input.txt")
msg = ""
for line in inp.readlines():
    msg += line

monkeys = []

for monkey_txt in msg.split("\n\n"):
    m_l = monkey_txt.split("\n")
    items = list(map(int, re.findall(r'\d+', m_l[1])))
    op = m_l[2].split(":")[1].strip()[6:].replace("old", "item")
    test = int(re.findall(r'\d+', m_l[3])[0])
    true_throw = int(re.findall(r'\d+', m_l[4])[0])
    false_throw = int(re.findall(r'\d+', m_l[5])[0])
    
    monkeys.append(Monkey(0, items, op, test, true_throw, false_throw))

def part1():
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspections += len(monkey.items)
            for item in monkey.items:
                w_l = eval(monkey.op) // 3

                if w_l % monkey.test == 0:
                    monkeys[monkey.t_t].items.append(w_l)
                else:
                    monkeys[monkey.f_t].items.append(w_l)
            monkey.items = []
                
    insp = []
    for monkey in monkeys:
        insp.append(monkey.inspections)
    
    insp = sorted(insp)
    print(insp[-1] * insp[-2])

def part2():
    total_n = 1
    for monkey in monkeys:
        total_n *= monkey.test

    insp = [0] * len(monkeys)
    for _ in range(10000):
        i = 0
        for monkey in monkeys:
            insp[i] += len(monkey.items)
            for item in monkey.items:
                w_l = eval(monkey.op) % total_n

                if w_l % monkey.test == 0:
                    monkeys[monkey.t_t].items.append(w_l)
                else:
                    monkeys[monkey.f_t].items.append(w_l)
            monkey.items = []
            i += 1
    insp.sort()
    print(insp[-1] * insp[-2])

part2()

