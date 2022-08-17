from typing import Any


def cycle_sort(arr: list) -> list:
    '''
    It is based on the idea that the permutation to be sorted can be factored into cycles, which can individually be rotated to give a sorted result.
    
    ```
    cycle_sort()
        1. If the element is already at the correct position then
                do nothing.
        2. else
                we will write it to its intended position.
                That position is inhabited by a different element b, which we then have to move to its correct position.
                This process of displacing elements to their correct positions continues until an element is moved to the original position of a. This completes a cycle.
    ```
    '''
    n: int = len(arr)
    for cycleStart in range(0, n-1):
        item: Any = arr[cycleStart]
        pos: int = cycleStart

        for i in range(cycleStart+1, n):
            if arr[i] < item:
                pos += 1

        if pos == cycleStart:
            continue
        
        while item == arr[pos]:  # duplicates
            pos += 1

        arr[pos], item = item, arr[pos]  # swapping
        
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart+1, n):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1

            arr[pos], item = item, arr[pos]

    return arr
