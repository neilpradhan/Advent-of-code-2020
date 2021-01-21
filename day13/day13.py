from math import prod


def read(input = "input.txt"):
    with open(input,"r") as f:
        lines = f.read().splitlines()
        return int(lines[0]),lines[1].split(",")


def calcDist(earliest, id):
    if earliest % id == 0:
        return 0
    return id * (earliest // id + 1) - earliest


def part1(earliest, ids):
    idlist = list(map(int, filter(lambda x: x != "x", ids)))
    print(idlist)
    closest = [ids[0], calcDist(earliest, idlist[0])]
    for id in idlist[1:]:
        currDist = calcDist(earliest, id)
        if currDist < closest[1]:
            closest = [id, currDist]
    return closest[0] * closest[1]


def part2()


def main():
    time_stamp, ids = read()
    print(part1(time_stamp, ids))
    
    
main()