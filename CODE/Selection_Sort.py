# Selection sort is an algorithm that selects the smallest element from an unsorted list in each iteration
# and places that element at the beginning of the unsorted list.
#
# Algorithm for Selection Sort:
# SelectionSort(array, size)
#   repeat (size - 1) times
#   set the first unsorted element as the minimum
#   for each of the unsorted elements
#     if element < currentMinimum
#       set element as new minimum
#   swap minimum with first unsorted position
# end SelectionSort
#############################################################################
def selection_sort(a):
    n=len(a)  
    for i in range(n):
        minimum=i

        for j in range((i+1),n):
            if a[minimum]>a[j]:
                minimum=j
        
        temp=a[i]
        a[i]=a[minimum]
        a[minimum]=temp

    return a

def main(a):
    arr=selection_sort(a)
    return arr
