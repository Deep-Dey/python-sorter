def selection_sort(a):
    n=len(a)  
    for i in range(n):
        minimum=i

        for j in range((i+1),n):
            if a[minimum]>a[j]:
                minimum=j
        
        temp=a[i]
        a[i]=a[minimum]
        a[minimum]=temp

    return a

def main(a):
    arr=selection_sort(a)
    return arr
