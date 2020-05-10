# Quicksort is an algorithm based on divide and conquer approach
# in which the array is split into subarrays and these sub-arrays are recursively called to sort the elements.
#
# Algorithm for Quick Sort:
# quickSort(array, leftmostIndex, rightmostIndex)
#   if (leftmostIndex < rightmostIndex)
#     pivotIndex <- partition(array,leftmostIndex, rightmostIndex)
#     quickSort(array, leftmostIndex, pivotIndex)
#     quickSort(array, pivotIndex + 1, rightmostIndex)
#
# partition(array, leftmostIndex, rightmostIndex)
#   set rightmostIndex as pivotIndex
#   storeIndex <- leftmostIndex - 1
#   for i <- leftmostIndex + 1 to rightmostIndex
#   if element[i] < pivotElement
#     swap element[i] and element[storeIndex]
#     storeIndex++
#   swap pivotElement and element[storeIndex+1]
# return storeIndex + 1
################################################################################
def pivot(a,s,n):## 's' is the starting position and 'n' is the ending position
        i=s-1 ## Set the pivot index
        pivot=a[s]

        for j in range((s+1),n):
            if a[j]<=pivot:
                i=i+1
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
            
        a[i+1],a[n]=a[n],a[i+1]
        
        return i+1

def quick_sort(a,s,n):
    if s<n:
        p=pivot(a,s,n)
        quick_sort(a,s,p)
        quick_sort(a,p+1,n)
    return a

def main(a):
    arr=quick_sort(a,0,len(a)-1)
    return arr
