def pigeonhole_sort(a):
    minimum = min(a) 
    maximum = max(a) 
    n = maximum - minimum + 1
  
    holes = [0] * n ## List of pigeonholes

    for i in a: 
        i=int(i)
        holes[i - minimum] += 1
   
    i = 0
    for count in range(n): ## Put the elements back into the array in order.
        while holes[count] > 0: 
            holes[count] -= 1
            a[i] = count + minimum 
            i += 1

    return a

def main(a):
    arr=pigeonhole_sort(a)
    return arr