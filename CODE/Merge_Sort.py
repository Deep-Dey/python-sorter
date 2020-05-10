# Merge Sort is a kind of Divide and Conquer algorithm in computer programming.
#
# Pseudo code for Merge Sort:
# MergeSort(A, p, r):
#     if p > r 
#         return
#     q = (p+r)/2
#     MergeSort(A, p, q)
#     MergeSort(A, q+1, r)
#     merge(A, p, q, r)
#########################################################################################
def merge(a,L,R):
    i=0
    j=0
    k=0
          
    while i<len(L) and j<len(R): 
        if L[i]<R[j]: 
            a[k]=L[i] 
            i=i+1
        else: 
            a[k]=R[j] 
            j=j+1
        k=k+1
          
    while i<len(L): 
        a[k]=L[i] 
        i=i+1
        k=k+1
          
    while j<len(R): 
        a[k]=R[j] 
        j=j+1
        k=k+1 

    return a

def merge_sort(a): 
    if len(a)>1: 
        mid=len(a)//2 
        L=a[:mid]  
        R=a[mid:] 
  
        merge_sort(L) 
        merge_sort(R)   

        a=merge(a,L,R)
    
    return a

def main(a):
    arr=merge_sort(a)
    return arr