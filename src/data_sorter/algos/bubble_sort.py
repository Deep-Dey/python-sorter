from typing import Any


def bubble_sort(arr: list) -> list:
    '''
    Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.

    ```
    procedure bubble_sort(A : list of sortable items)
        n := length(A)
        repeat
            swapped := false
            for i := 1 to n - 1 inclusive do
                if A[i - 1] > A[i] then
                    swap(A[i - 1], A[i])
                    swapped = true
                end if
            end for
            n := n - 1
        until not swapped
    end procedure
    ```
    '''
    for i in range(len(arr)):
        for j in range((len(arr)-i-1)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
