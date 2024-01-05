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
        m=101# range(-100, +100) meklē min vertibu
        a=0
        b=0
        for x in range(len(cycles[i])-1):
            num1=cycles[i][x]
            num2=cycles[i][x+1]
            for j in weights[num1]:#meklē svarus starp virsotnēm
                if(j[0]==num2):#atrada otro virsotni 
                    if(j[1]<m):#pārbauda edge svarus
                        m=j[1]#Saglaba min vertibas info
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
f = open("input4.txt", "r")
inputdata=(f.read()) 
f.close()
myList = inputdata.split()
myList.pop(0)#Dont care about n
for i in range(0,len(myList),3):
    addEdge(int(myList[i]),int(myList[i+1]),int(myList[i+2]))
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
result[0]=k
result[1]=W
print(result)
f = open("output.txt", "w")
for i in result:
    f.write(str(i))
    f.write(" ")
f.close()

