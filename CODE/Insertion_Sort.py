def insertion_sort(a):
    for i in range(1,len(a)): 
        # Shift all the elements to right that are large than key 
        key=a[i] 
        j=i-1
        
        while j>=0 and key<a[j]: 
            a[j+1]=a[j] 
            j=j-1

        a[j+1]=key
    
    return a

def main(a):
    a=insertion_sort(a)
    print("The sorted list is:", a)