

def read(input = "input.txt"):
    with open(input, "r") as f:
        return [0] + list(map(int,f.read().splitlines()))





def part1(arr):
    arr.sort()
    # print(arr)
    diff = {}
    diff[0] = 0
    diff[1] = 0
    diff[2] = 0
    diff[3] = 1
    for i in range(0,len(arr)-1):
        diff[arr[i+1] - arr[i]] += 1
    print(diff[1])
    print(diff[3])
    return diff[1] * diff[3]



def num_of_ways(arr,i, memo = {}):
    print("hello")
    if i in memo:
        return memo[i]
    if (i == len(arr)-1):
        return 1
    total = 0
    if (i+1 <= len(arr)-1 and (arr[i+1] - arr[i] <= 3)):        
        total+= num_of_ways(arr,i+1)
    if (i+2 <= len(arr)-1 and (arr[i+2] - arr[i] <= 3)):        
        total+=num_of_ways(arr,i+2)
    if (i+3 <= len(arr)-1 and (arr[i+3] - arr[i] <= 3)):        
        total+= num_of_ways(arr,i+3)
    memo[i] = total
    return total

def part2(arr):
    return num_of_ways(arr,0,{})



def main():
    arr = read()

    arr.sort()
    
    print(part2(arr))


main()