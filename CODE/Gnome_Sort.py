def Gnome_Sort(arr):
    n=len(arr) 
    pos=0
    while pos<n: 
        if pos==0: 
            pos=pos+1
        elif arr[pos]>=arr[pos-1]: 
            pos=pos+1
        else: 
            arr[pos], arr[pos-1] = arr[pos-1], arr[pos] ##swapping
            pos=pos-1
  
    return arr

def main(a):
    a=Gnome_Sort(a)
    print("The sorted list is:", a)