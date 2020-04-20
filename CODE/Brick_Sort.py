def Brick_Sort(arr): 
    n=len(arr)
    flag=0
    while flag == 0: 
        flag=1

        for i in range(1, n-1, 2): 
            if arr[i]>arr[i+1]: 
                arr[i], arr[i+1]=arr[i+1], arr[i] 
                flag=0
                  
        for i in range(0, n-1, 2): 
            if arr[i]>arr[i+1]: 
                arr[i], arr[i+1]=arr[i+1], arr[i] 
                flag=0
      
    return arr

def main(a):
    arr=Brick_Sort(a)
    return arr