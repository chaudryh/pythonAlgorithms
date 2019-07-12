
# This is supposed to be a merge sort

import time
start_time = time.time()

def mergeSort(myList):
	mergeSort2(myList, 0, len(myList)-1)
	
def mergeSort2(myList, first, last):
	if first < last:
		middle = (first + last)//2
		mergeSort2(myList, first, middle)
		mergeSort2(myList, middle+1, last)
		merge(myList, first, middle, last)
		
def merge(myList, first, middle, last):
	L = myList[first:middle+1]
	R = myList[middle+1:last+1]
	L.append(2**30)
	R.append(2**30)
	i = j = 0
	
	for k in range (first, last+1):
		if L[i] <= R[j]:
			myList[k] = L[i]
			i += 1
		else:
			myList[k] = R[j]
			j += 1

someList = [33, 81, 560, 1244, 17, 97, 251, 6, 729, 116, 1002]
mergeSort(someList)
print(someList)

print((time.time() - start_time))
