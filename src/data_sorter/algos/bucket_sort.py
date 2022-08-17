from selection_sort import selection_sort


def bucket_sort(arr):
    '''
    **Bucket sort cannot be performed for integer value**

    Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an arr into a number of buckets.\n
    ```
    bucket_sort()
      create N buckets each of which can hold a range of values
      for all the buckets
        initialize each bucket with 0 values
      for all the buckets
        put elements into buckets matching the range
      for all the buckets 
        sort elements in each bucket
      gather elements from each bucket
    end bucketSort
    ```
    '''
    # Create empty buckets
    bucket: list = [[] for _ in range(len(arr))]

    # Insert elements into their respective buckets
    for j in arr:
        index_b: int = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(arr)):
        bucket[i] = selection_sort(bucket[i])

    # Get the sorted elements
    k: int = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr