def Stooge_Sort(arr, l, h): 
    if l < h:
        if arr[l]>arr[h]: 
            arr[l], arr[h] = arr[h], arr[l]
        
        if h-l > 1: ## If there are more than 2 elements in the array(starts from 0)
            t = (int)((h-l + 1)/3) 
            Stooge_Sort(arr, l, (h-t)) ## Recursively sort first 2/3 elements 
            Stooge_Sort(arr, l + t, (h)) ## Recursively sort last 2/3 elements 
   
            Stooge_Sort(arr, l, (h-t)) ## Recursively sort first 2/3 elements again to confirm 

    return arr

def main(a):
    a=Stooge_Sort(a, 0, len(a)-1)
    print("The sorted list is:", a)