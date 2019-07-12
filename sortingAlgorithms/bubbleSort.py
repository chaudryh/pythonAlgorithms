
# This is supposed to be a bubble sort

import time

start_time = time.time()

def bubbleSort(myList):
    for i in range(0, len(myList)-1):
        for j in range(0, len(myList)-1-i):
            if myList[j]>myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList

someList = [3, 8, 2, 4, 1, 5, 6, 7, -5, -9]
print(bubbleSort(someList))

print((time.time() - start_time))

