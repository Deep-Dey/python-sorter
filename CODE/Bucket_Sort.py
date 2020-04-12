import Selection_Sort


def bucket_sort(a):
    output=list()
    index=list()
    n=len(a)
    for i in range(n):##make a list 2D
        index.append([])
    
    for i in range(n):
        temp=int(a[i]*n)
        index[temp].append(a[i])

    for i in range(n):
        index[i]=Selection_Sort.selection_sort(index[i])

    for i in range(n):
        output=output+index[i]
    return output


def main(a):
    ## Bucket sort cannot be performed for integer value
    ## So we convert all integer into fraction
    m=max(a)
    i=1
    while int(m/i)>0:
        i*=10
    
    for data in range(len(a)):
        a[data]=a[data]/i

    a=bucket_sort(a)

    for data in range(len(a)):
        a[data]=int(a[data]*i)
    #print("The sorted list is:", a)