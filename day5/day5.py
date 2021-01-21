def read(input = 'input.txt'):
    with open(input,'r') as f:
        arr = f.read().splitlines()
        return arr
    

def get_row(passport):
    lower = 0
    upper = 127
    for i in range(6):
        mid = (lower + upper)//2
        if passport[i] == "F":
            upper = mid
        elif passport[i] == "B":
            lower = mid +1
    if passport[6] == "F":
        return lower
    else:
        return upper
    
    
def get_col(passport):
    lower = 0
    upper = 7
    for i in range(7,9):
        mid = (lower + upper)//2
        if passport[i] == "L":
            upper = mid
        elif passport[i] == "R":
            lower = mid +1
    if passport[9] == "R":
        return upper
    else:
        return lower

def seat_ID(passport):
    col = get_col(passport)
    row = get_row(passport)
    seat_ID = 8* row  + col
    return seat_ID

def part1(arr):
    max_seat = 0
    for passport in arr:
        col = get_col(passport)
        row = get_row(passport)
        seat_ID = 8* row  + col
        max_seat = max(seat_ID,max_seat)
    return max_seat


def part1_test(passport = "BFFFBBFRRR"):
    max_seat = 0
    col = get_col(passport)
    row = get_row(passport)
    seat_ID = 8* row  + col
    return seat_ID


def part2(arr):
    a  = set()
    for passport in arr:
        col = get_col(passport)
        row = get_row(passport)
        seat_ID = 8* row  + col
        a.add(seat_ID)
    for ele in a:
        if ele+2 in a:
            return ele + 1
        
def part2_unseen(arr):
    total_list = list(range(part1(arr)+1))
    for passport in arr:
        total_list.remove(seat_ID(passport))
    return total_list[-1] 
def main():
    arr = read()
    # print(part1_test())
    print(part1(arr))
    # print(arr[0])
    # print(part2(arr))
    print(part2_unseen(arr))
    
    
    
main()