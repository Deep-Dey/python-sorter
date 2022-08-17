from typing import Any


def pivot(arr: list, s: int, n: int) -> int:
    i:int = s - 1  # Set the pivot index
    pivot: Any = arr[s]

    for j in range((s+1), n):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[n] = arr[n], arr[i+1]

    return i+1


def quick_sort_fn(arr: list, s: int, n: int) -> list:
    if s < n:
        p: int = pivot(arr, s, n)
        quick_sort_fn(arr, s, p)
        quick_sort_fn(arr, p+1, n)
    return arr


def quick_sort(arr: list) -> list:
    '''
    Quicksort is an algorithm based on divide and conquer approach in which the array is split into subarrays and these sub-arrays are recursively called to sort the elements.
    
    ```
    quickSort(array, leftmostIndex, rightmostIndex)
      if (leftmostIndex < rightmostIndex)
        pivotIndex <- partition(array,leftmostIndex, rightmostIndex)
        quickSort(array, leftmostIndex, pivotIndex)
        quickSort(array, pivotIndex + 1, rightmostIndex)
    
    partition(array, leftmostIndex, rightmostIndex)
      set rightmostIndex as pivotIndex
      storeIndex <- leftmostIndex - 1
      for i <- leftmostIndex + 1 to rightmostIndex
      if element[i] < pivotElement
        swap element[i] and element[storeIndex]
        storeIndex++
      swap pivotElement and element[storeIndex+1]
    return storeIndex + 1
    ```
    '''
    arr = quick_sort_fn(arr, 0, len(arr)-1)
    return arr