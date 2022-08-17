def heapify(arr: list, n: int, i: int) -> None:
    maximum: int = i
    l: int = 2 * i + 1
    r: int = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        maximum = l

    if r < n and arr[maximum] < arr[r]:
        maximum = r

    if maximum != i:
        arr[i], arr[maximum] = arr[maximum], arr[i]
        heapify(arr, n, maximum)


def heap_sort(arr: list) -> list:
    '''
    Heapsort is a comparison-based sorting algorithm.
    In the first step, the Heapsort algorithm involves preparing the list by first turning it into a max heap.
    In the second step, a sorted array is created by repeatedly removing the largest element from the heap and inserting it into the array.

    ```
    HeapSort()  
        1.  Call the buildMaxHeap() function on the list. Also referred to as heapify(), this builds a heap from a list in O(n) operations.
        2.  Swap the first element of the list with the final element. Decrease the considered range of the list by one.
        3.  Call the siftDown() function on the list to sift the new first element to its appropriate index in the heap.
        4.  Go to step (2) unless the considered range of the list is one element.
    ```
    '''
    n: int = len(arr)
    for i in range(n, -1, -1):  # Build a maxheap
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap Kore Max take laste Pathachhe
        heapify(arr, i, 0)
    
    return arr