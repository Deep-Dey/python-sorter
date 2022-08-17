def stooge_sort_fn(arr: list, l: int, h: int) -> list: 
    if l < h:
        if arr[l]>arr[h]: 
            arr[l], arr[h] = arr[h], arr[l]
        
        if h-l > 1: ## If there are more than 2 elements in the array(starts from 0)
            t = (int)((h-l + 1)/3) 
            stooge_sort_fn(arr, l, (h-t)) ## Recursively sort first 2/3 elements 
            stooge_sort_fn(arr, l + t, (h)) ## Recursively sort last 2/3 elements 
   
            stooge_sort_fn(arr, l, (h-t)) ## Recursively sort first 2/3 elements again to confirm 

    return arr

def stooge_sort(arr: list) -> list:
    '''
    Stooge sort is a recursive sorting algorithm.
    The running time of the algorithm is thus slower compared to reasonable sorting algorithms
    and a canonical example of a fairly inefficient sort. It is however more efficient than Slowsort.
    ```
    stooge_sort()
        1.  If the value at the start is larger than the value at the end, swap them.
        2.  If there are 3 or more elements in the list, then:
            i.      Stooge sort the initial 2/3 of the list
            ii.     Stooge sort the final 2/3 of the list
            iii.    Stooge sort the initial 2/3 of the list again
    ```
    '''
    return stooge_sort_fn(arr, 0, len(arr)-1)