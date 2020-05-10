# Strand sort is a recursive sorting algorithm that sorts items of a list into increasing order.
# It has O(n2) worst time complexity which occurs when the input list is reverse sorted.
#
# Algorithm for Strand Sort:
# StrandSort()
#     1.    Let ip[] be input list and op[] be output list.
#     2.    Create an empty sublist and move first item of ip[] to it.
#     3.    Traverse remaining items of ip. For every item x, check if x is greater than last inserted item to sublist. If yes, remove x from ip and add at the end of sublist. If no, ignore x (Keep it it in ip)
#     4.    Merge sublist into op (output list)
#     5.    Recur for remaining items in ip and current items in op.
####################################################################################
import Merge_Sort

def Strand_Sort(input_list):
    output_list=list()
    
    while len(input_list) > 0:
        sub_list=[input_list.pop(0)]
        pos=0

        while pos<len(input_list):
            if input_list[pos]>sub_list[-1]:
                sub_list.append(input_list.pop(pos))
            else:
                pos+=1

        temp_list=output_list+sub_list  ## For calling the module
        output_list=Merge_Sort.merge(temp_list, output_list, sub_list) ## Module
        
    return output_list

def main(a):
    arr=Strand_Sort(a)
    return arr