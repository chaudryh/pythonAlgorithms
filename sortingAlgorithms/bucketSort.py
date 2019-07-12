# This is supposed to be a bucket sort

import time
start_time = time.time()


def bucketSort(myList):

    size = len(myList)
    
    maximum = 0
    for num in myList:
        if num > maximum:
            maximum = num
            
    minimum = maximum
    for num in myList:
        if num < minimum:
            minimum = num

    bucketWidth = int(((maximum - minimum) + 3)/4)

    range1 = minimum  + bucketWidth
    range2 = minimum + 2*(bucketWidth)
    range3 = minimum + 3*(bucketWidth)
    range4 = minimum + 4*(bucketWidth)
    
    bucket1, bucket2, bucket3, bucket4 = [], [], [], []
    
    buckets = list()
    buckets.append(bucket1)
    buckets.append(bucket2)
    buckets.append(bucket3)
    buckets.append(bucket4)

    for i in range(size):
        if myList[i] in range(range1):
            bucket1.append(myList[i])
        elif myList[i] in range(range2):
            bucket2.append(myList[i])
        elif myList[i] in range(range3):
            bucket3.append(myList[i])
        elif myList[i] in range(range4):
            bucket4.append(myList[i])

    sortedList = []

    for bucket in buckets:
        if (len(bucket) > 1):
            sortedList.extend(bucketSort(bucket))
        else:
            sortedList.extend(bucket)
    return sortedList
                   
someList = [33, 81, 560, 1244, 17, 97, 251, 6, 729, 116, 1002]
print(bucketSort(someList))

print((time.time() - start_time))
