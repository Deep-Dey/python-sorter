def pivot(a,s,n):## 's' is the starting position and 'n' is the ending position
        i=s-1 ## Set the pivot index
        pivot=a[s]

        for j in range((s+1),n):
            if a[j]<=pivot:
                i=i+1
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
            
        a[i+1],a[s]=a[s],a[i+1]
        
        return i+1

def quick_sort(a,s,n):
    if s<n:
        p=pivot(a,s,n)
        quick_sort(a,s,p-1)
        quick_sort(a,p+1,n)

def main(a):
    quick_sort(a,0,len(a)-1)
    #print("The sorted list is:", a)