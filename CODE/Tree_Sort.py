# Tree Sort. Tree sort is a sorting algorithm that is based on Binary Search Tree data structure.
# It first creates a binary search tree from the elements of the input list or array
# and then performs an in-order traversal on the created binary search tree to get the elements in sorted order.
#
# Algorithm for Tree Sort:
# TreeSort()
#     1.  Take the elements input in an array.
#     2.  Create a Binary search tree by inserting data items from the array into the binary search tree.
#     3.  Perform in-order traversal on the tree to get the elements in sorted order.
########################################################################################
out_put=list()
def traverse(a):
    global out_put
    if a[0]!=None:
        traverse(a[0])

    out_put.append(a[1])
    
    if a[2]!=None:
        traverse(a[2])
#######################################################################
def insert(root, data):
    if data>=root[1]:
        if root[2]==None:
            root[2]=[None, data, None]
        else:
            insert(root[2],data)

    else:
        if root[0]==None:
            root[0]=[None, data, None]
        else:
            insert(root[0],data)
#######################################################################
def Tree_Sort(a):
    global out_put
    tree=[None,None,None]
    for i in range(len(a)):
        if tree[1]==None:
            tree=[None,a[i],None]
        else:
            if a[i]>=tree[1]:
                if tree[2]==None:
                    tree[2]=[None, a[i], None]
                else:
                    insert(tree[2],a[i])

            else:
                if tree[0]==None:
                    tree[0]=[None, a[i], None]
                else:
                    insert(tree[0],a[i])
    
    traverse(tree)
#######################################################################
def main(a):
    global out_put
    Tree_Sort(a)
    arr=out_put
    return arr
    

