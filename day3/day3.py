
def part1(arr,del_y,del_x):
    y = 0
    x = 0
    count = 0
    while(y<len(arr)):
        if arr[y][(x % len(arr[0]))] == "#":
           count+=1
        y+=del_y 
        x+=del_x
    return count 

def part2(arr):
    a = part1(arr,1,1) * part1(arr,1,3) * part1(arr,1,5) * part1(arr,1,7)*part1(arr,2,1)
    return a
def main():
    filename  = "input.txt"
    with open(filename,'r') as f:
        arr = list(map(lambda x:x.rstrip(),f.readlines()))
        print(part1(arr,1,3))
        print(part2(arr))



main()