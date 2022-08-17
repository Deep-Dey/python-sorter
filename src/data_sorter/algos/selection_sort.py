def selection_sort(arr):
    '''
    Selection sort is an algorithm that selects the smallest element from an unsorted list in each iteration
    and places that element at the beginning of the unsorted list.
    
    ```
    SelectionSort(array, size)
      repeat (size - 1) times
      set the first unsorted element as the minimum
      for each of the unsorted elements
        if element < currentMinimum
          set element as new minimum
      swap minimum with first unsorted position
    end SelectionSort
    ```
    '''
    n: int = len(arr)
    for i in range(n):
        minimum: int = i

        for j in range((i+1), n):
            if arr[minimum] > arr[j]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr
