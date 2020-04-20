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
