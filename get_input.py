import sys
from aocd import get_data

f = open("data/day_" + sys.argv[1] + "_input.txt", "x")
f.write(get_data(day=int(sys.argv[1]), year=2022))
f.close()

print("Got data for day " + sys.argv[1] + " successfully!")

