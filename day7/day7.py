class Node:
    def __init__(self,id):
        self.id = id
        # self.outgoing = {}
        # self.incoming = {}
        self.neighbours = {}
    def __str__(self):
        return f"{self.id}:{self.neighbours}"
        
    # add another node as adjacent with id and weight
    def add_neighbours(self,other,weight):
        self.neighbours[other] = weight
    
    
    # these functions wont work because dictionary cannot have different keys
    # def fill_incoming(self):      
    #     for key in self.neighbours.keys():
    #         if self.neighbours[key]<0:
    #            self.incoming[key] = self.neighbours[key]   
    # def fill_outgoing(self):
    #     for key in self.neighbours.keys():
    #         if self.neighbours[key]>0:
    #            self.outgoing[key] = self.neighbours[key]   
    def getEdge(self, other):
        return self.neighbours[other]
    
    def getParents(self):
        parents = {}
        for i in self.neighbours.keys():
            if self.neighbours[i] < 0:
                parents[i] = self.neighbours[i]
        return parents

    def getChildren(self):
        children = {}
        for i in self.neighbours.keys():
            if self.neighbours[i] > 0:
                children[i] = self.neighbours[i]
        return children    
    

    
    
    
    
class Graph:
    def __init__(self):
        self.nodes = {}
        
    
    def add_nodes(self,id):
        if id not in self.nodes.keys():
            self.nodes[id] = Node(id)
            
    def getNode(self,id):
        return self.nodes[id] if id in self.nodes.keys() else None
    
    def addEdge(self, src, dest, weight):
        weight = abs(weight)
        if src not in self.nodes.keys():
            self.add_nodes(src)
        if dest not in self.nodes.keys():
            self.add_nodes(dest)
        self.nodes[src].add_neighbours(dest,weight)
        self.nodes[dest].add_neighbours(src,0-weight)
        
        # self.nodes[src].fill_incoming()
        # self.nodes[src].fill_outgoing()
        # self.nodes[dest].fill_incoming()
        # self.nodes[dest].fill_outgoing()

def read(input = "input.txt"):
    g = Graph()
    with open (input, "r") as f:
        for line in f.read().splitlines():
            key, values  = line.split("bags contain ")
            # print("key",key)
            g.add_nodes(key.strip())
            if ("no other" in line):
                continue
            value_list = values.split(",")
            for value in value_list:
                word_list= value.split()
                # print(key)
                # print("".join(word_list[1:-1]).strip())
                g.addEdge(key.strip()," ".join(word_list[1:-1]).strip(), int(word_list[0]))
                

    return g

def part1(g):
    unique = set()
    start = g.getNode("shiny gold")
    # print(start)
    toProcess = set(start.getParents().keys())
    # print("to process",[x for x in toProcess])
    while len(toProcess) != 0:
        curr = toProcess.pop()
        toProcess.update(g.getNode(curr).getParents().keys())
        unique.add(curr)
    print(unique)
    return len(unique)


def func(g,id):

    if len(g.nodes[id].getChildren())==0:
        return 1 
    else:
        # print(g.nodes[id].getChildren().keys())
        return 1  + sum([g.nodes[id].getChildren()[key]* func(g,key) for key in  g.nodes[id].getChildren().keys()])
        

def part2(g, id):
    return func(g,id) -1


def main():
    g = Graph
    g = read()
    # print(part1(g))
    print(part2(g,"shiny gold"))

main()    
        