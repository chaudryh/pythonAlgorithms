# This is supposed to be a heap sort

import time
start_time = time.time()

def parent(index):
    return (index-1)//2
 
def left(index):
    return index*2 + 1
 
def right(index):
    return index*2 + 2
 
def heapSort(myList,n) :
    init = int(n/2)       
    for i in range(init,-1,-1) :     
        maxHeapify(myList,i,n-1)
    for end in range(n-1,0,-1):     
        myList[end],myList[0] = myList[0],myList[end]
        maxHeapify(myList,0,end-1)
    return myList
 
def maxHeapify(myList, index,heapsize):
    lf = left(index)
    rt = right(index)
    if lf < heapsize and myList[lf] > myList[index]:
        largest = lf
    else:
        largest = index
    if rt < heapsize and myList[rt] > myList[largest]:
        largest = rt
    if largest != index:
        myList[largest], myList[index] = myList[index], myList[largest]
        maxHeapify(myList, largest,heapsize)
 
def buildHeap(myList):
    for i in range(len(myList)-1,-1,-1):
        maxHeapify(myList,i,len(myList))

def main():

    someList = [3, 8, 2, 4, 1, 5, 6, 7, -5, -9]
    
    buildHeap(someList)
    heapsize = len(someList)
    heapSort(someList,heapsize)
    print(someList)
 
main()

print((time.time() - start_time))

 
 
