# This is supposed to be a red black tree

import time

start_time = time.time()

class BinaryTree(object):
    def __init__(self, data=None, isALeaf=True, colour='r', left=None, right=None):
        # binary tree initializing
        self.data = data
        self.isALeaf = isALeaf
        self.colour = colour
        self.left = left
        self.right = right

class BinarySearchTree(object):
    # binary tree set up
    def __init__(self, root=None):
        self.root = BinaryTree()

    def insert(self, value):
        self.root = recInsert(self.root, value)
        self.root.colour = 'b'

    def searchPath(self, val):
        path = []
        node = self.root
        while node is not None:
            path.append(node.data)
            if val < node.data:
                node = node.left
            elif val > node.data:
                node = node.right
            else:
                node = None
        return path

    def totalDepth(self):
        if self.root.isALeaf:
            return 0
        else:
            return recTotalDepth(self.root)

def recTotalDepth(node, curDepth=0):
    if node.isALeaf:
        return 0
    else:
        leftDepth = 0
        rightDepth = 0
        if node.left is not None:
            leftDepth = recTotalDepth(node.left, curDepth+1)
        if node.right is not None:
            rightDepth = recTotalDepth(node.right, curDepth+1)

        return leftDepth + curDepth + rightDepth

def printTree(node, indent=0):
    if node.isALeaf:
        return
    else:
        if node.right is not None:
            printTree(node.right, indent+4)
        print(" "*indent + str(node.data) + node.colour)
        if node.left is not None:
            printTree(node.left, indent+4)

def recInsert(node, value):
        if node.isALeaf:
            return BinaryTree(value, False, 'r', BinaryTree(None, True, 'b'), BinaryTree(None, True, 'b'))
        elif value > node.data:
            node.right = recInsert(node.right, value)
            if node.colour == 'r':
                return node
            else: 
                if node.right.colour == 'r':
                    if node.right.right.colour == 'r':
                        # red-red conflict on the right-right children
                        return rightRight(node)
                    elif node.right.left.colour == 'r':
                        # red-red conflict on the right-left children
                        return rightLeft(node)
                    else:
                        return node
                else:
                    return node
        else: 
            node.left = recInsert(node.left, value)
            if node.colour == 'r':
                return node
            else: 
                if node.left.colour == 'r':
                    if node.left.left.colour == 'r':
                        # red-red conflict on the left-left children
                        return leftLeft(node)
                    elif node.left.right.colour == 'r':
                        # red-red conflict on the left-right children
                        return leftRight(node)
                    else:
                        return node
                else:
                    return node

def delete(self, data):
    if self.root is None:
        return False		
    elif self.root.value == data:
        if self.root.leftChild is None and self.root.rightChild is None:
            self.root = None
        elif self.root.leftChild and self.root.rightChild is None:
            self.root = self.root.leftChild
        elif self.root.leftChild is None and self.root.rightChild:
            self.root = self.root.rightChild
        elif self.root.leftChild and self.root.rightChild:
            delNodeParent = self.root
            delNode = self.root.rightChild
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild
            self.root.value = delNode.value
            if delNode.rightChild:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.rightChild
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.leftChild = None
                    else:
                        delNodeParent.rightChild = None
        return True

def rightRight(node):
    # red-red conflict on right-right children
    child = node.right
    sib = node.left
    if sib.colour == 'r':
        child.colour = 'b'
        sib.colour = 'b'
        node.colour = 'r'
        return node
    else:
        node.right = child.left
        child.left = node
        child.colour = 'b'
        node.colour = 'r'
        return child

def rightLeft(node):
    # red-red conflict on right-left children
    child = node.right
    sib = node.left
    if sib.colour == 'r':
        child.colour = 'b'
        sib.colour = 'b'
        node.colour = 'r'
        return node
    else:
        grandchild = child.left
        child.left = grandchild.right
        node.right = grandchild.left
        grandchild.left = node
        grandchild.right = child
        grandchild.colour = 'b'
        node.colour = 'r'
        return grandchild

def leftLeft(node):
    # red-red conflict on right-right children
    child = node.left
    sib = node.right
    if sib.colour == 'r':
        child.colour = 'b'
        sib.colour = 'b'
        node.colour = 'r'
        return node
    else:
        node.left = child.right
        child.right = node
        child.colour = 'b'
        node.colour = 'r'
        return child

def leftRight(node):
    # red-red conflict on left-right children
    child = node.left
    sib = node.right
    if sib.colour == 'r':
        child.colour = 'b'
        sib.colour = 'b'
        node.colour = 'r'
        return node
    else:
        grandchild = child.right
        child.right = grandchild.left
        node.left = grandchild.right
        grandchild.right = node
        grandchild.left = child
        grandchild.colour = 'b'
        node.colour = 'r'
        return grandchild

def main():
    myTree = BinarySearchTree()
    #myList = [13,42,3,6,23,32,72,90,1,35,36,88,34,12,92,100,143,123,126,128]
    myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for i in myList:
        myTree.insert(i)

    printTree(myTree.root)
    print(myTree.searchPath(12))
    print(myTree.totalDepth())
    
main()

print((time.time() - start_time))
