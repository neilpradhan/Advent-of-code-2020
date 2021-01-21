def readline(line):

            a = line.rstrip().split(" ")
            first, second = map(int, a[0].split("-"))
            letter = a[1][0]
            password = a[2]
            return first,second,letter,password
            
def part1():
    filename  = "input2.txt"
    count_valid = 0
    with open(filename, "r") as f:
        valid = 0
        for line in f:
            first,second,letter,password = readline(line)
            count = 0

            for ele in password:
                if ele == letter:
                    count+=1
            if (first<=count<=second):
                valid+=1
    return valid           


def part2():
    
    filename  = "input2.txt"
    count_valid = 0
    with open(filename, "r") as f:
        valid = 0
        for line in f:
            first,second,letter,password = readline(line)
            count = 0

            if ((password[first-1]==letter) ^ (password[second-1] == letter)): 
                valid+=1    
    return valid
def main():
    print(part1())
    print(part2())
    
    return 0

    



main()            