#!/usr/bin/env python3

print( "enter the numbers to be sorted")	#give numbers with tab 
alist=list(map(int,input().split()))
print('\v')
print( "original list:")
print (alist)
print('\v')
height=[]


import time
start_time = time.time()
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
        # splitpoint is partitioning index, alist[] is now
        # at right place
       splitpoint = partition(alist,first,last)
       # Separately sort elements before
        # partition and after partition
       quickSortHelper(alist,first,splitpoint-1)           
       quickSortHelper(alist,splitpoint+1,last)

# The main function that implements QuickSort
# alist[] --> list to be sorted,
# first --> Starting index,
# last --> Ending index
 
# Function to do Quick sort
def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark

quickSort(alist)
print('1 . Sorted numbers by a Quicksort are : ')
print(alist)
r=time.time() - start_time
print("--- %s seconds for Quicksort ---" % (r))               #getting the running time
height.append(r)                                              #to get the height for the graph


print('\v')


import time
start_time = time.time()
def mergeSort(alist):
    
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
     # create temp arrays
        mergeSort(lefthalf)
        mergeSort(righthalf)
      # Merge the temp arrays back
        i=0     # Initial index of first subarray
        j=0     # Initial index of second subarray
        k=0     # Initial index of merge subarray
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            # Copy the remaining elements of L[], if there are any
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            # Copy the remaining elements of R[], if there are any
            j=j+1
            k=k+1

mergeSort(alist)
print('2 . Sorted numbers by a Mergesort are :  ')
print(alist)
r2=time.time() - start_time
print("--- %s seconds for Mergesort ---" % (r2))           #getting the running time
height.append(r2)                                          #to get the height for the graph


print('\v')


import time
start_time = time.time()
def bubbleSort(alist):
    n = len(alist)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if alist[j] > alist[j+1] :
                alist[j], alist[j+1] = alist[j+1], alist[j]

bubbleSort(alist)
print('3 . Sorted numbers by a Bubblesort are : ')
print(alist)
r3=time.time() - start_time
print("--- %s seconds for Bubblesort ---" % (r3))                       #getting the running time
height.append(r3)                                                       #to get the height for the graph


print('\v')


import time
start_time = time.time()
def insertionSort(alist):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(alist)):
 
        key = alist[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < alist[j] :
                alist[j+1] = alist[j]
                j -= 1
        alist[j+1] = key

insertionSort(alist)
print('4 . Sorted numbers by a Insertionsort are : ')
print(alist)
r4=time.time() - start_time
print("--- %s seconds for Insertionsort ---" % (r4))                 #getting the running time
height.append(r4)                                                    #to get the height for the graph


print('\v')


import time
start_time = time.time()
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(alist, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and alist[i] < alist[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and alist[largest] < alist[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        alist[i],alist[largest] = alist[largest],alist[i]  # swap
 
        # Heapify the root.
        heapify(alist, n, largest)
 
# The main function to sort an array of given size
def heapSort(alist):
    n = len(alist)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(alist, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        alist[i], alist[0] = alist[0], alist[i]   # swap
        heapify(alist, i, 0)
 
heapSort(alist)
n = len(alist)
print('5 . Sorted numbers by a Heapsort are : ')
print(alist)
r5=time.time() - start_time
print("--- %s seconds for Heapsort ---" % (r5))                            #getting the running time
height.append(r5)                                                          #to get the height for the graph


print('\v')
tick_label=[]

import matplotlib.pyplot as plt
import numpy as np
# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5]

# heights of bars


# labels for bars
tick_label = ['quick', 'merge', 'bubble', 'insertion', 'heap']
y_pos = np.arange(len(tick_label))
# plotting a bar chart
plt.bar(y_pos, height,align='center',
		width = 0.8, color = ['red', 'blue'])


plt.xticks(y_pos, tick_label)

# naming the x-axis
plt.xlabel('x - axis = sorting')
# naming the y-axis
plt.ylabel('y - axis = running time in seconds')
# plot title
plt.title('Running time for the sorting functions!')

# function to show the plot
plt.show()
