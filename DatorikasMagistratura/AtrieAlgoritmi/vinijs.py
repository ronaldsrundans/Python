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
    #print(u,v)
    weights[u].append([v,w])
    weights[v].append([u,w])
#    print()
    #print(graph)
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
 
    # print all the vertex with same cycle
    for i in range(0, cyclenumber):
        m=101 
        # Print the i-th cycle
        #print("Cycle Number %d:" % (i+1), end = " ")
        for x in range(len(cycles[i])-1):
            print(x, end = "\n")
            #print("Weights for", cycles[i][x])
            #print("Weights for", cycles[i][x+1])

            num1=cycles[i][x]
            num2=cycles[i][x+1]
            #print("Weights for", weights[num1])
            #print("Weights for", weights[num2])
            for j in weights[num1]:
                #print(j[0])
                if(j[0]==num2):
                    #print("Found it!:",num2)
                    
                    if(j[1]<m):
                        print("Weight is", j[1])
                        m=j[1]
                        print("a1",num1)
                        print("a2",num2)
                    break

            print()

        print()

# Python3 program to print all the cycles
# in an undirected graph
N = 500
 
# variables to be used
# in both functions
graph = [[] for i in range(N)]
cycles = [[] for i in range(N)]
weights = [[] for i in range(N)]
#print(weights)
"""
for i in range (N-1):
    addEdge(i,i+1,100)

    # add edges
print("weights")
print(weights[0])
print(weights[N-1])
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

#print("weights")
#print(weights[2])

    #addEdge(10, 11)
    #addEdge(11, 12)
    #addEdge(11, 13)
    #addEdge(12, 13)
 
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

print(cycles)
"""
# Driver Code
if __name__ == "__main__":
 
    # add edges
    addEdge(1, 2,1)
    addEdge(2, 3,2)
    addEdge(3, 4,2)
    addEdge(4, 6,3)
    addEdge(4, 7,4)
    addEdge(5, 6,5)
    addEdge(3, 5,6)
    addEdge(7, 8,7)
    addEdge(6, 10,1)
    addEdge(5, 9,2)
    addEdge(10, 9,3)
    #addEdge(10, 11)
    #addEdge(11, 12)
    #addEdge(11, 13)
    #addEdge(12, 13)
 
    # arrays required to color the
    # graph, store the parent of node
    color = [0] * N
    par = [0] * N
 
    # store the numbers of cycle
    cyclenumber = 0
 
    # call DFS to mark the cycles
    dfs_cycle(1, 0, color, par)
 
    # function to print the cycles
    printCycles()
"""
