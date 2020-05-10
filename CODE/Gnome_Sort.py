# The gnome sort is a sorting algorithm which is similar to insertion sort in that it works with one item at a time 
# but gets the item to the proper place by a series of swaps, similar to a bubble sort.
#
# Pseudo code for Gnome Sort:
# procedure gnomeSort(a[]):
#     pos := 0
#     while pos < length(a):
#         if (pos == 0 or a[pos] >= a[pos-1]):
#             pos := pos + 1
#         else:
#             swap a[pos] and a[pos-1]
#             pos := pos - 1
##############################################################################
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
    arr=Gnome_Sort(a)
    return arr