from typing import Any


out_put: list = list()

def traverse(arr: list) -> None:
    global out_put
    
    if arr[0] != None:
        traverse(arr[0])

    out_put.append(arr[1])

    if arr[2] != None:
        traverse(arr[2])


def insert(root: list, data: Any) -> None:
    if data >= root[1]:
        if root[2] == None:
            root[2] = [None, data, None]
        else:
            insert(root[2], data)

    else:
        if root[0] == None:
            root[0] = [None, data, None]
        else:
            insert(root[0], data)
#######################################################################


def tree_sort_fn(arr: list) -> None:
    global out_put
    tree = [None, None, None]
    for i in range(len(arr)):
        if tree[1] == None:
            tree = [None, arr[i], None]
        else:
            if arr[i] >= tree[1]:
                if tree[2] == None:
                    tree[2] = [None, arr[i], None]
                else:
                    insert(tree[2], arr[i])

            else:
                if tree[0] == None:
                    tree[0] = [None, arr[i], None]
                else:
                    insert(tree[0], arr[i])

    traverse(tree)

def tree_sort(arr: list) -> list:
    '''
    Tree Sort. Tree sort is a sorting algorithm that is based on Binary Search Tree data structure.
    It first creates a binary search tree from the elements of the input list or array
    and then performs an in-order traversal on the created binary search tree to get the elements in sorted order.
    ```
    TreeSort()
        1.  Take the elements input in an array.
        2.  Create a Binary search tree by inserting data items from the array into the binary search tree.
        3.  Perform in-order traversal on the tree to get the elements in sorted order.
    ```
    '''
    global out_put
    tree_sort_fn(arr)
    arr = out_put.copy()
    return arr
