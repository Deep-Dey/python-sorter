# Heapsort is a comparison-based sorting algorithm.
# In the first step, the Heapsort algorithm involves preparing the list by first turning it into a max heap.
# In the second step, a sorted array is created by 
# repeatedly removing the largest element from the heap and inserting it into the array.

# Pseudo code for Heap Sort:
# HeapSort()  
#     1.  Call the buildMaxHeap() function on the list. Also referred to as heapify(), this builds a heap from a list in O(n) operations.
#     2.  Swap the first element of the list with the final element. Decrease the considered range of the list by one.
#     3.  Call the siftDown() function on the list to sift the new first element to its appropriate index in the heap.
#     4.  Go to step (2) unless the considered range of the list is one element.
###########################################################################################
def heapify(a,n,i): 
    maximum=i 
    l=2*i+1 
    r=2*i+2  
  
    if l<n and a[i]<a[l]: 
        maximum=l 
   
    if r<n and a[maximum]<a[r]: 
        maximum=r 
  
    if maximum!=i: 
        a[i],a[maximum]=a[maximum],a[i]
        heapify(a,n,maximum)

def heapSort(a): 
    n=len(a) 
    for i in range(n,-1,-1): ## Build a maxheap 
        heapify(a,n,i) 
  
    for i in range(n-1,0,-1): 
        a[i],a[0]=a[0],a[i] ## Swap Kore Max take laste Pathachhe
        heapify(a,i,0)
    return a

def main(a):
    arr=heapSort(a)
    return arr