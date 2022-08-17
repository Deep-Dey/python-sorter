def gnome_sort(arr: list) -> list:
    '''
    The gnome sort is a sorting algorithm which is similar to insertion sort in that it works with one item at a time but gets the item to the proper place by a series of swaps, similar to a bubble sort.
    ```
    procedure gnomeSort(a[]):
        pos := 0
        while pos < length(a):
            if (pos == 0 or a[pos] >= a[pos-1]):
                pos := pos + 1
            else:
                swap a[pos] and a[pos-1]
                pos := pos - 1
    ```
    '''
    n: int = len(arr)
    pos: int = 0
    while pos < n:
        if pos == 0:
            pos = pos+1
        elif arr[pos] >= arr[pos-1]:
            pos = pos+1
        else:
            arr[pos], arr[pos-1] = arr[pos-1], arr[pos]
            pos = pos-1
    
    return arr
