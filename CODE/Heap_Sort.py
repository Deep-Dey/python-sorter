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