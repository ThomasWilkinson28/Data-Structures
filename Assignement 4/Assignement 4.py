#“I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity.”
import random
#Define class for the vertex's
class Vertex:
    def __init__(self, key):
        #Create a variable for the vertex number and an array storing all its connections
        self.id = key
        self.connectedTo = {}

    #Create function for adding new nodes next to already formed ones
    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    #Create function which returns all the connections of a node
    def getConnections(self):
        return self.connectedTo.keys()

#Define a class for the graph
class Graph:
    def __init__(self):
        #Create an array for the vertices in the graph
        self.vertList = {}

    #Create a function for adding new vertices
    def addVertex(self, key):
        #Make each vertices objects of the Vertex class
        newVertex = Vertex(key)
        #Assign each new vertex a location inf the verList array corresponding to its value
        self.vertList[key] = newVertex

    #Create a function for getting back a vertex by inputing its key
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    
    #Create a function for obtaining the diameter of the graph
    def diameter(self):
        #Create variable for tracking to largest diameter of the graph
        max_diameter = 0
        #Cycle through all vertices in the graph
        for vertex in self.vertList.values():
            #Find the maxDistance 
            tot_distance = self.BFS(vertex)
            max_diameter = max(max_diameter, tot_distance)
        return max_diameter

    #Create a function to add new vertex's next to existing ones and form edges between the added vertex and the existing one
    def addEdge(self, p, i, cost=0):
        if p not in self.vertList:
            #If p is not already a vertex add it
            self.addVertex(p)
        if i not in self.vertList:
            #If i is not already a vertex add it
            self.addVertex(i)
        #Use the addNeighbor function from the vertex class to make an edge between them
        self.vertList[p].addNeighbor(self.vertList[i], cost)
        self.vertList[i].addNeighbor(self.vertList[p], cost)

    #Create function for breadth first search algorithm
    def BFS(self, vertice):
        #Create a set to keep track of the visited vertices
        visited = set()
        #Create an array queue used to traverse the graph, include the distance from which it is to the starting vertex
        queue = [(vertice, 0)]
        #Define variable for keeping track of distance between nodes
        tot_distance = 0
        #Run while loop until queue is empty
        while queue:
            #Take first vertex in queue
            vertex, distance = queue.pop(0)
            #Make current vertex as visited to avoid processing it again
            visited.add(vertex)
            #Update total distance 
            tot_distance = max(tot_distance, distance)
            #Cycle through the neighbors of current vertex
            for neighbor in vertex.getConnections():
                if neighbor not in visited:
                    #Add neighbor to queue if it hasn't already been visited
                    queue.append((neighbor, distance + 1))
                    #Make it so that it dosn't get visited again
                    visited.add(neighbor)
        return tot_distance

    #Create a function for depth first search algorithm
    def DFS(self, start):
        #Create a set to keep track of the visited vertices
        visited = set()
        #Create an array stack used to traverse the graph, include the distance from which it is to the starting vertex
        stack = [(start, 0)]
        #Define variable for keeping track of distance between nodes
        tot_distance = 0
        #Run while stack is not empty 
        while stack:
            #Take first vertex on stack along with its distance from the first vertex
            vertex, distance = stack.pop()
            #Make current vertex as visited to avoid processing it again
            visited.add(vertex)
            #Update total distance 
            tot_distance = max(tot_distance, distance + 1)
            #Cycle through the neighbors of current vertex
            for neighbor in vertex.getConnections():
                if neighbor not in visited:
                    #Add neighbor to stack if it hasn't already been visited
                    stack.append((neighbor, distance + 1))
                    #Make it so that it dosn't get visited again
                    visited.add(neighbor)       
        return tot_distance
    
def generateRandomTree(n):
    #Create variable for the graph class
    generatedTree = Graph()
    #Cycle through given n value creating two random nodes with an edge in between them
    for i in range(1, n-1):
        p = random.randint(0, i-1)
        generatedTree.addEdge(p, i)
    return generatedTree

