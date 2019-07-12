# This is supposed to be a selction sort

import time
start_time = time.time()

def selectionSort(myList):
    for i in range (0, len(myList) - 1):
        minIndex = i
        for j in range (i+1, len(myList)):
            if myList[j] < myList[minIndex]:
                minIndex = j

        if minIndex != i:
            myList[i], myList[minIndex] = myList[minIndex], myList[i]

    return myList

someList = [3, 8, 2, 4, 1, 5, 6, 7, -5, -9]
print(selectionSort(someList))

print((time.time() - start_time))
