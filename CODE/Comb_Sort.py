# Comb sort is a comparison based sorting algorithm which improves on bubble sort.

# Pseudo code for Comb Sort:
# CombSort()
# 	1.    Create variables gap and swapped and constant SHRINK_FACTOR and initialize as below:
# 	          i. gap = size of the array
# 	         ii. swapped = false
# 	        iii. SHRINK_FACTOR = 1.3
# 	    'swapped' is used to check whether any 2 elements have been swapped at the end of an iteration,
# 		 like it is used in Bubble Sort algorithm for optimization.
# 	2.    Set swapped = false
# 	3.    Set gap = (int) (gap/SHRINK_FACTOR).
# 	4.    Iterate over the array from i = 0 to i < n - gap:
# 	    a.    If array[i] > array[i + gap]
# 	         i.    swap the elements array[i] and array[i + gap], to arrange in sorted order
# 	        ii.    set swapped = true
# 	5.    Repeat steps 2-4 while gap != 1 and swapped = true
#####################################################################################
def getNextGap(gap): # To find next gap from current
	gap = (gap * 10)//13 # Shrink gap by Shrink factor 
	if gap < 1: 
		return 1
	return gap 
    
def comb_Sort(arr): 
	n = len(arr) 
	gap = n 
 
	while gap !=1: 
		gap = getNextGap(gap) 

		for i in range(0, n-gap): 
			if arr[i] > arr[i + gap]: 
				arr[i], arr[i + gap]=arr[i + gap], arr[i]
	return arr

def main(a):
    arr=comb_Sort(a)
    return arr
