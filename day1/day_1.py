def readEntries(filename="input.txt"):
    with open(filename, "r") as f:
        return [int(line.rstrip()) for line in f]
    
    


def part1(entries):
    entriesset = set(entries)
    if 1010 in entriesset:
        if entries.count(1010) > 1:
            return f"1010 * 1010 = {1010 ** 2}"
        else:
            entriesset.remove(1010)
    for i in entriesset:
        if (2020 - i) in entriesset:
            return f"{i} * {2020 - i} = {i * (2020  - i)}"


def part2(entries, sum):
    entries.sort()
    for i in range(0,len(entries)-2):
        l=i+1
        r=len(entries)-1
        while(l<r):
            if (sum == entries[l]+entries[i]+entries[r]):
                print("be")
                return  entries[l]* entries[i]*entries[r]         
            elif (sum <entries[l]+entries[i]+entries[r]):
                r-=1
            else:
                l+=1

def main():
    entries = readEntries()
    # print(part1(entries))
    print(part2(entries,2020))


main()