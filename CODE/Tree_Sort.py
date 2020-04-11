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
    a=out_put
    print("The sorted list is:", a)
    

