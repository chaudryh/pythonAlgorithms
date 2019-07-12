# This supposed to be a quick sort

import time
start_time = time.time()

def quick_sort(myList):
        p = partition(myList, 1, len(myList)-1)
        partition(myList, 0, p-1)
        partition(myList, p+1, len(myList)-1)
        return (myList)
	
def get_pivot(myList, low, hi):
	mid = (hi + low) // 2
	s = sorted([myList[low], myList[mid], myList[hi]])
	if s[1] == myList[low]:
		return low
	elif s[1] == myList[mid]:
		return mid
	return hi
	
def partition(myList, low, hi):
	pivotIndex = get_pivot(myList, low, hi)
	pivotValue = myList[pivotIndex]
	myList[pivotIndex], myList[low] = myList[low], myList[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if myList[i] < pivotValue:
			border += 1
			myList[i], myList[border] = myList[border], myList[i]
	myList[low], myList[border] = myList[border], myList[low]

	return (border)
			
someList = [3, 8, 2, 4, 1, 5, 6, 7, -5, -9]
print(quick_sort(someList))

print((time.time() - start_time))
