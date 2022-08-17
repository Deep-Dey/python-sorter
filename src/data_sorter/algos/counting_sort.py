from typing import Any


def counting_sort(arr: list) -> list:
    '''
    Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array.
    ```
    counting_sort(array, size)
      max <- find largest element in array
      initialize count array with all zeros
      for j <- 0 to size
        find the total count of each unique element and 
        store the count at jth index in count array
      for i <- 1 to max
        find the cumulative sum and store it in count array itself
      for j <- size down to 1
        restore the elements to array
        decrease count of each element restored by 1
    end counting_sort
    ```
    '''
    n: int = len(arr)
    maximum: Any = max(arr)
    maximum = maximum + 1
    counter: list = [0] * maximum
    output_list: list = [0] * n

    for i in range(n):
        counter[arr[i]] += 1

    for i in range(1, maximum):
        counter[i] += counter[i-1]

    for i in range(n):
        output_list[counter[arr[i]]-1] = arr[i]
        counter[arr[i]] -= 1

    return output_list