def generateRandomEdges(inputedGraph, k):
        added_edges = 0
        connection = 0
        #Make sure to only add specified number of edges
        while added_edges < k:
            #Pick two random vertices out of the ones in the inputed graph
            v1 = random.randint(0, len(inputedGraph.vertList) - 1)
            v2 = random.randint(0, len(inputedGraph.vertList) - 1)
            vertex1 = inputedGraph.getVertex(v1)
            #Cycle through the connections of one vertex to make sure they arent already connected
            for connect1 in vertex1.getConnections():
                #If the v1 is already connected to v2 set connection condition true
                if (connect1 == v2):
                    connection = 1
            #If v1 and v2 are not the same vertex and if they are not connected add new connection between them
            if v1 != v2 and connection == 0:
                inputedGraph.addEdge(v1, v2)
                added_edges += 1 

# Experiment
if __name__ == "__main__":
    #Part 1
    #Generate Random tree using function
    generateTree = generateRandomTree(9)
    print("Adjacency list of generated tree:")
    #Cycle through the vertices of the tree
    for vertex in generateTree.vertList.values():
        #Print each vertex
        print("Vertex:", end = ' ')
        print(vertex.id, end =', ')
        print("Connections:", end=' ')
        #Print Connections of each vertex
        for connect in vertex.getConnections():
            print(connect.id, end=' ')
        print("\n")
    print("Graph Diameter:", generateTree.diameter())
    print("\n")
    #Add 8 edges to the generated tree
    generateRandomEdges(generateTree, 8)
    print("Adjacency list of generated tree with 8 added edges:")     
       #Cycle through the vertices of the tree
    for vertex in generateTree.vertList.values():
        #Print each vertex
        print("Vertex:", end = ' ')
        print(vertex.id, end =', ')
        print("Connections:", end=' ')
        #Print Connections of each vertex
        for connect in vertex.getConnections():
            print(connect.id, end=' ')
        print("\n")
    print("Graph Diameter:", generateTree.diameter())

    #Part 2  
    k = 10
    n_values = [100, 200, 400, 800, 1600]
    print("Part 2:")
    #Cycle through n_values
    for n in n_values:
        avg_tree_diameter = 0
        avg_graph_diameter = 0
        
        #Cycle through k
        for _ in range(k):
            #Create tree with n vertices
            tree = generateRandomTree(n)
            #Find tree diameter
            tree_diameter = tree.diameter()
            #Add it to other calculated diameters
            avg_tree_diameter += tree_diameter
            #Add n edges between all the vertices
            generateRandomEdges(tree, n)
            #Find the new diameter of the now graph
            graph_diameter = tree.diameter()
            #Add it to the other calculated graph diameters
            avg_graph_diameter += graph_diameter
        
        #Find average graph and tree diameters by dividing added sum of all by sample size
        avg_tree_diameter /= k
        avg_graph_diameter /= k
        
        #Print average diameters
        print(f"Average Tree Diameter for n={n}: {avg_tree_diameter}")
        print(f"Average Graph Diameter for n={n}: {avg_graph_diameter}")
  
    #Part 3
    print("Part 3:")
    #Cycle through n_values
    for n in n_values:
        tot_ratio = 0
        
        #Cycle through k
        for _ in range(k):
            #Create tree with n vertices
            tree = generateRandomTree(n)
            #Add n edges between all the vertices
            generateRandomEdges(tree, n)
            #Pick a random vertex out of the ones in the graph
            v = random.randint(0, len(tree.vertList) - 1)
            vertex = tree.getVertex(v)
            #Compute traversal edge sum from v using BFS
            b = tree.BFS(vertex)
            #Compute traversal edge sum from v using DFS
            a = tree.DFS(vertex)
            #Calculate ratio and add it to total sum of ratios
            ratio = a/b
            tot_ratio = tot_ratio + ratio
        
        #Find average ratio by dividing added sum of all by sample size
        tot_ratio /= k
        #Print average ratio
        print(f"Average Ratio for n={n}: {tot_ratio}")   
