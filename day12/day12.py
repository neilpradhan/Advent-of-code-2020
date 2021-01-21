
import math
def read(input = "input.txt"):
    with open(input,"r") as f:
        return f.read().splitlines()
        
        
        
dirs  = {"N" :(0,1) ,"S" : (0,-1),"E" : (1,0),"W" : (-1,0)}

degrees  = {0 : (1,0), 90 : (0,1) , 180 : (-1,0), 270 : (0,-1)}

DIRS = {"N": (1, 0), "E": (0, 1), "S": (-1, 0), "W": (0, -1)}
ROTS = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}

def part1(arr):
    x = 0
    y = 0
    face = 0
    for inst in arr:
        direction = inst[:1]
        value = int(inst[1:])
        
        if direction == "F":
            f = degrees[face]
            x += value * f[0]
            y += value * f[1]
        elif direction == "L":
            face = (face+value) % 360
        elif direction == "R":
            face = (face-value)% 360
            
        else:
            x += dirs[direction][0] * value
            y += dirs[direction][1] * value
    return abs(x) + abs(y)




def rotate_way(pt, val):
    
    if val == 90:
        temp = pt[0]
        pt[0] = pt[1]
        pt[1] = 0-temp
    elif val == 180:
        pt[0] = 0 - pt[0]
        pt[1] = 0 - pt[1]
    elif val == 270:
        temp  = pt[0]
        pt[0] = 0-pt[1]
        pt[1] = temp
         


        
def part2(arr):
    ship = [0,0]
    waypoint = [10,1]
    for inst in arr:
        direction = inst[:1]
        value = int(inst[1:])
        
        if direction == "F":
            ship[0] += value * waypoint[0]
            ship[1] += value * waypoint[1]
        elif direction == "L":
            rotate_way(waypoint,(0-value)% 360)
        elif direction == "R":
            rotate_way(waypoint,value % 360)
            
        else:
            waypoint[0] += dirs[direction][0] * value
            waypoint[1] += dirs[direction][1] * value
        print("way",waypoint[0],waypoint[1])
        print("ship",ship[0],ship[1])
    return abs(ship[0]) + abs(ship[1])    
     

def main():
    arr = read()

    # print(part1(arr))
    print(part2(arr))
    

main()
        
        
        
        