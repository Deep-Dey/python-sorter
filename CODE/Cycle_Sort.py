# It is based on the idea that the permutation to be sorted can be factored into cycles,
# which can individually be rotated to give a sorted result.
#
# Algorithm for Cycle Sort:
# CycleSort()
#     1. If the element is already at the correct position then
#             do nothing.
#     2. else 
#             we will write it to its intended position.
#             That position is inhabited by a different element b,
#             which we then have to move to its correct position.
#             This process of displacing elements to their correct positions continues
#             until an element is moved to the original position of a. This completes a cycle.
##################################################################################################
def cycleSort(a):
    for cycleStart in range(0,len(a) - 1):
        item=a[cycleStart]
        pos=cycleStart

        for i in range(cycleStart+1,len(a)):
            if a[i] < item:
                pos+=1

        if pos==cycleStart:
            continue

        while item==a[pos]: ## duplicates
            pos+=1

        a[pos],item=item,a[pos] ## swapping
####################################################################
        while pos!=cycleStart:
            pos=cycleStart 
            for i in range(cycleStart+1,len(a)):
                if a[i] < item:
                    pos+=1

            while item==a[pos]:
                pos+=1

            a[pos],item=item,a[pos]

    return a

def main(a):
    arr=cycleSort(a)
    return arr
