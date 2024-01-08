# Function to mark the vertex with
# different colors for different cycles
#Time Complexity: O(N + M), where N is 
#the number of vertexes and M is the number of edges. 
#Space: O(N + M)
def dfs_cycle(u, p, color, par):
    global cyclenumber 
    #print("u,p",u,p)
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
        # backtrack the vertex which are in the current cycle thats found
        while cur != u:
            cur = par[cur]
            v.append(cur)
        cycles[cyclenumber] = v
        cyclenumber += 1 
        return 
    par[u] = p     # partially visited.
    color[u] = 1     # simple dfs on graph
    for v in graph[u]:         
        if v == par[u]:# if it has not been visited previously
            continue
        dfs_cycle(v, u, color, par)     
    color[u] = 2 # completely visited.
#Add the edges to the graph
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
# Function to find weights in cycles      
def printCycles2():
    global k
    k=0
    global W
    W=0 
    for i in range(0, cyclenumber):
        m=101# range(-100, +100), find min weight in each cycle
        a=0 #vertice a for results
        b=0 #vertice b for rersults
        for x in range(len(cycles[i])):
            num1=cycles[i][x]
            if (x<(len(cycles[i]))-1):#if a is not last node
                num2=cycles[i][x+1]
            else:#a is last node, check with first node
                num2=cycles[i][0]
            for j in weights[num1]:#weight on edge a - b
                if(j[0]==num2):#found b vertice
                    if(j[1]<m):#check weight
                        m=j[1]#Store min, a, b
                        a=num1
                        b=num2
                        #print("m,a,b:",m,a,b,j[1])
                    break
        result.append(a)#Write a, b
        result.append(b)
        k=k+1 #store k for results array
        W=W+m #store total weight for results array
N = 500 #Max number of vertices
result=[]
result.append(0)# k value
result.append(0)# W value
graph = [[] for i in range(N)] # Adjacency list - stores connected vertices
cycles = [[] for i in range(N)] #Found cycles
weights = [[] for i in range(N)]#[[0]-connected vertice [1]-weight],...
f = open("input.txt", "r")
inputdata=(f.read()) 
f.close()
myList = inputdata.split()
myList.pop(0)#Dont care about n value
for i in range(0,len(myList),3):
    addEdge(int(myList[i]),int(myList[i+1]),int(myList[i+2])) 
color = [0] * N #array to color the graph 
par = [0] * N #store the parent of node
cyclenumber = 0 # store the numbers of cycle
dfs_cycle(int(myList[0]),0, color, par) #finds all cycles 
printCycles2()# fills result array
result[0]=k
result[1]=W
print(result)
f = open("output.txt", "w")
for i in result:
    f.write(str(i))
    f.write(" ")
f.close()

