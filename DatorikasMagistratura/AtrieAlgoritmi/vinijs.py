# Function to mark the vertex with
# different colors for different cycles
def dfs_cycle(u, p, color: list,
              par: list):
    global cyclenumber 
    # already (completely) visited vertex.
    if color[u] == 2:
        return 
    # seen vertex, but was not 
    # completely visited -> cycle detected.
    # backtrack based on parents to
    # find the complete cycle.
    if color[u] == 1:
        v = []
        cur = p
        v.append(cur) 
        # backtrack the vertex which are
        # in the current cycle thats found
        while cur != u:
            cur = par[cur]
            v.append(cur)
        cycles[cyclenumber] = v
        cyclenumber += 1 
        return 
    par[u] = p 
    # partially visited.
    color[u] = 1 
    # simple dfs on graph
    for v in graph[u]: 
        # if it has not been visited previously
        if v == par[u]:
            continue
        dfs_cycle(v, u, color, par) 
    # completely visited.
    color[u] = 2 
# add the edges to the graph
def addEdge(u, v, w): 
    graph[u].append(v)
    graph[v].append(u)
    weights[u].append([v,w])
    weights[v].append([u,w])
# Function to print the cycles
def printCycles(): 
    # print all the vertex with same cycle
    for i in range(0, cyclenumber): 
        # Print the i-th cycle
        print("Cycle Number %d:" % (i+1), end = " ")
        for x in cycles[i]:
            print(x, end = " ")
        print()
def printCycles2():
    global k
    k=0
    global W
    W=0 
    for i in range(0, cyclenumber):
        m=101
        a=0
        b=0
        for x in range(len(cycles[i])-1):
            num1=cycles[i][x]
            num2=cycles[i][x+1]
            for j in weights[num1]:
                if(j[0]==num2):
                    if(j[1]<m):
                        m=j[1]
                        a=num1
                        b=num2
                    break
        result.append(a)
        result.append(b)
        k=k+1
        W=W+m
# Python3 program to print all the cycles
# in an undirected graph
N = 500
result=[]
result.append(0) 
result.append(0) 
# variables to be used
# in both functions
graph = [[] for i in range(N)]
cycles = [[] for i in range(N)]
weights = [[] for i in range(N)]
f = open("input2.txt", "r")
inputdata=(f.read()) 
f.close()
myList = inputdata.split()
myList.pop(0)#Dont care about n
print((len(myList))/3)
print("myList:",myList)
"""
addEdge(1, 2,-1)
addEdge(2, 3,2)
addEdge(3, 4,2)
addEdge(4, 6,3)
addEdge(4, 7,4)
addEdge(5, 6,-5)
addEdge(3, 5,6)
addEdge(7, 8,7)
addEdge(6, 10,1)
addEdge(5, 9,2)
addEdge(10, 9,3)
addEdge(10, 11,7)
addEdge(11, 12,8)
addEdge(11, 13,9)
addEdge(12, 13,10)
addEdge(12, 1,14)
"""
    # arrays required to color the
    # graph, store the parent of node
color = [0] * N
par = [0] * N 
    # store the numbers of cycle
cyclenumber = 0 
    # call DFS to mark the cycles
dfs_cycle(1, 0, color, par) 
    # function to print the cycles
printCycles2()
#print("k=",k)
#print("W=",W)
result[0]=k
result[1]=W
print(result)
#print(cycles)
