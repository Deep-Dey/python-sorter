# Insertion sort is a sorting algorithm
# that places an unsorted element at its suitable place in each iteration.
#
# Algorithm for Insertion Sort:
# insertionSort(array)
#   mark first element as sorted
#   for each unsorted element X
#     'extract' the element X
#     for j <- lastSortedIndex down to 0
#       if current element j > X
#         move sorted element to the right by 1
#     break loop and insert X here
# end insertionSort
##############################################################################
def insertion_sort(a):
    for i in range(1,len(a)): 
        # Shift all the elements to right that are large than key 
        key=a[i] 
        j=i-1
        
        while j>=0 and key<a[j]: 
            a[j+1]=a[j] 
            j=j-1

        a[j+1]=key
    
    return a

def main(a):
    arr=insertion_sort(a)
    return arr