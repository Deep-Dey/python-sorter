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
