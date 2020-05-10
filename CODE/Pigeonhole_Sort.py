# Pigeonhole sorting is a sorting algorithm that is suitable for sorting lists of elements
# where the number of elements and the number of possible key values are approximately the same.
#
# Algorithm for PigeonHole Sort:
# PigeonHoleSort()
#     1.  Find minimum and maximum values in array.
#         Let the minimum and maximum values be ‘min’ and ‘max’ respectively.
#         Also find range as ‘max-min+1’.
#     2.  Set up an array of initially empty “pigeonholes” the same size as of the range.
#     3.  Visit each element of the array and then put each element in its pigeonhole.
#         An element arr[i] is put in hole at index arr[i] – min.
#     4.  Start the loop all over the pigeonhole array in order
#         and put the elements from non- empty holes back into the original array.
################################################################################
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