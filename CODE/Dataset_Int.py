# This program generate Numerical values to perform sorting where number of data is given by the user 
# and store them into a TXT file named "Unsorted_Integers.txt"
#####################################################################################
def main(n):
    itemset=list()
    for j in range(n,0,-1):
        itemset.append(j)
            
#################################################### Write to a TXT file in "..\FILES\" path   
    import os

    directory_path = os.path.join(os.getcwd(), 'FILES')
    if not os.path.exists(directory_path):
                os.mkdir(directory_path)

    file_path = os.path.join(directory_path, 'Unsorted_Integers.txt')

    f = open(file_path, 'w')
    for i in itemset:
        f.write(str(i))
        f.write(' ')
    f.close()

    return itemset

