# This is supposed to be an insertion sort

import time
start_time = time.time()

def insertionSort(myList):
    for i in range(1, len(myList)):
        currentNum = myList[i]
       # x = 0
        for j in range(i-1, -2, -1):
           # x = j
            if myList[j] > currentNum:
                myList[j+1] = myList[j]
            else:
                break
        myList[j+1] = currentNum

    return myList

someList = [3, 8, 2, 4, 1, 5, 6, 7, -5, -9]
print(insertionSort(someList))

print((time.time() - start_time))
