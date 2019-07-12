# This is supposed to be a binary search tree

import time

start_time = time.time()

class Node:
	def __init__(self, val):
		self.value = val
		self.leftChild = None
		self.rightChild = None
		
	def insert(self, data):
		if self.value == data:
			return False
			
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node(data)
				return True

		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True
				
	def search(self, data):
		if(self.value == data):
			return True
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.search(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.search(data)
			else:
				return False
				
	def preorder(self):
		if self:
			print (str(self.value))
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()

	def postorder(self):
		if self:
			if self.leftChild:
				self.leftChild.postorder()
			if self.rightChild:
				self.rightChild.postorder()
			print (str(self.value))

	def inorder(self):
		if self:
			if self.leftChild:
				self.leftChild.inorder()
			print (str(self.value))
			if self.rightChild:
				self.rightChild.inorder()

class Tree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def search(self, data):
		if self.root:
			return self.root.search(data)
		else:
			return False
			
	def preorder(self):
		if self.root is not None:
			#print("PreOrder")
			self.root.preorder()
		
	def postorder(self):
		if self.root is not None:
			#print("PostOrder")
			self.root.postorder()
			
	def inorder(self):
		if self.root is not None:
			#print("InOrder")
			self.root.inorder()

bst = Tree()

myList = [33, 218, 64, 459, 193, 761, 903]

for i in range(len(myList)):
    bst.insert(myList[i])

bst.insert(211)
bst.search(193)
    
bst.inorder()

print((time.time() - start_time))

