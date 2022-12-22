inp = open("data/day_7_input.txt")

class File:
    def __init__(self, name, size, parent_dir):
        self.name = name
        self.size = size
        self.parent_dir = parent_dir

class Directory:
    def __init__(self, name, parent_dir, child_dirs):
        self.name = name
        self.parent_dir = parent_dir
        self.child_dirs = child_dirs

def create_dir():
    main_dir = Directory("/", None, {})
    curr_dir = main_dir
    listing = False

    for line in inp.readlines():
        line = line.strip()
        if line.startswith("$"):
            listing = False
            cmd = line.split(" ")
            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    curr_dir = curr_dir.parent_dir
                elif cmd[2] == "/":
                    curr_dir = main_dir
                else:
                    curr_dir = curr_dir.child_dirs.get(cmd[2])
            else:
                listing = True
                continue

        if listing == True:
            f = line.split(" ")
           
            if f[0] == "dir":
                curr_dir.child_dirs[f[1]] = Directory(f[1], curr_dir, {})
            else:
                curr_dir.child_dirs[f[1]] = File(f[1], int(f[0]), curr_dir)
               
    return main_dir

main_dir = create_dir()
sizes = []

def calc_sizes(dir):
    if type(dir) == File:
        return dir.size
    size = 0
    for child in dir.child_dirs.values():
        s = calc_sizes(child)
        size += s
    sizes.append(size)

    return size
calc_sizes(main_dir)

def part1():
    print(sum(size for size in sizes if size <= 100000))

def part2():
    n_s = max(sizes) - 40_000_000
    print(min(size for size in sizes if size > n_s))

part1()
part2()

