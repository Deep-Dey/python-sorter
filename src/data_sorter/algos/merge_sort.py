def merge(arr: list, L: int, R: int) -> list:
    i: int = 0
    j: int = 0
    k: int = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i = i+1
        else:
            arr[k] = R[j]
            j = j+1
        k = k+1

    while i < len(L):
        arr[k] = L[i]
        i = i+1
        k = k+1

    while j < len(R):
        arr[k] = R[j]
        j = j+1
        k = k+1

    return arr


def merge_sort(arr: list) -> list:
    '''
    Merge Sort is a kind of Divide and Conquer algorithm in computer programming.
    ```
    MergeSort(A, p, r):
        if p > r 
            return
        q = (p+r)/2
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        merge(A, p, q, r)
    ```
    '''
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        arr = merge(arr, L, R)

    return arr
