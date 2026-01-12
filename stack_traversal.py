def stack_on_ordertraversal(root):

    res = []
    current = root
    stack = []


    while current is not None or len(stack) >0:
        while current is not None:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        res.append(current.val)
        current = current.right
    
    return res


            