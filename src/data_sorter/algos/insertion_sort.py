def insertion_sort(arr: list) -> list:
    '''
    Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
    ```
    insertionSort(array)
      mark first element as sorted
      for each unsorted element X
        'extract' the element X
        for j <- lastSortedIndex down to 0
          if current element j > X
            move sorted element to the right by 1
        break loop and insert X here
    end insertionSort
    ```
    '''
    for i in range(1,len(arr)): 
        # Shift all the elements to right that are large than key 
        key=arr[i] 
        j=i-1
        
        while j>=0 and key<arr[j]: 
            arr[j+1]=arr[j] 
            j=j-1

        arr[j+1]=key
    
    return arr