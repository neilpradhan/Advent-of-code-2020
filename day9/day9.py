def read(input = "input.txt"):
    with open(input, "r") as f:
        return list(map(int,f.read().splitlines()))



def part1(arr):
    for i in range(25,len(arr)):
        if not num_is_valid(i,arr):
            return arr[i]
    return None


def num_is_valid(i, arr):
    
    target = arr[i]
    rest = arr[i-25:i]
    # two nos with exact half
    if rest.count(target/2) > 1:
        return True
    for i in range(len(rest)):
        if (target - rest[i]) in rest:
            return True
    return False

#better time complexity O(n)
def part2(arr):
    invalid_num = part1(arr)
    start = 0
    curr_sum = arr[0]
    
    for i in range(1,len(arr)):
        while (curr_sum > invalid_num):
            
            curr_sum = curr_sum - arr[start]
            start+=1
        
        if (curr_sum == invalid_num):
                # print(start, i)
                return max(arr[start:i]) + min(arr[start:i])
        

        curr_sum = curr_sum + arr[i]
        # print("curr_sum",curr_sum)
    # print(start)
    return 0



# def part2(arr):
#     invalid_num = part1(arr)
#     for i, num in enumerate(arr):
#         k = [num]
#         next = i+1
#         while (sum(k)<invalid_num):
#             k.append(arr[next])
#             next+=1
#         if (sum(k) == invalid_num and len(k)>2):
#             return min(k) + max(k)

def main():
    arr = read()
    # print(arr)

    # print(part1(arr))

    print(part2(arr))

    



main()