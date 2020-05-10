# Counting sort is a sorting algorithm that sorts the elements of an array
# by counting the number of occurrences of each unique element in the array.
#
# Algorithm for Counting Sort:
# countingSort(array, size)
#   max <- find largest element in array
#   initialize count array with all zeros
#   for j <- 0 to size
#     find the total count of each unique element and 
#     store the count at jth index in count array
#   for i <- 1 to max
#     find the cumulative sum and store it in count array itself
#   for j <- size down to 1
#     restore the elements to array
#     decrease count of each element restored by 1
########################################################################
def counting_sort(a):
    n=len(a)
    maximum=max(a)
    maximum=maximum+1
    counter=[0]*maximum
    output_list=[0]*n

    for i in range(n):
        counter[a[i]]+=1

    for i in range(1,maximum):
        counter[i]+=counter[i-1]

    for i in range(n):
        output_list[counter[a[i]]-1]=a[i]
        counter[a[i]]-=1
        
    a=output_list

    return a

def main(a):
    arr=counting_sort(a)
    return arr
