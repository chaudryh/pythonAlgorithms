# This is supposed to be a radix sort

import time
start_time = time.time()

def radixSort( myList ):
  radix = 10
  maxLength = False
  temp , placement = -1, 1

  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( radix )]

    # split myList between lists
    for  i in myList:
      temp = i // placement
      buckets[temp % radix].append( i )
      if maxLength and temp > 0:
        maxLength = False

    # empty lists into aList array
    a = 0
    for bucket in range( radix ):
      bucket = buckets[bucket]
      for i in bucket:
        myList[a] = i
        a += 1

    # move to next digit
    placement *= radix
  return myList

someList = [380007694, 80074, 297, 444, 173, 5870069, 60041, 720094]
print(radixSort(someList))

print((time.time() - start_time))
