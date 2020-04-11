def Brick_Sort(a): 
    n=len(a)
    flag=0
    while flag == 0: 
        flag=1

        for i in range(1, n-1, 2): 
            if a[i]>a[i+1]: 
                a[i], a[i+1]=a[i+1], a[i] 
                flag=0
                  
        for i in range(0, n-1, 2): 
            if a[i]>a[i+1]: 
                a[i], a[i+1]=a[i+1], a[i] 
                flag=0
      
    return a

def main(a):
    a=Brick_Sort(a)
    print("The sorted list is:", a)