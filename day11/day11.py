def read(input = "input.txt"):
    arr = []
    with open(input,"r") as f:
        return list(map(list, f.read().splitlines()))



def get_count(arr,i,j):
    count = 0
    for x in range(max(0,i-1),min(i+2,len(arr))):
        for y in range(max(0,j-1), min(j+2,len(arr[1]))):
            if not (x==i and y==j) and arr[x][y] == "#":
                count += 1
    return count

def iteration(arr, get_count):
    while True:
        change_to_fill = [] # list of tuples
        change_to_empty = []
        # print(len(arr))
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                count = get_count(arr,i,j)
                if arr[i][j] == ".":
                    continue
                if (count == 0  and arr[i][j] == "L"):
                    change_to_fill.append((i,j))
                if (count >= 4 and arr[i][j] == "#"):
                    change_to_empty.append((i,j))
        for s in change_to_fill:
            arr[s[0]][s[1]] = "#"
        for s in change_to_empty:
            arr[s[0]][s[1]] = "L"
        print("empty",len(change_to_empty))
        print("full",len(change_to_fill))
        if len(change_to_empty) + len(change_to_fill) == 0:
            return sum(map(lambda x: x.count("#"),arr))




def visibly_occupied(arr,i,j):
    count  = 0
    ## find visible by slopes
    directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    # see in all 8 directions
    count = 0
    for d in directions:
        flag = False
        curr_ele = [i+d[0],j+d[1]] 
        while(not flag and (0<= curr_ele[0] <len(arr)) and (0<= curr_ele[1] <len(arr[0]))  ):
            curr_val = arr[curr_ele[0]][curr_ele[1]]            
            
            if curr_val == "#":
                flag = True
                count+=1
            elif curr_val == "L":
                flag = True
            else:
                curr_ele[0] += d[0]
                curr_ele[1] += d[1]
    return count
        
def iteration_part2(arr, visibly_occupied):
    while True:
        change_to_fill = [] # list of tuples
        change_to_empty = []
        # print(len(arr))
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                count = visibly_occupied(arr,i,j)
                if arr[i][j] == ".":
                    continue
                if (count == 0  and arr[i][j] == "L"):
                    change_to_fill.append((i,j))
                if (count >= 5 and arr[i][j] == "#"):
                    change_to_empty.append((i,j))
        for s in change_to_fill:
            arr[s[0]][s[1]] = "#"
        for s in change_to_empty:
            arr[s[0]][s[1]] = "L"
        print("empty",len(change_to_empty))
        print("full",len(change_to_fill))
        if len(change_to_empty) + len(change_to_fill) == 0:
            return sum(map(lambda x: x.count("#"),arr))



def part1(arr):
    
    return iteration(arr, get_count)


def part2(arr):
    return iteration_part2(arr,visibly_occupied)

def main():
    arr = read()

    # print(part1(arr))
    print(part2(arr))
    # print(len(arr))
    
        
    
main()