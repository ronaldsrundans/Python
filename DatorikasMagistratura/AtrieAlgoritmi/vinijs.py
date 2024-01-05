
"""
# Python3 program to print all the cycles
# in an undirected graph
N = 15
 
# variables to be used
# in both functions
graph = [[] for i in range(N)]
cycles = [[] for i in range(N)]
weights = [[] for i in range(N)]
rows, cols = (N, N)
arr = [[]*cols]*rows
print(arr)


""" 
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
    print(u,v)

    weights[u].append([v,w])
    weights[v].append([u,w])

    print()
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

# Python3 program to print all the cycles
# in an undirected graph
N = 15
 
# variables to be used
# in both functions
graph = [[] for i in range(N)]
cycles = [[] for i in range(N)]
weights = [[] for i in range(N)]
print(weights)
adj={}
rows, cols = (N, N)
arr = [['x']*cols]*rows
#arr[0][0]=100
#print(arr[0][0])
print(arr)

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
print("arr1=",arr[1][2])
print("arr2=",arr[2][1])

print(arr)
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
print(weights)
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
