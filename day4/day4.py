
def read(input = 'input.txt'):
    with open(input,'r') as f:
        arr = f.read().split('\n\n')
        return arr

def part2(arr):
    count = 0
    for passport in arr:
                        
                    
            
        passport_dict = {key_value.split(':')[0] : key_value.split(':')[1] for key_value in passport.split()}
        if (first_verify(passport_dict)):
            if (1920 <= int(passport_dict['byr']) <= 2002) \
                and (2010 <= int(passport_dict['iyr']) <= 2020) \
                and (2020 <= int(passport_dict['eyr']) <= 2030) \
                and ((passport_dict['hgt'][-2:] == 'cm' and (150 <= int(passport_dict['hgt'][:-2]) <= 193))
                or (passport_dict['hgt'][-2:] == 'in' and (59 <= int(passport_dict['hgt'][:-2]) <= 76))) \
                and passport_dict['hcl'][0] == '#' and len(passport_dict['hcl']) == 7 and int(passport_dict['hcl'][1:], 16)+1 \
                and passport_dict['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'} \
                and (len(passport_dict['pid']) == 9 and passport_dict['pid'].isnumeric()):
                count+=1
    return count


def first_verify(passport_dict):
    w = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if set(passport_dict.keys()).issuperset(w):
        return True
    return False



def part1(arr):
    w = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    count = 0
    for passport in arr:
        a = set(map(lambda x:x.split(':')[0],passport.split()))
        # print(passport.split()) converts in to list then split it on : to and do [0 ] to get the keys and create a set
        # print(a)
        if a.issuperset(w):
            count+=1

    return count
def main():
    filename = "input.txt"
    arr = read()
    # print(part1(arr))
    print(part2(arr))


main()