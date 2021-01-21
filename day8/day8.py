def read(input = "input.txt"):
    arr = []
    with open(input, "r") as f:
        # for line in f:
        #     instruction, number = line.split()
        #     arr.append([instruction,number])
        #     arr.append(line)
        # return arr
        return f.read().splitlines()
        

# def part1(arr,acc, i, vis):
#     if (i in vis):
#         return False,acc
    
#     if arr[i][0] == 'nop':
#         vis.append(i)
#         return part1(arr,acc,i+1,vis)
#     if arr[i][0] == 'acc':
#         vis.append(i)
#         acc = acc + int(arr[i][1])
#         return part1(arr,acc,i+1,vis)
#     if arr[i][0] == 'jmp':
#         vis.append(i)
#         return part1(arr,acc,i + int(arr[i][1]),vis)

def terminate(instruction):
    vis = set()
    index = 0
    acc = 0
    while (index < len(instruction)):
        if index in vis:
            return False, acc
        print(instruction[index])
        curr, val  = instruction[index].split()
        # print("curr","val",curr,val)
        if curr == "jmp":
            index += int(val)
        else:
            if curr == "acc":
                acc += int(val)
            index +=1
    return True, acc
        
# def part2()

def part1(instruction):
    return terminate(instruction)[1]



def part2(instruction):
    for i, line in enumerate(instruction):
        temp = line.split()
        change = []
        if temp[0] == "nop":
            change = instruction[:i] + ["jmp" + " "+ temp[1]] + instruction[i+1:]
        elif temp[0] == "jmp":
            change = instruction[:i] + ["nop" +" "+ temp[1]] + instruction[i+1:]
        
        x = terminate(change)
        if (x[0] ==True):
            return x[1]

def main():
    instruction = read()
    # print(arr)
    # print(instruction)
    # vis = []
    # print(part1(arr,0,0,vis))
    # print(instruction[0])
    print(part2(instruction))
    
main()