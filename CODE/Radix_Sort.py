# Radix sort is a sorting technique that sorts the elements by first grouping the individual digits of the same place value.
# Then, sort the elements according to their increasing/decreasing order.
#
# Algorithm for Radix Sort:
# radixSort(array)
#   d <- maximum number of digits in the largest element
#   create d buckets of size 0-9
#   for i <- 0 to d
#     sort the elements according to ith place digits using countingSort
#
# countingSort(array, d)
#   max <- find largest element among dth place elements
#   initialize count array with all zeros
#   for j <- 0 to size
#     find the total count of each unique digit in dth place of elements and
#     store the count at jth index in count array
#   for i <- 1 to max
#     find the cumulative sum and store it in count array itself
#   for j <- size down to 1
#     restore the elements to array
#     decrease count of each element restored by 1
####################################################################################
def counting_sort(a,position):
    n=len(a)
    counter=[0]*10
    output_list=[0]*n

    for i in range(n):
        temp=(int(a[i]/position))%10
        counter[temp]+=1

    for i in range(1,10):
        counter[i]+=counter[i-1]

    for i in range(n-1, -1, -1):
        temp=(int(a[i]/position))%10
        output_list[counter[temp]-1]=a[i]
        counter[temp]-=1
     
    return output_list

def radix_sort(a):
    maximum=max(a)
    i=1
    while int(maximum/i) > 0:
        a=counting_sort(a,i)
        i*=10
    return a

def main(a):
    arr=radix_sort(a)
    return arr
