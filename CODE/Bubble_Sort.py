def bubble_sort(a):
    for i in range(len(a)):
        for j in range((len(a)-i-1)):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
    

def main(a):
    a=bubble_sort(a)
    #print("The sorted list is:", a)