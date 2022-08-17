from data_sorter.algos.merge_sort import merge


def strand_sort(arr: list) -> list:
    '''
    Strand sort is a recursive sorting algorithm that sorts items of a list into increasing order.
    It has O(n2) worst time complexity which occurs when the input list is reverse sorted.
    ```
    StrandSort()
        1.    Let ip[] be input list and op[] be output list.
        2.    Create an empty sublist and move first item of ip[] to it.
        3.    Traverse remaining items of ip. For every item x, check if x is greater than last inserted item to sublist. If yes, remove x from ip and add at the end of sublist. If no, ignore x (Keep it it in ip)
        4.    Merge sublist into op (output list)
        5.    Recur for remaining items in ip and current items in op.
    ```
    '''
    output_list: list = list()

    while len(arr) > 0:
        sub_list: list = [arr.pop(0)]
        pos: int = 0

        while pos < len(arr):
            if arr[pos] > sub_list[-1]:
                sub_list.append(arr.pop(pos))
            else:
                pos += 1

        temp_list: list = output_list + sub_list  # For calling the module
        output_list: list = merge(temp_list, output_list, sub_list)  # Module

    return output_list
