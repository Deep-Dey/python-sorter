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
