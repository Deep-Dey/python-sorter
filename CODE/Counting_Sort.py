def counting_sort(a):
    n=len(a)
    maximum=max(a)
    maximum=maximum+1
    counter=[0]*maximum
    output_list=[0]*n

    for i in range(n):
        counter[a[i]]+=1

    for i in range(1,maximum):
        counter[i]+=counter[i-1]

    for i in range(n):
        output_list[counter[a[i]]-1]=a[i]
        counter[a[i]]-=1
        
    a=output_list

    return a

def main(a):
    a=counting_sort(a)
    print("The sorted list is:", a)
