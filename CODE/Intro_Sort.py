# Introsort begins with quicksort and if the recursion depth goes more than a particular limit
# it switches to Heapsort to avoid Quicksort's worse case O(N2) time complexity.
#
# Pseudo code for Intro Sort Sort:
# sort(A : array):
#     depthLimit = 2xfloor(log(length(A)))
#     introsort(A, depthLimit)
#
# Introsort(A, depthLimit):
#     n = length(A)
#     if n<=16:
#         insertionSort(A)
#     if depthLimit == 0:
#         heapsort(A)
#     else:
#         p = partition(A)  # using quick sort, the partition point is found 
#         Introsort(A[0:p-1], depthLimit - 1)
#         Introsort(A[p+1:n], depthLimit - 1)
#########################################################################################
import math
import statistics
import Insertion_Sort
import Heap_Sort
import Quick_Sort
 
def Introsort_Util(arr, begin, end, depthLimit):
    size = end - begin 
    
    if size < 16: # if the data set is small, call insertion sort 
        Insertion_Sort.insertion_sort(arr) 
        return
  
    if depthLimit == 0: # if the recursion limit is occurred call heap sort
        Heap_Sort.heapSort(arr)
        return
  
    pivot = statistics.median([begin, begin + size // 2, end])
    (arr[pivot], arr[end]) = (arr[end], arr[pivot])

    partitionPoint = Quick_Sort.pivot(arr, begin, end)
    Introsort_Util(arr, begin, partitionPoint - 1, depthLimit - 1) 
    Introsort_Util(arr, partitionPoint + 1, end, depthLimit - 1)
  
  
def Intro_Sort(arr, begin, end):
    depthLimit = 2 * math.log2(end - begin) 
    Introsort_Util(arr, begin, end, depthLimit)
    return arr
   
def main(arr):
    a=Intro_Sort(arr, 0, len(arr) - 1)
    return a
