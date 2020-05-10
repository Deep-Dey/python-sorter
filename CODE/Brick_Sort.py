# An Odd-Even Sort or brick sort is a simple sorting algorithm,
# which is developed for use on parallel processors with local interconnection.
#
# Algorithm for Odd-Even Sort / Brick Sort:
# BrickSort()
#   if n>2 then
#     1. apply odd-even merge(n/2) recursively to the even subsequence a0, a2, ..., an-2
#        and to the odd subsequence a1, a3, , ..., an-1
#     2. comparison [i : i+1] for all i element {1, 3, 5, 7, ..., n-3}
#   else
#     comparison [0 : 1]
##################################################################################
def Brick_Sort(arr): 
    n=len(arr)
    flag=0
    while flag == 0: 
        flag=1

        for i in range(1, n-1, 2): 
            if arr[i]>arr[i+1]: 
                arr[i], arr[i+1]=arr[i+1], arr[i] 
                flag=0
                  
        for i in range(0, n-1, 2): 
            if arr[i]>arr[i+1]: 
                arr[i], arr[i+1]=arr[i+1], arr[i] 
                flag=0
      
    return arr

def main(a):
    arr=Brick_Sort(a)
    return arr