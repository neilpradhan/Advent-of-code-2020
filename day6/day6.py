def read(input  = "input.txt"):
    with open(input, "r") as f:
        arr = f.read().split('\n\n')
        return arr


def part1(arr):
    count = 0
    for x in arr:
        count+= len(set("".join(x.split())))
    return count

def part2(arr):
    count = 0
    for x in arr:
        arr_inter= list(map(set,x.split()))
        count += len(arr_inter[0].intersection(*arr_inter[1:]))    
    return count
def main():
    arr = read()
    print(part1(arr))
    # print(arr)
    print(part2(arr))




main()