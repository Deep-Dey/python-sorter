def counting_sort(a,position):
    n=len(a)
    counter=[0]*10
    output_list=[0]*n

    for i in range(n):
        temp=(int(a[i]/position))%10
        counter[temp]+=1

    for i in range(1,10):
        counter[i]+=counter[i-1]

    for i in range(n-1, -1, -1):
        temp=(int(a[i]/position))%10
        output_list[counter[temp]-1]=a[i]
        counter[temp]-=1
     
    return output_list

def radix_sort(a):
    maximum=max(a)
    i=1
    while int(maximum/i) > 0:
        a=counting_sort(a,i)
        i*=10
    return a

def main(a):
    arr=radix_sort(a)
    return arr
