#https://www.lavivienpost.net/weighted-graph-as-adjacency-list/
#https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
class Edge : 
	#Constructor, Time O(1) Space O(1)
	def __init__(self, v, w) :
		self.connectedVetex = v 
		self.weight = w
 
    #Time O(1) Space O(1)
	def __str__(self):
		return "(" + str(self.connectedVetex) + "," + str(self.weight) + ")"
	
class GraphWeighted :
    #Constructor, Time O(1) Space O(1)
    def __init__(self, directed) :
        self.adj = {}
        self.directed = directed #true or false 
#Add edges including adding nodes, Time O(1) Space O(1)
    def addEdge(self, a, b, w) :    
        if a not in self.adj:
            self.adj[a] = []
        if b not in self.adj:
            self.adj[b] = []   	
        edge1 = Edge(b, w)	
        self.adj[a].append(edge1)
        if (self.directed == False) :
            edge2 = Edge(a, w)
            self.adj[b].append(edge2)
	#Find the edge between two nodes, Time O(n) Space O(1), n is number of neighbors 
    def findEdgeByVetex(self, a,  b) :
        ne = self.adj.get(a)
        for edge in ne:
            if edge.connectedVetex == b :
                return edge
        return None
    
    #Remove direct connection between a and b, Time O(1) Space O(1)
    def removeEdge(self, a, b) :
        ne1 = self.adj[a]
        ne2 = self.adj[b] 
        if ne1 == None or ne2 == None :
            return
        edge1 = self.findEdgeByVetex(a, b)
        ne1.remove(edge1)
        if (self.directed == False) :
            edge2 = self.findEdgeByVetex(b, a)
            ne2.remove(edge2)
        
    #Remove a node including all its edges, 
	#Time O(v) Space O(1), V is number of vertics in graph
    def removeNode(self, a) :       
        if self.directed == False:  #undirected
            ne1 = self.adj[a]
            for edge in ne1 :
                edge1 = self.findEdgeByVetex(edge.connectedVetex, a) 
                self.adj[edge.connectedVetex].remove(edge1)
        else : #directed
            for k, v in self.adj.items(): 
                edge2 = self.findEdgeByVetex(k, a)
                if edge2 is not None:
                    self.adj[k].remove(edge2);	
        self.adj.pop(a)
	#Check whether there is node by its key, Time O(1) Space O(1)
    def hasNode(self, key) :
        return key in self.adj.keys()
	
	#Check whether there is direct connection between two nodes, Time O(n), Space O(1)
    def hasEdge(self, a, b):
        edge1 = self.findEdgeByVetex(a, b)
        if self.directed : #directed
            return edge1 is not None
        else : #undirected or bi-directed
            edge2 = self.findEdgeByVetex(b, a)
            return edge1 is not None and edge2 is not None
 # Check there is path from src and dest
	# DFS, Time O(V+E), Space O(V)
    def hasPathDfs(self, src, dest) : 
        visited = {}
        return self.dfsHelper(src, dest, visited)
	
	#DFS helper, Time O(V+E), Space O(V) 
    def dfsHelper(self, v, dest, visited) :
        if v == dest:
            return True
        visited[v] = True
        for edge in self.adj[v] :
            u = edge.connectedVetex
            if u not in visited:
                return self.dfsHelper(u, dest, visited)
        return False

	
	#Check there is path from src and dest
	#BFS, Time O(V+E), Space O(V)
    def hasPathBfs(self, src, dest) : 
        visited = {} 
        q = [] 
        visited[src] = True
        q.append(src) 
        while q : 
            v = q.pop(0); 
            if v == dest: 
                return True 
            for edge in self.adj[v] :  
                u = edge.connectedVetex              
                if u not in visited:  
                    q.append(u)
                    visited[u] = True	    	        
        return False 
	# Print graph as hashmap, Time O(V+E), Space O(1)
    def printGraph(self) :
        for k, v in self.adj.items():
            print(str(k) + "-", end ="")
            for edge in v:
                print(edge, end="")
            print()

	#Traversal starting from src, DFS, Time O(V+E), Space O(V)
    def dfsTraversal(self, src) : 
        visited = {}
        self.helper(src, visited)
        print()
	
	#DFS helper, Time O(V+E), Space O(V) 
    def helper(self, v, visited) :
        visited[v] = True
        print(str(v) +" ",end="")
        for edge in self.adj[v] :
            u = edge.connectedVetex
            if u not in visited:               
                self.helper(u, visited)

	
    # Traversal starting from src, BFS, Time O(V+E), Space O(V)
    def bfsTraversal(self, src) : 
        q = [] 
        visited = {} 
        q.append(src) 
        visited[src] = True 
        while (len(q) > 0) : 
            v = q.pop(0) 
            print(str(v) + " ",end="");        
            for edge in self.adj[v] :   
                u = edge.connectedVetex
                if u not in visited:
                    q.append(u); 
                    visited[u] = True
        print()
    """
    def isCyclicUtil(self, v, visited, recStack):
 
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be popped from
        # recursion stack before function ends
        recStack[v] = False
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        #self.connectedVetex = v
        visited = [False] * (self.adj + 1)
        recStack = [False] * (self.adj + 1)
        for node in range(self.adj):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
    """
# Driver's code
if __name__ == "__main__":
    #e = Edge()
    g = GraphWeighted(True)#directed == True
    #g.directed == True
    g.addEdge(1, 2, 5)
    g.addEdge(1, 3, 6)
    g.addEdge(2, 3, 3)
    g.addEdge(3, 4, 2)
    g.printGraph() 
    print(g.bfsTraversal(1))
    g.bfsTraversal(1)
    """
    if g.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")
    """    
