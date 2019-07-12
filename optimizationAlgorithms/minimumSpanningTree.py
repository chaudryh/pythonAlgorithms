# This is supposed to be a minimum spanning tree
  
import time

start_time = time.time()

class Graph:

	def __init__(self,vertices):
		self.V= vertices 
		self.graph = []

	# function to add an edge to graph
	def addEdge(self,u,v,w):
		self.graph.append([u,v,w])

	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	def join(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		# Join by Rank
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		#Increment its rank by one
		else :
			parent[yroot] = xroot
			rank[xroot] += 1

	# The main function to construct the mst
	def KruskalMST(self):

		result =[] # Used for the resultant MST

		i = 0 # Used for sorted edges
		e = 0 # Used for result[]

		
		self.graph = sorted(self.graph,key=lambda item: item[2])
		#print self.graph

		parent = [] ; rank = []

		for node in range(self.V):
			parent.append(node)
			rank.append(0)
	
		# Number of edges to be taken is V-1
		while e < self.V -1 :

			# Increment the index for next iteration
			u,v,w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent ,v)

			# Increment the index of result for next edge
			if x != y:
				e = e + 1
				result.append([u,v,w])
				self.join(parent, rank, x, y)		 

		print ("Following are the edges in Minimum Spanning Tree")
		for u,v,weight in result:
			print ("%d -> %d = %d" % (u,v,weight))


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()

print((time.time() - start_time))
