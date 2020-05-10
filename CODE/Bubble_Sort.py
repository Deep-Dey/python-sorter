# Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list,
# compares adjacent elements and swaps them if they are in the wrong order.
# 
# Pseudo code for Bubble Sort:
# procedure bubbleSort(A : list of sortable items)
#     n := length(A)
#     repeat
#         swapped := false
#         for i := 1 to n - 1 inclusive do
#             if A[i - 1] > A[i] then
#                 swap(A[i - 1], A[i])
#                 swapped = true
#             end if
#         end for
#         n := n - 1
#     until not swapped
# end procedure
############################################################################
def bubble_sort(a):
    for i in range(len(a)):
        for j in range((len(a)-i-1)):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
    

def main(a):
    arr=bubble_sort(a)
    return arr