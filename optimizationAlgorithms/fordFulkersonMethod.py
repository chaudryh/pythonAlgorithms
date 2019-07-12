# This is supposed to be the Ford Fulkerson method
  
import time

start_time = time.time()

class Graph:
  
    def __init__(self,graph):
        self.graph = graph 
        self. ROW = len(graph)
      
    def BFS(self,s, t, parent):
 
        # Mark all the vertices as not visited
        visited =[False]*(self.ROW)
         
        # Create a list for BFS
        list=[]
         
        # Mark the source node as visited
        list.append(s)
        visited[s] = True
         
        # Standard BFS Loop
        while list:
 
            #Delist a vertex from list and print it
            u = list.pop(0)
         
            # Get all adjacent vertices of the vertex u
            # If a adjacent has not been visited, mark it
            # as unvisited
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    list.append(ind)
                    visited[ind] = True
                    parent[ind] = u
 
        return True if visited[t] else False
             
     
    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS stores the path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # No flow initially
 
        while self.BFS(source, sink, parent) :
 
            # Find the maximum flow through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # Reverse edges along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
 
   
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
 
g = Graph(graph)
 
source = 0; sink = 5
  
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
 
print((time.time() - start_time))
