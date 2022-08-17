import math
import statistics

from data_sorter.algos.heap_sort import heap_sort
from data_sorter.algos.insertion_sort import insertion_sort
from data_sorter.algos.quick_sort import pivot


def introsort_util(arr: list, begin: int, end: int, depthLimit: int) -> list:
    size = end - begin

    if size < 16:  # if the data set is small, call insertion sort
        return insertion_sort(arr)

    if depthLimit == 0:  # if the recursion limit is occurred call heap sort
        return heap_sort(arr)

    _pivot = statistics.median([begin, begin + size // 2, end])
    (arr[_pivot], arr[end]) = (arr[end], arr[_pivot])

    partitionPoint = pivot(arr, begin, end)
    introsort_util(arr, begin, partitionPoint - 1, depthLimit - 1)
    introsort_util(arr, partitionPoint + 1, end, depthLimit - 1)


def intro_sort(arr: list) -> list:
    '''
    Introsort begins with quicksort and if the recursion depth goes more than a particular limit it switches to Heapsort to avoid Quicksort's worse case O(N2) time complexity.
    ```
    sort(A : array):
        depthLimit = 2*floor(log(length(A)))
        introsort(A, depthLimit)
    
    Introsort(A, depthLimit):
        n = length(A)
        if n<=16:
            insertionSort(A)
        if depthLimit == 0:
            heapsort(A)
        else:
            p = partition(A)  # using quick sort, the partition point is found
            Introsort(A[0:p-1], depthLimit - 1)
            Introsort(A[p+1:n], depthLimit - 1)
    ```
    '''
    begin: int = 0
    end: int = len(arr) - 1
    depthLimit: float = 2 * math.log2(end - begin)
    introsort_util(arr, begin, end, depthLimit)
    return arr