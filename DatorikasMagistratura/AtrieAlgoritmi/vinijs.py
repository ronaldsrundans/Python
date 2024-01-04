#https://www.lavivienpost.net/weighted-graph-as-adjacency-list/
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
        print("q=",q)
        while q :
            print("q=",q) 
            v = q.pop(0); 
            print("v=",v)
            if v == dest:
                print("True=", v) 
                return True 
            for edge in self.adj[v] :  
                u = edge.connectedVetex  
                print("u=",u)            
                if u not in visited:  
                    q.append(u)
                    visited[u] = True	    	        
        return False 
	# Print graph as hashmap, Time O(V+E), Space O(1)
    def printGraph(self) :
        for k, v in self.adj.items():# k=virsotne
            print(str(k) + "-", end ="")
            for edge in v:# v=edge objects (savienotas virsotnes un svari)
                print(edge, end="")
            print()
    def printGraph2(self) :
        for k, v in self.adj.items():
            #print("k=",k)
            #print("v=",v)
            print(str(k) + "-", end ="")
            for edge in v:
                #print("EDGE=",edge)
                print(edge, end="")
            print()

	#Traversal starting from src, DFS, Time O(V+E), Space O(V)
    def dfsTraversal(self, src) : 
        visited = {}
        self.helper(src, visited)
        print()
    def dfsTraversal2(self, src) : 
        visited = {}#kopa ar apmekletajam virsotnem
        recStack = {}#kopa ar apmekletajam virsotnem
        self.helper2(src, visited,recStack)
        print()
	
	#DFS helper, Time O(V+E), Space O(V) 
    def helper(self, v, visited) :
        visited[v] = True
        print(str(v) +" ",end="")
        for edge in self.adj[v] :
            u = edge.connectedVetex# u=savienota virsotne
            if u not in visited:               
                self.helper(u, visited)
	
	#DFS helper, Time O(V+E), Space O(V) 
    def helper2(self, v, visited,recStack) :
        #if v in visited:
        #    print("Visited!")
        recStack[v] = True
        #print("Visited:")
        #print(visited)
        #print("Stack")
        #print(recStack)
        visited[v] = True
        for edge in self.adj[v] :
            u = edge.connectedVetex
            if u in visited:
                print("\n")
                print("Found cycle to:",u)    
                print("From node:", v)
                #print(":",recStack)
                print("Path:",visited)
                #for i in visited:
                #    print(i)
                print("\n")


        #print("v=", str(v))
        #v=current vertex, visited= array, and recursion stack.
        #pievieno check for vai kaimiņu virsotnes ir jau visited masīvā
        print(str(v) +" ",end="")
        for edge in self.adj[v] :
            u = edge.connectedVetex# u=savienota virsotne
            if u not in visited:               
                self.helper2(u, visited,recStack)
	
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

# Driver's code
if __name__ == "__main__":
    #e = Edge()
    g = GraphWeighted(True)#directed == True
    #g.directed == True

    g.addEdge(0, 1, 5)
    g.addEdge(0, 2, 5)
    g.addEdge(1, 2, 5)
    g.addEdge(1, 3, 6)
    g.addEdge(2, 3, 3)
    g.addEdge(2, 0, 3)
    g.addEdge(3, 4, 2)

    #g.printGraph2() 

    #print(g.bfsTraversal(1))
    #g.bfsTraversal(0)
    g.dfsTraversal2(0)
    #g.dfsTraversal2(1)
    #g.dfsTraversal2(2)
    #g.dfsTraversal2(3)
    #g.dfsTraversal2(4)

    #print(g.hasPathBfs(1,0))#True
    #print(g.hasPathBfs(3,0))#True

    """
    if g.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")
    """   
